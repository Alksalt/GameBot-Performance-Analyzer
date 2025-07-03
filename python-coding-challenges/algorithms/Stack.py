class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
        print(f'{item} has been pushed')

    def is_Empty(self):
        return len(self.items) == 0

    def pop(self):
        if self.is_Empty():
            raise IndexError("Pop from empty stack")
        else:
            self.items.pop()
    def peek(self):
        if self.is_Empty():
            return None
        return self.items[-1]

    def __len__(self):
        return len(self.items)

    def __str__(self):
        return "Stack: " + str(self.items)

def is_closed(exp: str) -> bool:
    stack = Stack()
    mapping = {')': '(', ']': '[', '}': '{'}
    for char in exp:
        if char in mapping.values():
            stack.push(char)
            print(f'adding {char} to stack')
        elif char in mapping:
            if stack.is_Empty() or stack.pop() != mapping[char]:
                return False
    return stack.is_Empty()

