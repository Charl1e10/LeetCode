# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        list1Answer = ""
        list2Answer = ""
        while l1 is not None:
            list1Answer = str(l1.val) + list1Answer
            l1 = l1.next
        while l2 is not None:
            list2Answer = str(l2.val) + list2Answer
            l2 = l2.next
        
        head = ListNode()
        answer = head
        overallAnswer = int(list1Answer) + int(list2Answer)
        StrAnswer = str(overallAnswer)[::-1]
        for i in range (len(StrAnswer)):
            a = StrAnswer[i]
            newNode = ListNode(int(a))
            answer.next = newNode
            answer = answer.next

        return head.next