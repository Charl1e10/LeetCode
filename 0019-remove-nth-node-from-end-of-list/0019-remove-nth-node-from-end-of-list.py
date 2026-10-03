# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:
        previous = head
        answer = head
        length = 1
        while answer.next is not None:
            answer = answer.next
            length += 1

        if length < 3:
            if n == 2:
                head = head.next
            elif length == 1:
                return
            else:
                head.next = None
        else:
            if n == length:
                head = head.next
            else:
                for i in range((length - n) - 1):
                    previous = previous.next

                before = previous
                previous = previous.next
                previous = previous.next

                before.next = previous
        
        return head
