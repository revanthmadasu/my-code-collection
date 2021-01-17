

/* you only have to complete the function given below.  
node is defined as  

struct node {
    
    int data;
    struct node *left;
    struct node *right;
  
};

*/
void inOrder( struct node *root) {
    struct node *temp=root;
    if(root==NULL)return;
    inOrder(root->left);
    printf("%d ",root->data);
    inOrder(root->right);

}


