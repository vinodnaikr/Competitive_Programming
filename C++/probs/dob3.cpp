#include<iostream>
using namespace std;

class DATE{
	private:
		int date,month,year;
	public:
		void set_date(int d1,int m1,int y1);
		void show_date();
};

int main(){
	DATE d1;
	cout<<"Program starts:"<<endl;
	d1.set_date(10,3,2004);
	d1.show_date();
	return 0;
}

void DATE::set_date(int d1,int m1,int y1)
{
	date=d1;
	month=m1;
	year=y1;
}

void DATE::show_date()
{
	cout<<"The date is:"<<endl;
	cout<<date<<":"<<month<<":"<<year<<endl;
}
