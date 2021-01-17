

/* 
The structure of the node is

typedef struct node {

	int freq;
    char data;
    node * left;
    node * right;
    
} node;

*/
void inorder(node*);

void decode_huff(node * root, string s) {
    int i=0;
    char c;
    node *temp;
    while(s[i]!='\0')
    {
        temp=root;
        while(true)
        {
            c=s[i];
           // printf("%d",i);
            if(c=='0')
            {
                temp=temp->left;
                if(temp->data=='\0')
                {
                    //printf("%d",i);
                    ++i;
                    continue;
                }
                else
                {
                    printf("%c",temp->data);
                    ++i;
                    break;
                }
            }
            if(c=='1')
            {
                temp=temp->right;
                if(temp->data=='\0')
                {
                    //printf("%d",i);
                    ++i;
                    continue;
                }
                else
                {
                    printf("%c",temp->data);
                    ++i;
                    break;
                }
            }
        }

    }
}

void inorder(node *root)
{
    if(root==NULL)return;
    inorder(root->left);
    printf("%c",root->data);
    inorder(root->right);
}


