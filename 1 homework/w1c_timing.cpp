// AUTHOR ShenHan shawnhan@bu.edu
// AUTHOR ChanglongJiang cljiang@bu.edu

#include <iostream>
#include <ctime>
#include <stdlib.h>
#include <math.h>

using namespace std;

int main() {
	clock_t start_clock_a,end_clock_a;
	clock_t start_clock_b,end_clock_b;
	clock_t start_clock_c,end_clock_c;
	short unsigned int a=1;
	unsigned int b=1;
	long unsigned int c=1;
	start_clock_a=clock();
	while(a!=0){
		a++;
	}
	end_clock_a=clock();
	double mincroseconds_a=(double)(end_clock_a-start_clock_a)/CLOCKS_PER_SEC*1000000;
	cout << "short unsigned int time (mincroseconds): "<<mincroseconds_a << endl;
	start_clock_b=clock();
	while(b!=0){
		b++;
	}
	end_clock_b=clock();
	double seconds_b=(double)(end_clock_b-start_clock_b)/CLOCKS_PER_SEC;
	cout << "unsigned int time (seconds): "<<seconds_b<<endl;
	int bytesOfInt=sizeof(b);
	//cout<<bytesOfInt<<endl;
	int bytesOfLong=sizeof(c);
	//cout<<bytesOfLong<<endl;
	long int times=pow(2,(bytesOfLong-bytesOfInt)*8);
	//cout<<times<<endl;
	long double years_c=(times*seconds_b)/60/60/24/365.25;
	/*start_clock_c=clock();
	while(c!=0){
		c++;
	}
	end_clock_c=clock();
	double years_c=(double)(end_clock_c-start_clock_c)/CLOCKS_PER_SEC/31536000;*/
	cout << "long unsigned int time (years): "<<years_c<<endl;
	return 0;
}
