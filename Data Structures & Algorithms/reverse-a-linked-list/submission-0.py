# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev, curr = None, head

        while curr : 
            # we know from the fact that this list has a node and a pointer self.next
            temp = curr.next

            #this is where you reverse the pointer of current.next node to the previous node
            curr.next = prev
            #moving prev forward now that the current.next is pointing to previous element i e we reversed the node
            prev = curr
            #we are moving forward hence we stored the next value in temp
            curr = temp 
        #this returns the whole list behind it
        return prev