#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int main(){
	int arr[5];
	cout<<"Enter 5 integers:"<<endl;
	
	for(int i=0;i<5;i++){
		cin>>arr[i];
	}
	
	int greatest=arr[0];
	
	for(int i=1;i<5;i++){
		if(arr[i]>greatest){
			greatest=arr[i];
		}
	}
	
	cout<<"The Greatest of 5 numbers is:"<<greatest<<endl;   
}
