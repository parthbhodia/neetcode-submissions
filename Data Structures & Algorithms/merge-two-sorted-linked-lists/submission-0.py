# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        

        #let's create a dummy node 

        dummy = ListNode()
        tail = dummy

        #both has to be non empty for it to work 
        while list1 and list2:

            if list1.val < list2.val :

                tail.next = list1

                list1 = list1.next

            else: 

                tail.next = list2
                list2 = list2.next

            # to move the pointer from current posisiton since we added 1 to the tail so we need to make our new node as 1 now by updating the pointer    
            tail = tail.next

        if list1:
            tail.next = list1

        elif list2:
            tail.next = list2
        #caant return dummy since dummy  has 0 init value
        return dummy.next



