#include <iostream>
#include <algorithm>
#include <bits/stdc++.h>
#include <vector>
using namespace std;


void missing(long long int n, vector <long long int> a)
{
    //int x[n-1]={0};
    sort(a.begin(), a.end());
    // for(auto i:a)
    // {
    //     cout<< i<< endl;
    // }
    
    for(auto &i:a){
        if(a[0]==2 && n==2){
            cout<<"1";
            break;
        }
        else if(a[i]!=i+1 && a[i]!=2){
            cout<< i+1;
            break;

        }
        
        else{
            
            continue;
        }
    }

}
int main()
{
    long long int n;
    cin >> n;
    long long int s;
    vector <long long int> a;
    for( int i=0; i<n-1; i++)
    {
        
        cin >> s;
        a.push_back(s);

    }

    // for( auto i:a)
    // {
    //     cout<<i<<endl;
    // }
    missing(n,a);

}