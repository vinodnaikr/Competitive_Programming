#include<iostream>
#include<vector>
using namespace std;
// painters partition problem

bool isPossible(vector<int> arr,int n,int m,int maxAllowedTime){
    int painterCount=1;
    int timeSum=0;

    for(int i=0;i<n;i++){
        if(timeSum+arr[i]<=maxAllowedTime){
            timeSum+=arr[i];
        }
        else{
            painterCount++;
            if(painterCount>m || arr[i]>maxAllowedTime){
                return false;
            }
            timeSum=arr[i];
        }
    }
    return true;

}


int minTimeToPaint(vector<int> arr,int n,int m){
    int sum = 0;
    int maxValue = INT8_MIN;
    
    for(int i=0;i<n;i++){
        sum+=arr[i];
        maxValue=max(maxValue,arr[i]);
    }

    int st=maxValue;
    int end=sum;
    int ans=-1;

    while(st<=end){
        int mid=st+(end-st)/2;
        
        if(isPossible(arr,n,m,mid)){
            ans=mid;
            end=mid-1;

        }
        else{
            st=mid+1;
        }
        

    }
}

int main(){
    vector<int> arr =  {40,30,10,20};
    int n = 4;
    int m = 2;
    cout<<minTimeToPaint(arr,n,m)<<endl;
    


}