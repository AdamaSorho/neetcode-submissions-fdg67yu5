# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        str1, str2 = '', ''

        curr = l1
        while curr:
            str1 = str(curr.val) + str1
            curr = curr.next

        curr = l2
        while curr:
            str2 = str(curr.val) + str2
            curr = curr.next

        strs = str(int(str1) + int(str2))
        head = ListNode(int(strs[-1]))
        curr = head

        for i in range (len(strs) - 2, -1, -1):
            node = ListNode(int(strs[i]))
            curr.next = node
            curr = curr.next

        return head
        