# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, cu = None, head

        while cu:
            temp = cu.next
            cu.next = prev
            prev = cu
            cu = temp
            
        return prev



        