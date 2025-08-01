#
"""
Problem: 0002. Add Two Numbers
Link: https://leetcode.com/problems/add-two-numbers/

Description: Add two numbers represented by linked lists, where each node contains a single digit. The digits are stored in reverse order.
Approach: Traverse both lists, sum digits with carry, build result list.
Time Complexity: O(max(N, M))
Space Complexity: O(max(N, M))
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode()
        itr_dummy = dummy
        carry = 0

        while l1 or l2:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            itr_dummy.next = ListNode(val1 + val2 + carry)
            if itr_dummy.next.val > 9:
                carry = 1
                itr_dummy.next.val = itr_dummy.next.val % 10
            else:
                carry = 0
            l1 = l1.next
            l2 = l2.next
            itr_dummy = itr_dummy.next

        if carry:
            itr_dummy.next = ListNode(1, None)

        return dummy.next


# Helper to convert list to linked list
def list_to_linked(lst):
    dummy = ListNode()
    current = dummy
    for num in lst:
        current.next = ListNode(num)
        current = current.next
    return dummy.next

# Helper to convert linked list to list
def linked_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

# === Test case ===
l1 = list_to_linked([2, 4, 3])  # Represents the number 342
l2 = list_to_linked([5, 6, 4])  # Represents the number 465

sol = Solution()
print(linked_to_list(sol.addTwoNumbers(l1,l2)))
