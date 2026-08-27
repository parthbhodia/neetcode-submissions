# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head

        while fast and fast.next:
            #check inner cycle loop as they be closing gap in (n-1 iterations)
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        #fast reached first to the end of the loop that is null
        return False