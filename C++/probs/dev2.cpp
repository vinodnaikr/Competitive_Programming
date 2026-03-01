#include<iostream>
#include<conio.h>
using namespace std;

int main()
{
	int spoon=4, fork=5;
	int & cutlery=fork;
	cout<<"program starts"<<endl;
	cout<<"fork ="<<fork<<endl;
	cout<<"cutlery="<<cutlery<<endl;
	cout<<"address of fork is:"<<&fork<<endl;
	cout<<"address of cutlery is :"<<&cutlery<<endl;
	
	&cutlery=&spoon;
	cout<<"spoons ="<<spoon<<endl;
	cout<<"cutlery ="<<cutlery<<endl;
	cout<<"address of spoon is:"<<&spoon<<endl;
	cout<<"address of cutlery is :"<<&cutlery<<endl;
	return 0;
}