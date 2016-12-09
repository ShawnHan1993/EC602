// AUTHOR Shen Han shawnhan@bu.edu
// AUTHOR Changlong Jiang cljiang@bu.edu
// AUTHOR Xinyu Li lxinyu@bu.edu

#include <iostream>
#include <math.h>
using namespace std;
double giveElectonNum(double radio,int ifNoNeuton=0){

	double mEarth=5.97e24;
	double mProton=1.6726e-27;
	if (ifNoNeuton==1)
		return (long int)mEarth/mProton;
	else{
		double protonRadio=1/(1/radio+1);
		double cc=round((mEarth*protonRadio)/mProton)/pow(2,43);
		return cc;
	}
}
double estimatedBoundRadio=0.95;
double lowerBoundRadio=0.87;
double upperBoundRadto=1;
int main() {
	double a1=giveElectonNum(estimatedBoundRadio);
	double a2=giveElectonNum(lowerBoundRadio);
	double a3=giveElectonNum(upperBoundRadto);
	cout<<a1<<endl;
	cout<<a2<<endl;
	cout<<a3<<endl;
	return 0;
}
