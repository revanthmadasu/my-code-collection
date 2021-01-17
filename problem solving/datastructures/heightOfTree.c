

/* you only have to complete the function given below.  
node is defined as  

struct node {
    
    int data;
    struct node *left;
    struct node *right;
 
};

*/
int heightRecursion(struct node*,int);
int getHeight(struct node* root) {
    // Write your code here
    return heightRecursion(root,-1);
}
int heightRecursion(struct node* root,int height)
{
    int leftHeight,rightHeight;
    if(root==NULL)return height;
    ++height;
    leftHeight=heightRecursion(root->left,height);
    rightHeight=heightRecursion(root->right,height);
    if(leftHeight>rightHeight)return leftHeight;
    return rightHeight;
}

