#include <vector>
#include <string>
#include <stack>
#include <map>
#include <algorithm>
using namespace std;

class Solution {
public:
    
    int strStr(string haystack, string needle) {
        int idx=0,a=0,b=0,len=0;
        while(1){
            if(b==needle.size())return idx;
            if(a==haystack.size())return -1;
            while(haystack[a]==needle[b]){
                a++;b++;len++;
                if(b==needle.size())return idx;
            }
            idx++;
            a=a-len+1;
            b=0;len=0;
        }
    }
};
