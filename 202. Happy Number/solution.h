#include <vector>
#include <map>
#include <algorithm>
using namespace std;

class Solution {
public:
    int trans(int n){
        int ans=0;
        while(n!=0){
            int tmp=n%10;
            ans+=(tmp*tmp);
            n=n/10;
        }
        return ans;
    }
    bool isHappy(int n) {
        map<int,int> record;
        while(n!=1){
            if(record.count(n))return false;
            else{
                record[n]=1;
                n=trans(n);
            }
        }
        return true;
    }
};
