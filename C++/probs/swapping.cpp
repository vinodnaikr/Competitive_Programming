#include<iostream>
using namespace std;

void swap(int &a ,int & b);

int main(){
	int i=10,j=20;
	cout<<"Program starts"<<endl;
	cout<<"initial values"<<endl;
	cout<<"i="<<i<<"j="<<j<<endl;
	swap(i,j);
	cout<<"after swapping"<<endl;
	cout<<"i="<<i<<"j="<<j<<endl;
	return 0;
}

void swap(int &a ,int &b){
	int temp;
	temp=a;
	a=b;
	b=temp;
}
