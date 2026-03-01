#include<iostream>
using namespace std;
int main(){
    int n;
    cin>>n;
    // int num=1;
    for(int i=1;i<=n;i++){
        for(int j=n;j>=i;j--){
            cout<<i<<" ";
            // num++;

        }
        cout<<endl;
    }
    
//  cout<<endl;
}