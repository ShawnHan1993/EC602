// Show the command line argument values.
#include <iostream>
#include <string> // provides stoX where X can be i (int), d (double), etc.

using namespace std;
int main(int argc, char const *argv[])
{
    // the following example shows what argc and argv are
    //
    // c-strings are hard to use properly and are dangerous.
    int i,j;

    cout << "argc is " << argc << endl;
    for (i=0; i<argc; i++){
        //print out argv[i]

        cout << "argv of " << i << " is " << argv[i] << endl;
        
        //print out argv[i], discover its length
        j=0;
        while ( argv[i][j])  // equivalent to (argv[i][j] != '\0')
             cout << argv[i][j++];

        cout << " len " << j;

        // alternative
        string s(argv[i]);
        cout << " len " << s.size();
        cout << endl;
    }
}