#include <iostream>
#include <algorithm>
#define max(a,b) ((a)>(b)?(a):(b))
using namespace std;

int main() {
	int tc;
	cin >> tc;
	for(int i=0;i<tc;i++) {
	    // Input the number array
	    int num;
	    int flag = 0;
	    cin >> num;
	    int arr[num];
	    for(int j=0;j<num;j++) {
	        cin >> arr[j];
	    }
      
      // The following commented code is Bubble Sort. It is O(n^2) and will cause TLE.
      // for(int p=0;p<num-1;p++) {
      //     for(int q=0;q<num-p-1;q++) {
      //         if(arr[q+1]<arr[q]) {
      //             int tmp = arr[q];
      //             arr[q] = arr[q+1];
      //             arr[q+1] = tmp;
      //         }
      //     }
      // }
        
      // The sort() command uses a modified QuickSort Algorithm which is O(nlogn)  
      sort(arr, arr+num);
      
      int diff[num];
      diff[0]=arr[1]-arr[0];
      diff[num-1]=arr[num-1]-arr[num-2];
      for(int r=1;r<num-1;r++) {
          diff[r]=max(arr[r+1]-arr[r], arr[r]-arr[r-1]);
      }
      for(int s=0;s<num;s++) {
          if(diff[s]>1 || diff[s]<-1) {
              flag = 1;
          }
      }
      if(flag == 0) 
          cout<<"YES \n";
      else
          cout<<"NO \n";
	}
	return 0;
}
