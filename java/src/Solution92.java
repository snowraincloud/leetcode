import java.util.List;

/**
 * //TODO
 *
 * @author wangjunhao
 **/


class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }

    public static ListNode listToListNode(int[] list){
        ListNode head = new ListNode();
        ListNode root = head;
        for (int val: list) {
            head.next = new ListNode(val);
            head = head.next;
        }
        return root.next;
    }
}

public class Solution92 {
    public ListNode reverseBetween(ListNode head, int left, int right) {
        ListNode root = new ListNode(-1, head);
        ListNode pre = root;
        for (int i = 0; i < left - 1; i++) {
            pre = pre.next;
        }
        ListNode cur = pre.next;
        ListNode next;
        for (int i = 0; i < right - left; i++) {
            next = cur.next;
            cur.next = next.next;
            next.next = pre.next;
            pre.next = next;
        }
        return root.next;
    }

    public static void main(String[] args) {
        int[] head = {1,2,3};
        int left = 1, right = 3;
        ListNode root = ListNode.listToListNode(head);
        ListNode res = new Solution92().reverseBetween(root, left, right);
        System.out.println("----------");
    }

}
