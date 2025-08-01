"""
Problem: 0021. Merge Two Sorted Lists
Link: https://leetcode.com/problems/merge-two-sorted-lists/

Description:
    Merge two sorted linked lists and return it as a new sorted list.

Approach:
    Use a dummy node and iterate through both lists, attaching the smaller node each time.

Time Complexity: O(N + M)
Space Complexity: O(1)
"""

import random
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, val):
        if self.head is None:
            self.head = Node(val, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(val, None)

    def create_list(self, lst):
        for val in lst:
            self.insert_at_end(val)
    def to_node_list(self):
        result = []
        itr = self.head

        while itr.next:
            result.append(itr)
            itr = itr.next


class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution:
    def MergeSortedLists(self, list1, list2):
        dummy = ListNode(-1)
        current = dummy

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next

            current = current.next
        current.next = list1 or list2
        return dummy.next







