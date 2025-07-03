class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        if self.head is None:
            return "Linked list is empty"
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.val) + '-->' if itr.next else str(itr.val)
            itr = itr.next
        return llstr
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            itr = itr.next
            count += 1
        return count

    def insert_at_beginning(self, val):
        node = Node(val, self.head)
        self.head = node

    def insert_at_end(self, val):
        if self.head is None:
            self.head = Node(val, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(val, None)

    def insert_at(self, val, index):
        if index < 0 or index > self.get_length():
            raise Exception('Incorrect index')

        if index == 0:
            self.insert_at_beginning(val)
            return


        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = Node(val, itr.next)
                break
            itr = itr.next
            count += 1
    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            itr = itr.next
            count += 1
    def insert_values(self, lst: list):
        for val in lst:
            self.insert_at_end(val)
    def clear_and_insert(self, lst):
        self.head = None
        self.insert_values(lst)
    def __len__(self):
        self.get_length()

    def reverse_in_place(self):
        prev = None
        current = self.head

        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def __reversed__(self):
        values = []
        current = self.head
        while current:
            values.append(current)
            current.next

        for val in reversed(values):
            yield val

    def __iter__(self):
        current = self.head
        while current:
            yield current.val
            current = current.next

    def __getitem__(self, index):
        if index < 0 and index > self.get_length():
            raise Exception('Index is out of range')

        current = self.head
        for _ in range(index):
            current = current.next
        return current.val

    def __setitem__(self, index, value):
        if index < 0 or index >= self.get_length():
            raise IndexError("Index out of range")

        current = self.head
        for _ in range(index):
            current = current.next
        current.val = value







if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_beginning(2)
    ll.insert_at_beginning(3)
    ll.insert_at_end(11)
    ll.insert_values([5,8,11,55,66,77,88])
    print(ll.get_length())
    print(ll)
    ll.clear_and_insert([1,2,3,4,5])
    print(ll)
