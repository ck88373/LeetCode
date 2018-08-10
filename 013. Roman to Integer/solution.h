#include <vector>
#include <cstring>
#include <map>
#include <algorithm>
using namespace std;

class Solution {
public:
    int romanToInt(string s) {
        string roman="IVXLCDM";
        map<char,int> table;
        int base=1;
        for(int i=0;i<roman.size();i++){
            table[roman[i]]=base;
            if(i%2==0)base*=5;
            else base*=2;
        }
        int ans=0;
        for(int i=0;i<s.size();i++){
            if(i+1>=s.size()||table[s[i]]>=table[s[i+1]])ans+=table[s[i]];
            else{
                ans=ans+table[s[i+1]]-table[s[i]];
                i++;
            }
        }
        return ans;
    }
};
