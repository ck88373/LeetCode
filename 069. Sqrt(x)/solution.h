#include <vector>
#include <string>
#include <stack>
#include <map>
#include <algorithm>
using namespace std;

class Solution {
public:
    int mySqrt(int x) {
        int left=1,right=x;
        int mid;
        while(left<=right){
            mid=(left+right)/2;
            if(mid==x/mid&&mid*mid==x)return mid;
            else if(mid>x/mid){
                right=mid-1;
            }
            else left=mid+1;
        }
        return right;
    }
};
