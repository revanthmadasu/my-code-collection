

/* you only have to complete the function given below.  
node is defined as  

struct node {
    
    int data;
    struct node *left;
    struct node *right;
  
};

*/
void inorder(struct node*);
struct node* insert( struct node* root, int data ) {
		struct node* temp=(struct node*)malloc(sizeof(struct node));
        temp->data=data;
        temp->left=NULL;
        temp->right=NULL;
        struct node* temp1=root;
        if(temp1==NULL)root=temp;
        else
        while(temp1!=NULL)
        {
            if(temp1->data>data)
            {
                if(temp1->left==NULL)
                {
                    temp1->left=temp;
                    break;
                }
                else
                temp1=temp1->left;
            }
            else{
                    if(temp1->right==NULL)
                    {
                        temp1->right=temp;
                        break;
                    }
                    else
                    temp1=temp1->right;
            } 
        }
        //inorder(root);
        return root;
}
void inorder(struct node* root)
{
    printf("Hey");
    if(root==NULL)return;
    inorder(root->left);
    printf("%d ",root->data);
    inorder(root->right);
}

