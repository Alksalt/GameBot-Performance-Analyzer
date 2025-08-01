
"""
Problem: 0380. Insert Delete GetRandom O(1)
Link: https://leetcode.com/problems/insert-delete-getrandom-o1/

Description:
    Design a data structure that supports insert, delete, and getRandom in average O(1) time.

Approach:
    Use a list and hash map for O(1) operations.

Time Complexity: O(1) average per operation
Space Complexity: O(N)
"""

import random

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
        last_val = self.lst[-1]
        self.lst[index], self.lst[-1] = last_val, self.lst[index]
        self.lst.pop()
        self.d[last_val] = index
        self.d.pop(val)
        return True

    def getRandom(self) -> int:
        return random.choice(self.lst)

if __name__ == "__main__":
    # Example usage
    obj = RandomizedSet()
    print(obj.insert(1))    # True
    print(obj.remove(2))    # False
    print(obj.insert(2))    # True
    print(obj.getRandom())  # 1 or 2
    print(obj.remove(1))    # True
    print(obj.insert(2))    # False
    print(obj.getRandom())  # 2