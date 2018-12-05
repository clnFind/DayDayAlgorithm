# -*- coding: utf-8 -*-


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def addTwoNumbers(self, l1, l2):
        """
        输入：(2 -> 4 ) + (5 -> 6 -> 4)
        输出：7 -> 0 -> 5
        原因：42 + 465 = 507
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # 同时遍历两个链表，将对应位的数子相加。如果有进位就记录下来
        head = ListNode((l1.val + l2.val) % 10)
        current = head

        # 进位
        carry = (l1.val + l2.val) // 10
        while l1.next or l2.next:
            num1 = 0
            num2 = 0
            if l1.next:
                l1 = l1.next
                num1 = l1.val
            if l2.next:
                l2 = l2.next
                num2 = l2.val
            current.next = ListNode((num1 + num2 + carry) % 10)
            carry = (num1 + num2 + carry) // 10
            current = current.next
        if carry != 0:
            current.next = ListNode(carry)
        return head


if __name__ == '__main__':

    l1 = ListNode(2)
    node2 = ListNode(4)
    # node3 = ListNode(3)
    l1.next = node2
    # node2.next = node3
    print(l1.val, l1.next.val)

    l2 = ListNode(5)
    node5 = ListNode(6)
    node6 = ListNode(4)
    l2.next = node5
    node5.next = node6
    print(l2.val, l2.next.val, l2.next.next.val)

    result = Solution().addTwoNumbers(l1, l2)
    print(result.val, result.next.val, result.next.next.val)
