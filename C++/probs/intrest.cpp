#include<iostream>
#include<cmath>
using namespace std;

int main()
{
	float t=10,n=4,r=0.12;
	float p=5000,A;
	A=p*pow((1+r/n),(n*t));
	cout<<"The Amount Returned after 10 years is:"<<A<<endl;
	return 0;
}
