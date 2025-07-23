import random
from collections import deque
class RandomizedSet2:

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

class RandomizedSet:

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
        index = self.d.get(val, deque()).popleft()
        if not index:
            return False
        else:
            last_val = self.lst[-1]
            self.lst[index], self.lst[-1] = last_val, self.lst[index]
            self.lst.pop()
            self.d[last_val].append(index)
            self.d.pop(val)
            return True
    def getRandom(self) -> int:
        return random.choice(self.lst)
# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()