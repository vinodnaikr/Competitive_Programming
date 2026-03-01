#include<iostream>
#include<conio.h>
#include<math.h>
using namespace std;

long gcd(long a ,long b){
	long num1,num2,temp;
	
	if(a>=b){
		num1=a;
		num2=b;
	}
	else{
		num1=b;
		num2=a;
	}
	while(num2!=0){
		temp=num1%num2;
		num1=num2;
		num2=temp;
		
	}
	return num1;
}

int main()
{
	cout<<"Program accuracy starts:"<<endl;
	long k , m, result;
	cout<<"Enter the value of k:";
	cin>>k;
	cout<<"Enter the value of m:";
	cin>>m;
	result=gcd(k,m);
	cout<<"GCD is:"<<result<<endl;
	return 0;
}

