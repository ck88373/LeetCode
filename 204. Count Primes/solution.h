#include <vector>
#include <unordered_set>
#include <algorithm>
using namespace std;

class Solution {
public:
    int countPrimes(int n) {
        int count=0;
        unordered_set<int> record;
        if(n<=2)return 0;
        for(int i=2;i*i<n;i++){
            if(record.find(i)==record.end()){
                for(int j=i+i;j<n;){
                    record.insert(j);
                    j+=i;
                }
            }
            
        }
        for(int i=2;i<n;i++){
            if(record.find(i)==record.end())count++;
        }
        return count;
    }
};
