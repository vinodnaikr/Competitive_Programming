// binray search
#include<iostream>
#include<vector>
using namespace std;
int binarySearch(vector<int> &arr,int target){
    int start=0;
    int end=arr.size()-1;
    while(start<=end){
        int mid=start+(end-start)/2;
        if(arr[mid]==target){
            return mid;
        }
        else if(arr[mid]>target){
            end=mid-1;
        }
        else{
            start=mid+1;
        }
    }
    return -1;
}
int main(){
    vector<int> arr={1,2,3,4,5,6,7,8,9};
    int target=5;
    int result=binarySearch(arr,target);
    if(result==-1){
        cout<<"Element not found in the array."<<endl;
    }
    else{
        cout<<"Element found at index: "<<result<<endl;
    }
}
