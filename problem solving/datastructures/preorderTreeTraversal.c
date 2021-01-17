

/* you only have to complete the function given below.  
node is defined as  

struct node {
    
    int data;
    struct node *left;
    struct node *right;
  
};

*/
void preOrder( struct node *root) {
    struct node *temp=root;
    if(root==NULL)return;
    printf("%d ",root->data);
    preOrder(root->left);
    preOrder(root->right);
}


