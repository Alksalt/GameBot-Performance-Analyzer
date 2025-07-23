import random
from collections import deque

class RandomizedSet:

    def __init__(self):
        self.lst = []
        self.d = {}

    def insert(self, val: int) -> bool:
        if val in self.d:
            return False
        self.lst.append(val)
        self.d[val] = len(self.lst) - 1
        return True

    def remove(self, val: int) -> bool:
        index = self.d.get(val, -1)
        if index == -1:
            return False
        else:
            last_val = self.lst[-1]
            self.lst[index], self.lst[-1] = last_val, self.lst[index]
            self.lst.pop()
            self.d[last_val] = index
            self.d.pop(val)
            return True
    def getRandom(self) -> int:
        return random.choice(self.lst)

class RandomizedCollection:

    def __init__(self):
        self.lst = []
        self.d = {}

    def insert(self, val: int) -> bool:
        self.lst.append(val)
        if val not in self.d:
            self.d[val] = deque([len(self.lst) - 1])
            return True
        else:
            self.d[val].append(len(self.lst) - 1)
            return False

    def remove(self, val: int) -> bool:
        if val not in self.d or not self.d[val]:
            return False
        index = self.d[val].popleft()
        last_val = self.lst[-1]

        if index != len(self.lst) - 1:

            self.lst[index] = last_val

            self.d[last_val].remove(len(self.lst) - 1)
            self.d[last_val].append(index)

        self.lst.pop()
        if not self.d[val]:
            del self.d[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.lst)
# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()