#include <iostream>
#include <string>
using namespace std;

int main() {
	int tc;
	cin >> tc;
	while(tc--) {
	    int num, count = 0, i = 0;
	    cin >> num;
	    string ballOrder;
	    cin >> ballOrder;
	    while(i<num-1) {
	        if(ballOrder[i]==ballOrder[i+1]) {
	            // Same ball colour, increase count by one and move on
	            i+=1;
	        }
	        else {
	            count+=1;
	            i+=2;
	        }
	    }
	    cout << count << "\n";
	}
	return 0;
}
