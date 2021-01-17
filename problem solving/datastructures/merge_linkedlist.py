

# Complete the mergeLists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insertItem(llist, item):
    # if llist.tail:
    #     if llist.tail.data != item:
    #         llist.insert_node(item)
    #         print(item)        
    # else:
    llist.insert_node(item)            
    print(item)
def mergeLists(head1, head2):
    mergedList = SinglyLinkedList()
    while head1 or head2:
        print('called', head1 and head1.data, head2 and head2.data)
        if head1 and head2:
            if head1.data < head2.data:
                insertItem(mergedList, head1.data)
                head1 = head1.next
            else:
                insertItem(mergedList, head2.data)
                head2 = head2.next
        elif head1:
            insertItem(mergedList, head1.data)
            head1 = head1.next            
        else:
            insertItem(mergedList, head2.data)
            head2 = head2.next            
    return mergedList.head
