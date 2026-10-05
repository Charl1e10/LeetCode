# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return False
        point1 = head
        point2 = head.next 
        while point1 != point2:
            if point2 is None or point2.next is None:
                return False
            point1 = point1.next
            point2 = point2.next.next
        
        return True
        

        