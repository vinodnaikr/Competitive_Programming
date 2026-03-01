#include<iostream>
using namespace std;

int main(){
	cout<<"Program starts here"<<endl;
	union{
		int num1;
		long num2;
	};
	
	num2=256*2561+5;
	cout<<num2<<endl;
	cout<<num1<<endl;
	return 0;
}
