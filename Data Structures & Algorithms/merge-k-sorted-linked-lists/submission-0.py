# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None
        
        return self.divide(lists, 0, len(lists) - 1)

    
    def divide(self, lists: List[Optional[ListNode]], l: int, r: int) -> Optional[ListNode]:
        if l > r:
            return None
        
        if l == r:
            return lists[l]

        m = l + ((r - l) // 2)
        left = self.divide(lists, l, m)
        right = self.divide(lists, m + 1, r)

        return self.conquer(left, right)

    def conquer(self, l1: Optional[ListNode], 
                l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            
            curr = curr.next
        
        curr.next = l1 or l2

        return dummy.next
        