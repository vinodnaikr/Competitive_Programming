#include<iostream>
#include<vector>
using namespace std;

bool isValid(vector<int> arr,int n,int m,int maximumAllowedPages){
    int stu = 1;
    int pages = 0;

    for(int i=0;i<n;i++){
        if(arr[i]>maximumAllowedPages){
            return false;
        }
        if(pages + arr[i] <= maximumAllowedPages){
            pages += arr[i];
        }
        else{
            stu++;
            pages = arr[i];
        }
    }
    return stu > m ? false : true;
}

int allocateBooks(vector<int> arr,int n,int m){

    if(m>n){
        return -1;
    }
    
    int sum=0;
    for(int i=0;i<n;i++){
        sum+=arr[i];
    }

    int st=0,end=sum; // range of possible answer

    while(st<=end){
        int mid = st+(end-st)/2;
        int ans = -1;

        if(isValid(arr,n,m,mid)){  //left
            ans = mid;             
            end = mid-1;
        }
        else{ //right
            st = mid+1;
        }

    }

}

int main(){
    vector<int> arr ={2,1,3,4};
    int n = 4,m = 5;
    cout<<allocateBooks(arr,n,m)<<endl;

    return 0;
}