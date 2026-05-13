# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        reminder = 0
        result = head = ListNode()
        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            curDigit = val1 + val2 + reminder
            if curDigit >= 10:
                reminder = curDigit // 10
                curDigit = curDigit % 10
            else:
                reminder = 0
            result.next = ListNode(curDigit)
            result = result.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if reminder != 0:
            result.next = ListNode(reminder)
        return head.next
            
            
        