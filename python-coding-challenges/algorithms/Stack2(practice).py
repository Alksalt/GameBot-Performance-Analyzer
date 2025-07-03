class Stack:
    def __init__(self):
        self.items = []

    def push(self, *item):
        for i in item:

            self.items.append(i)
        print(f'{item} has been pushed')

    def is_Empty(self):
        return len(self.items) == 0

    def pop(self):
        if self.is_Empty():
            raise IndexError("Pop from empty stack")
        else:
            self.items.pop()
    def top(self):
        if self.is_Empty():
            return None
        return self.items[-1]

    def __str__(self):
        return "Stack: " + str(self.items)

    def __iter__(self):
        return iter(self.items)

class GetMini:
    def __init__(self, lst):
        self.mini_items = sorted(lst.items, reverse=True)

    def getMini(self):
        if self.mini_items:
            return self.mini_items[-1]

    def push(self, *item):
        mini = self.getMini()
        pushed = False
        for i in item:
            if i < mini:
                self.mini_items.append(i)
                pushed = True

        return 'was/were pushed' if pushed else 'was/were not pushed'

    def top(self):
        return self.mini_items[0]

    def pop(self):
        return self.mini_items.pop(0)

    def __str__(self):
        return "Stack: " + str(self.mini_items)


stack = Stack()

stack.push(1,2,3,0,-1)

mini_stack = GetMini(stack)
print(mini_stack.getMini())