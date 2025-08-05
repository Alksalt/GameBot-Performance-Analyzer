"""
Problem: 0141. Linked List Cycle
Link: https://leetcode.com/problems/linked-list-cycle/

Description:
    Given head, the head of a linked list, determine if the linked list has a cycle in it.

Approach:
    Use two pointers (slow and fast). If they meet, there is a cycle.

Time Complexity: O(N)
Space Complexity: O(1)
"""


from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


if __name__ == "__main__":
    # Example 1: Cycle exists
    nodes = [ListNode(i) for i in range(4)]
    for i in range(3):
        nodes[i].next = nodes[i+1]
    nodes[3].next = nodes[1]  # cycle at node 1
    head1 = nodes[0]
    print(Solution().hasCycle(head1))  # Output: True

    # Example 2: No cycle
    nodes2 = [ListNode(i) for i in range(3)]
    for i in range(2):
        nodes2[i].next = nodes2[i+1]
    head2 = nodes2[0]
    print(Solution().hasCycle(head2))  # Output: False
        