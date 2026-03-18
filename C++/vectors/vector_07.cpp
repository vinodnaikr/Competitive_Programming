#include<iostream>
#include<vector>
#include <algorithm>
using namespace std;
// Aggressive cows problem

bool isPossible(vector<int> arr,int N,int C,int maxAllowedDist){
    int cows=1;
    int lastPos=arr[0];
    for(int i=1;i<N;i++){
        if(arr[i]-lastPos>=maxAllowedDist){
            cows++;
            lastPos=arr[i];
        }
        if(cows==C){
            return true;
       
        }
    }
    
    return false;
}

int getDistance(vector<int> arr ,int N,int C){
    sort(arr.begin(),arr.end());
    int st = 0;
    int end = arr[N-1] - arr[0];
    int ans = -1;

    while(st<=end){
        int mid = st+(end-st)/2;
        if(isPossible(arr,N,C,mid)){
            ans=mid;
            st=mid+1;
        }
        else{
            end=mid-1;
        }

    }

    return ans;


}

int main(){
    vector<int> arr = {1,2,8,4,9};
    int n = arr.size();
    int cows=3;
    cout<<getDistance(arr,n,cows)<<endl;
}