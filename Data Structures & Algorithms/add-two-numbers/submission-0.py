# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        

        dummy = ListNode()
        curr = dummy


        carry = 0

        while l1 or l2 or carry:

            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0

            val = v1 + v2 + carry #find the sum
            carry = val // 10 # get the carry value that is first digit here
            val = val % 10 # leave the remainder digits to be added
            
            curr.next = ListNode(val) # to add a new value directly you need to use ListNode cannot add a integer directly

            curr = curr.next # move the new pointer to the next value we just added 

            # update the pointers

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        return dummy.next
            