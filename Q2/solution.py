# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head
        temp = temp2 = head
        for i in range(n):
            temp = temp.next
        while temp and temp.next:
            temp = temp.next
            temp2 = temp2.next
        if temp is not None:
            temp2.next = temp2.next.next
        else:
            head = head.next
        return head
