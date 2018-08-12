#include <vector>
#include <string>
#include <queue>
#include <map>
#include <algorithm>
using namespace std;


class Solution {
public:
    int maxProfit(vector<int>& prices) {
        vector<int> sell;
        int mx=0,ans=0;
        for(int i=prices.size()-1;i>=0;i--){
            if(prices[i]>mx)mx=prices[i];
            sell.push_back(mx);
        }
        for(int i=0;i<prices.size();i++){
            int tmp=sell[prices.size()-1-i]-prices[i];
            if(tmp>ans)ans=tmp;
        }
        return ans;
    }
};
