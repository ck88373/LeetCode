#include <vector>
#include <unordered_set>
#include <algorithm>
using namespace std;

class Solution {
public:
    int reverse(int x) {
        bool flag=true;
        if(x<0){
            flag=false;
            x=-x;
            if(x<0)return 0;
        }
        long long ans=0;
        while(x){
            int tmp=x%10;
            x=x/10;
            ans=tmp+10*ans;
            
        }
        long long base=1;
        long long INF=(base<<31);
//        printf("%lld",INF);
        if(ans>INF)return 0;
        int ans_=ans;
        return flag?ans_:(-ans_);
    }
};

