#include<iostream>
using namespace std;

long factor(int n);

int main(){
	int n;
	long fact;
	cout<<"Program starts"<<endl;
	cout<<"Enter n value:"<<endl;
	cin>>n;
	if(n<1||n>10){
		cout<<"Error in input";
	}
	else{
		fact=factor(n);
		cout<<"Factorial of "<<n<<"is"<<fact<<endl;
	}
	return 0;
}

long factor(int n){
	int I; long temp=1;
	
	for(I=2;I<=n;I++){
		temp=temp*I;
	}
	return temp;
}
