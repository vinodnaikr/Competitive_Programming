#include<iostream>
using namespace std;

class DATE_TYPE{
	public:
		int date,month,year;
};

int main(){
	DATE_TYPE date1;
	cout<<"Program starts:"<<endl;
	date1.date=10;
	date1.month=3;
	date1.year=2004;
	cout<<"today's date is:"<<endl;
	cout<<date1.date<<":"<<date1.month<<":"<<date1.year<<endl;
	return 0;
}
