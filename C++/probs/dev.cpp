#include<iostream>
#include<conio.h>
using namespace std;

enum PLANETS{ ravi,chandra,magal,budh,guru,shukra,shani
};

int main(){
	PLANETS p1 ,p2;
	p1=ravi;
	p2=chandra; 
	p2=PLANETS(4);
	cout<<p1<< endl;
	cout<<"p2 is"<<p2<<endl;
	p2=(PLANETS) 3;
	cout<<"p2 is"<<p2<<endl;
	getch();
	return 0;
	
}
