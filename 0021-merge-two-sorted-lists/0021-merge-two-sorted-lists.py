# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        head = ListNode()
        answer = head
        while list1 is not None and list2 is not None: 
            if list1.val <= list2.val:
                answer.next = list1
                list1 = list1.next
                answer = answer.next
            else:
                answer.next = list2
                list2 = list2.next
                answer = answer.next

        if list1 is not None:
            while list1 is not None:
                answer.next = list1
                list1 = list1.next
                answer = answer.next
        
        else:
            while list2 is not None:
                answer.next = list2
                list2 = list2.next
                answer = answer.next
        
        return head.next