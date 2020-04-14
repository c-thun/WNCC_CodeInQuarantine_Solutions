#include <bits/stdc++.h>
using namespace std;

int main() {
    int tc;
    cin >> tc;
    for(int i=0;i<tc;i++) {
        long long int x, y;
        cin>>x>>y;
        long long int nums=1, ans=-1; int flag=0;
        while(true) {
            long long int rem = (y-(x%y))%y;
            if(rem<nums) {
                ans = x+rem;
            }
            if(ans<1e18 and (ans%y)==0) {
                break;
            }
            if(x>1e18) {
                flag = 1;
                break;
            }
            else {
                x*=10;
                nums*=10;
            }
        }
        if(ans<=1e18 and flag==0) 
            cout<<ans<<"\n";
        else 
            cout<<-1<<"\n";
    }
  return 0;
}
