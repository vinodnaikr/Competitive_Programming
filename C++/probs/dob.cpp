#include<iostream>
using namespace std;

class DATE_TYPE
{
	private:
		int date,month;
	public:
		int year;
};

int main(){
	DATE_TYPE date1;
	cout<<"Program starts"<<endl;
	date1.year=2004;
	cout<<"Now we are in the year "<<date1.year<<"\t/"<<"AD"<<endl;
	return 0;
}
