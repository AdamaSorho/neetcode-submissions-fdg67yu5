# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        N = 0
        curr = head

        while curr:
            N += 1
            curr = curr.next

        removeNode = N - n

        if removeNode == 0:
            return head.next

        curr = head
        for i in range(N):
            if i + 1 == removeNode:
                curr.next = curr.next.next
                break

            curr = curr.next

        return head
