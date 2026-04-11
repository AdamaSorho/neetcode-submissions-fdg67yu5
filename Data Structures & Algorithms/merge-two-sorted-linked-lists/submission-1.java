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
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        if (list1 == null && list2 == null) return null;
        
        ListNode head = new ListNode(0);
        ListNode node = head;
        ListNode last = null;

        while (list1 != null && list2 != null) {
            if (list1.val < list2.val) {
                node.val = list1.val;
                node.next = new ListNode(0);
                last = node;
                node = node.next;
                list1 = list1.next;
            }
            else {
                node.val = list2.val;
                node.next = new ListNode(0);
                last = node;
                node = node.next;
                list2 = list2.next;
            }
        }

        while(list1 != null) {
            node.val = list1.val;
            node.next = new ListNode(0);
            last = node;
            node = node.next;
            list1 = list1.next;
        }

        while(list2 != null) {
            node.val = list2.val;
            node.next = new ListNode(0);
            last = node;
            node = node.next;
            list2 = list2.next;
        }

        last.next = null;

        return head;
    }
}