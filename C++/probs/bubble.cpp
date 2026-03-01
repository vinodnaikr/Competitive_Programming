
//int const max=10;
#include<iomanip>
#include<iostream>
#include<conio.h>
using namespace std;


void sort(int b[],int max);
bool swapped;

int main(){
	int i;
    int  max=10;
	int a[max]={0,1,2,3,4,5,6,7,8,9};
	cout<<"programs starts"<<endl;
	cout<<"before sorting"<<endl;
	for(i=0;i<max;i++){
		cout<<setw(6)<<a[i];
	}
	cout<<endl;
	sort(a,max);
	cout<<"After sorting"<<endl;
	for(i=0;i<max;i++){
		cout<<setw(6)<<a[i];
	}
	cout<<endl;
	return 0;
}

void sort(int b[],int max){
	int i,j;
	int temp;
	for(i=0;i<max-1;i++){
		swapped = false;
		for(j=0;j<max-1;j++){
			if(b[j]>b[j+1]){
				temp=b[j];
				b[j]=b[j+1];
				b[j+1]=temp;
				swapped=true;
			}
		}
		if(!swapped){
			break;
		}
	}
}
