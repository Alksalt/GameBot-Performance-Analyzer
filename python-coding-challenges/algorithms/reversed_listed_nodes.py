class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f'The value is {self.val}'


def reverse_nodes(head: int):
    prev = None
    current = head
    while current is not None:
        next = current.next
        current.next = prev
        prev = current
        current = next
    return prev

def print_list(head: int):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

nodes = [ListNode(i) for i in range(1,11)]
for i in range(len(nodes)-1):
    nodes[i].next = nodes[i + 1]
new_head = reverse_nodes(nodes[0])
print_list(new_head)


