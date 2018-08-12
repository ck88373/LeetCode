#include <vector>
#include <string>
#include <queue>
#include <map>
#include <algorithm>
using namespace std;


class Solution {
public:
    bool isPalindrome(string s) {
        int n=0;
        for(int i=0;i<s.size();i++){
            if((s[i]>='a'&& s[i]<='z')||(s[i]>='0'&& s[i]<='9'))s[n++]=s[i];
            else if(s[i]>='A'&& s[i]<='Z')s[n++]=s[i]-'A'+'a';
        }
        for(int i=0;i<n/2;i++){
            if(s[i]!=s[n-1-i])return false;
        }
        return true;
    }
};
