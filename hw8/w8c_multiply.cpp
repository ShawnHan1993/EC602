// AUTHOR Shen_Han shawnhan@bu.edu
// AUTHOR Changlong_Jiang cljiang@bu.edu

#include <iostream>
#include <string>
#include <vector>
#include <fstream>
using namespace std;
typedef vector<vector<int>> int_matrix;
typedef vector<vector<double>> double_matrix;
int checkInput(int n,char const *argu[],ifstream &A,ifstream &B,int &M,int &N,int &L){
	if ((n != 8) && (n != 6))
		return 1;
    string argu1(argu[1]);
	if ((argu1.compare("double")==0) || (argu1.compare("int")==0))
		;
    else
        return 1;

    if (n==6){
		try {
			N = stoi(argu[2]);
			M = N; L = N;
			if (N <1)
				return 1;
		}
		catch (...) {
			return 1;
		}
		A.open(argu[3]);
		B.open(argu[4]);
		if (A.fail() == 1 || B.fail() == 1)
			return 2;
        return 0;
    }
    else if (n==8){
        try
        {
            M=stoi(argu[2]);
            N=stoi(argu[3]);
            L=stoi(argu[4]);
			if (N <1 || M <1 || L <1)return 1;
        }
        catch (...)
        {
            return 1;
        }
		A.open(argu[5]);
		B.open(argu[6]);
		if (A.fail() == 1 || B.fail() == 1)
			return 2;
        return 0;
    }
    return 1;
}

template <typename T>
vector<vector<T>> Max(vector<vector<T>> const& A, vector<vector<T>> const&B) {
	int M = A.size();
	int N = A[0].size();
	int L = B[0].size();

	vector<vector<T>> c(M, vector<T>(L));

	for (int i = 0; i<M; i++)
		for (int j = 0; j<L; j++)
			for (int k = 0; k<N; k++)
				c[i][j] += A[i][k] * B[k][j];

	return c;
}

template <typename C>
void write(C const&re,ofstream &reFile,int M,int L) {
	for (int i = 0; i < M; i++) {
		for (int j = 0; j < L; j++) {
			reFile << re[i][j];
			reFile << ' ';
		}
		reFile << endl;
	}
	reFile.close();
	return;
}

template <typename K>
int file2mat(vector<vector<K>> &A,ifstream &fileA,int M,int N) {
	int i = 0, j = 0, counter = 0;
	K tmp=0;
	try {
		while (fileA >> tmp) {
			if (i > (M-1))
				return 3;
			A.at(i).at(j) = tmp;
			j++; counter++;
			if (j == N) {
				j = 0;
				i++;
			}
		}
		if (counter != M*N) return 3;
		return 0;
	}
	catch (...){ return 3; }

}

int main(int argc,char const *argv[])
{
    ifstream fileA,fileB;
	ofstream fileC;
    int M=0,N=0,L=0;
    int checkCode=checkInput(argc,argv,fileA,fileB,M,N,L);
    if (checkCode!=0) return checkCode;  
	try {
		string argu1(argv[argc-1]);
		if (argu1.compare("UNREADABLE") == 0)
			return 4;
		fileC.open(argv[argc - 1]);
	}
	catch (...) {
		return 4;
	}
    /***input the matrix***/
    if (argc==6){
        string argu1(argv[1]);
        if ( argu1.compare("double")==0){
            double_matrix A(N, vector<double>(N));double_matrix B(N, vector<double>(N));double_matrix re(N, vector<double>(N));

			checkCode = file2mat<double>(A, fileA, M, N);
			if (checkCode != 0)return checkCode;
			checkCode = file2mat<double>(B, fileB, N, L);
			if (checkCode != 0)return checkCode;

			fileA.close();
			fileB.close();
			re = Max<double>(A, B);
			write<double_matrix>(re, fileC, N, N);
        }
        else
        {
            int_matrix A(N, vector<int>(N));int_matrix B(N, vector<int>(N));int_matrix re(N, vector<int>(N));

			checkCode = file2mat<int>(A, fileA, M, N);
			if (checkCode != 0)return checkCode;
			checkCode = file2mat<int>(B, fileB, N, L);
			if (checkCode != 0)return checkCode;

			fileA.close();
			fileB.close();
			re = Max<int>(A, B);
			write<int_matrix>(re, fileC, N, N);
        }    
   
    }
    else{
        string argu1(argv[1]);
        if ( argu1.compare("double")==0){
            double_matrix A(M, vector<double>(N));double_matrix B(N, vector<double>(L));double_matrix re(M, vector<double>(L));

			checkCode = file2mat<double>(A, fileA, M, N);
			if (checkCode != 0)return checkCode;
			checkCode = file2mat<double>(B, fileB, N, L);
			if (checkCode != 0)return checkCode;

			fileA.close();
			fileB.close();
			re = Max<double>(A, B);
			write<double_matrix>(re, fileC, M, L);
        }
        else
        {
            int_matrix A(M, vector<int>(N));int_matrix B(N, vector<int>(L));int_matrix re(M, vector<int>(L));

			checkCode = file2mat<int>(A, fileA, M, N);
			if (checkCode != 0)return checkCode;
			checkCode = file2mat<int>(B, fileB, N, L);
			if (checkCode != 0)return checkCode;

			fileA.close();
			fileB.close();
			re = Max<int>(A, B);
			write<int_matrix>(re, fileC, M, L);
        }
        }
    /***_____***/
	

    return 0;
   

}