#include <vector>
#include <map>
#include <algorithm>
using namespace std;

class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int sum=0,ans=nums[0];
        for(int i=0;i<nums.size();i++){
            sum+=nums[i];
            ans=max(ans,sum);
            sum=max(0,sum);
        }
        return ans;
    }
};
