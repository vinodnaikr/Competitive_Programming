// binary search using recursion
#include<iostream>
#include<vector>
using namespace std;

int binarySearch(vector<int> arr,int target,int start,int end){
    int mid=start+(end-start)/2;
    if(arr[mid]<target){
        return binarySearch(arr,target,mid+1,end);
    }
    else if(arr[mid]>target){
        return binarySearch(arr,target,start,mid-1);
    }
    else{
        return mid;
    }

}

int main(){
    vector<int> arr={1,2,3,4,5};
    int target =3;
    int result=binarySearch(arr,target,0,arr.size()-1);
    cout<<"Element found at index: "<<result<<endl;

}