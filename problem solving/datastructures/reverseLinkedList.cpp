

// Complete the reverse function below.

/*
 * For your reference:
 *
 * SinglyLinkedListNode {
 *     int data;
 *     SinglyLinkedListNode* next;
 * };
 *
 */

SinglyLinkedListNode* reverse(SinglyLinkedListNode* head) {
    SinglyLinkedListNode* reverseHead, * temp,*newNode;
    int stack[1000];
    int top=0;
    while(head!=NULL)
    {
        stack[top]=head->data;
        head=head->next;
        top++;
    }
    reverseHead=(SinglyLinkedListNode*)malloc(sizeof(SinglyLinkedListNode));
    temp=reverseHead;
    while(top-1>=0)
    {
        newNode=(SinglyLinkedListNode*)malloc(sizeof(SinglyLinkedListNode));
        newNode->next=NULL;
        newNode->data=stack[top-1];
        --top;
        temp->next=newNode;
        temp=temp->next;
    }
    return reverseHead->next;
}


