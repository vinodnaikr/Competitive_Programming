#include<iostream>
using namespace std;

class TIME{
	private:
		int hr,min,sec;
	public:
		void set_time();
		void show_time();
		int is_later(TIME *tx);
};

void TIME::set_time()
{
	cout<<"Enter hours:";
	cin>>hr;
	cout<<"Enter minutes:";
	cin>>min;
	cout<<"Enter seconds:";
	cin>>sec;
}

void TIME::show_time()
{
	cout<<endl<<"The set time is:"<<"\n";
	cout<<hr<<":"<<min<<":"<<sec;
}

int TIME::is_later(TIME*tx)
{
	int answer=0;
	long s1,s2;
	
	s1=((hr*60)+min)*60+sec;
	s2=(((*tx).hr*60)+tx->min)*60+(*tx).sec;
	if(s2>s1)
	{
		answer=1;
	}
	return answer;
}
int main(){
	TIME t1,t2;
	t1.set_time();
	t1.show_time();
	t2.set_time();
	t2.show_time();
	
	cout<<endl<<"Time t2 is later than t1?";
	if(t1.is_later(&t2))
	{
		cout<<"yes";
	}
	else
	{
		cout<<"No";
	}
	return 0;
}
