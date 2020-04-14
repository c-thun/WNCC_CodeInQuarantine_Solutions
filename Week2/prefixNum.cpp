#include<bits/stdc++.h>
using namespace std;

void exec() {
	long long x,y,a,f=0,lim,curr;
	lim=pow(10,18);
	cin>>x>>y;
	for(long long i=1;!f;i*=10) {
	    a = i*x;
		if(a>lim/10) f=1;
        curr=a%y;
        if(curr==0)  {
		    cout<<a<<endl;
		    return;
		}
		if(y-curr < i) {
			a=a+y-curr;
			if(a>0 and a<=lim) {
				cout<<a<<endl;
				return;
			}
		} 
	}
	cout<<"-1\n";
	return;
}

int main() {
    int t;
    cin>>t;
    while(t--) {
        exec();
    }
}
