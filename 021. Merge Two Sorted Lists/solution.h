#include <vector>
#include <string>
#include <stack>
#include <map>
#include <algorithm>
using namespace std;

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */


struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};


class Solution {
public:
//    ListNode* ListCopy(ListNode* x){
//        if(x==NULL)return NULL;
//        ListNode* y=new ListNode(*x);
//        ListNode* cur=y;
//        while(x->next!=NULL){
//            x=x->next;
//            cur->next = new ListNode(*x);
//            cur=cur->next;
//        }
//        return y;
//    }
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        ListNode *head,*p;
        head= new ListNode(0);
        p=head;
        while(l1!=NULL||l2!=NULL){
            if(l2==NULL||(l1!=NULL&&l1->val<l2->val)){
                p->next=new ListNode(l1->val);
                l1=l1->next;
            }
            else{
                p->next=new ListNode(l2->val);
                l2=l2->next;
            }
            p=p->next;
        }
        return head->next;
    }
};

