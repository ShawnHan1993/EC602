/*Copyright [2016] <Copyright Shawn&Changlong>*/
#include<iostream>
#include<map>
#include<fstream>
#include<string>
#include<algorithm>
#include<vector>
using std::string;
using std::cout;
using std::cin;
using std::endl;
using std::vector;
using std::ifstream;
using std::map;

int main(int argc, char const *argv[]) {
    ifstream wordlistFile;
    wordlistFile.open(argv[1]);
    string word;
    map<int, map<string, vector<string>>> bigDict;
    while (wordlistFile >> word) {
        string tmp = word;
        sort(tmp.begin(), tmp.end());
        bigDict[tmp.length()][tmp].push_back(word);
    }
    string check;
    int n;
    while (1) {
        vector<string> result;
        cin >> check >> n;
        if (n == 0)
            return 0;
        sort(check.begin(), check.end());
        if (check.length() == n)
            result = bigDict[n][check];
        if (check.length() > n) {
            int *cur = new int[n];
            for (int i = 0; i < n; i++)
                cur[i] = i;
            bool flag = true;
            while (flag) {
                string curMat;
                for (int i = 0; i < n; i++)
                    curMat.push_back(check[cur[i]]);
                vector<string> tmp = bigDict[n][curMat];
                result.insert(result.end(), tmp.begin(), tmp.end());
                for (int i = n - 1; i > -1; i--) {
                    int stop = check.length() - n + i;
                    int tmp = cur[i];
                    cur[i] = stop + 1;
                    while (tmp < stop) {
                        tmp++;
                        if (check[tmp] != check[tmp - 1]) {
                            cur[i] = tmp;
                            break;
                        }
                    }
                    if (cur[i] > stop) {
                        if (i == 0) {
                            flag = false;
                            break;
                        }
                        continue;
                    }
                    for (int kk = i + 1; kk < n; kk++)
                        cur[kk] = cur[kk - 1] + 1;
                    break;
                }
            }
        }
        sort(result.begin(), result.end());
        for (int i = 0; i < result.size(); i++)
            cout << result[i] << endl;
        cout << '.' << endl;
    }
    return 0;
}
