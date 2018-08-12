#include <vector>
#include <string>
#include <queue>
#include <map>
#include <algorithm>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
    void Mirrior(TreeNode* &s, TreeNode* &t){
        if(s==NULL)return;
        if(s->right!=NULL)t->left=new TreeNode(s->right->val);
        if(s->left!=NULL)t->right=new TreeNode(s->left->val);
        Mirrior(s->right, t->left);
        Mirrior(s->left,t->right);
    }
    bool TreeComp(TreeNode* &a, TreeNode* &b){
        if(a==NULL||b==NULL){
            if(a==NULL&&b==NULL)return true;
            else return false;
        }
        else if(a->val!=b->val)return false;
        else{
            return TreeComp(a->left, b->left)&&TreeComp(a->right, b->right);
        }
        
    }
    bool isSymmetric(TreeNode* root) {
        TreeNode *mirrior;
        if(root!=NULL)mirrior=new TreeNode(root->val);
        else mirrior=NULL;
        Mirrior(root, mirrior);
        return TreeComp(root, mirrior);
    }
};
