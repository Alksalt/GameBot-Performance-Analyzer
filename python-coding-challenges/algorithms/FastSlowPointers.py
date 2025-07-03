class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)

class SlowFastPointer:
    def __init__(self, head: ListNode):

        self.head = head

    def find_cycle(self):
        slow = fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return slow

        return None
    def bool_find_cycle(self):
        return True if self.find_cycle() else False
    def find_middle(self):
        if not self.bool_find_cycle():

            slow = fast = self.head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow
        else:
            return None
    def start_cycle(self):
        meet = self.find_cycle()
        if not meet:
            print('not a cycle')
            return None

        ptr1 = meet
        ptr2 = self.head
        while ptr1 != ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        return ptr1

node1 = ListNode(1)
node2 = ListNode(5)
node3 = ListNode(3)
node4 = ListNode(9)
node5 = ListNode(11)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node2

nodes = [ListNode(i) for i in range(1,6)]
for i in range(len(nodes) - 1):
    nodes[i].next = nodes[i + 1]

slow_fast = SlowFastPointer(node1)
print(slow_fast.find_cycle())
print(slow_fast.start_cycle())