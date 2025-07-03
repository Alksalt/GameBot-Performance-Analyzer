# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head):
        itr = head
        while itr and itr.next:
            if itr.val == itr.next.val:
                itr.next = itr.next.next
            else:
                itr = itr.next

        return head

    ar = [1,1,2,3,3]
    b = [1,2]

