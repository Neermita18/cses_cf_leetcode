#include <iostream>
#include <bits/stdc++.h>
#include <string.h>
using namespace std;

int main()
{
    
    long int n,m;
   scanf("%li %li", &n, &m);
    //cout<<""<<endl;
    std::string s;
    cin>>s;
    //cout<<""<<endl;
    long int a,b;
    string st;
    long int i=1;
    while(i<=m){
        
        scanf("%li %li", &a, &b);
       
        string substring = s.substr(a-1,b-a+1);
        //cout<<substring<<endl;
    string ret= s.erase(a-1,b-a+1);
    string fin=ret.append(substring);
        s=fin;
        i++;
    }
    
cout<<s<<endl;   
}

