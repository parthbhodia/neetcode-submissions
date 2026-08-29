# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        


        # we need dummy to make the node stop right before the deletion of the required node
        dummy = ListNode(0, head)
        left = dummy
        right = head 

        #now let's move the right node to fill the gap

        while n > 0 and right:

            right = right.next
            n -= 1

        # now we have the gap between left and right node

        while right:
            #keep movingg till we reach the end
            left = left.next
            right = right.next

        
        # delete the node

        left.next = left.next.next

        return dummy.next


     
