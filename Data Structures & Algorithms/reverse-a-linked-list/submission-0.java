/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public ListNode reverseList(ListNode head) {
        if (head == null) return null;

        Stack<ListNode> stack = new Stack<>();
        
        while(head != null) {
            stack.push(head);
            head = head.next;
        }

        head = stack.pop();
        ListNode node = head;
        while(!stack.isEmpty()) {
            node.next = stack.pop();
            node = node.next;
        }
        node.next = null;

        return head;
    }
}
