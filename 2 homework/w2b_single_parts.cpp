// AUTHOR Shen Han shawnhan@bu.edu
// AUTHOR Changlong Jiang cljiang@bu.edu
// AUTHOR Xinyu Li lxinyu@bu.edu

#include <iostream>
#include <iomanip>
using namespace std;

typedef unsigned int raw32;

struct Single_Parts{
	raw32 fraction:23;
	raw32 exponent:8;
	raw32 sign:1;
};

const raw32 MASK_SIGN=1<<31;
const raw32 MASK_BEXP=0xff<<23;
const raw32 MASK_FRAC=0x7fffff;
// single_parts

// print out the parts of the structure Single_Parts
void print_sp(Single_Parts sp)
{
  if (sp.sign==1)
		 cout << "negative"  << endl;
  else
  		cout << "positive" << endl;

 cout << hex
      //<< setfill('0')
      << "expo: " << sp.exponent << endl
      << "frac: " << sp.fraction << endl
      << dec;
}

// define Single_Parts, build(), and take_apart() for float
Single_Parts take_apart(float s){
	raw32 x;
	Single_Parts sp;
	x=*reinterpret_cast<raw32*>(&s);

	sp.sign=(x bitand MASK_SIGN)>>31;
	sp.exponent=(x bitand MASK_BEXP)>>23;
	sp.fraction=(x bitand MASK_FRAC);
	 return sp;
}

float build(Single_Parts sp)
{
       // read this from inside out:
       // this means get the address of dp, then think of it as a pointer to a double
       // then get the double and return it.
       return *reinterpret_cast<float*>(&sp);
}

int main()
{

	float num_from_build;

	float numbers[5]={1.0/3,2,1.3e10,3e11,6};

	// show the structure of the numbers
	for (int i=0;i<5;i++)
	{
		// take apart the numbers, then re-build to test that it works.

		Single_Parts sp= take_apart(numbers[i]);
	 	num_from_build = build(sp);

	 	cout << endl;
	    print_sp(sp);
	 	cout << numbers[i] << " " << num_from_build  << endl;
	}

    // example of a weird number, negative zero.
    double neg_zero{-0.0};

    cout << endl;
    cout << neg_zero << endl;

    print_sp(take_apart(neg_zero));

    return 0;
}
