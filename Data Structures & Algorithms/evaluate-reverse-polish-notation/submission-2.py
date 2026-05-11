class DoubleLinkedList:
    def __init__(self, val: int, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        n = len(tokens)
        if n == 1:
            return int(tokens[0])

        head = DoubleLinkedList(tokens[0])
        curr = head

        for i in range(1, n):
            curr.next = DoubleLinkedList(tokens[i], prev=curr)
            curr = curr.next

        print(head.val, curr.val)

        while head is not None:
            if head.val in "+-*/":
                l = int(head.prev.prev.val)
                r = int(head.prev.val)

                if head.val == '+':
                    op = l + r
                elif head.val == '-':
                    op = l - r
                elif head.val == '*':
                    op = l * r
                else:
                    op = int(l / r)
                
                head.val = str(op)
                head.prev = head.prev.prev.prev

                if head.prev is not None:
                    head = head.prev

            ans = int(head.val)
            head = head.next

        return ans
