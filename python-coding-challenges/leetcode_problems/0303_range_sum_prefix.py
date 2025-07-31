class NumArray:

    def __init__(self, nums: list[int]):
        self.lst = nums
    def sumRange(self, left: int, right: int) -> int:
        

    def sumRange_brute(self, left: int, right: int) -> int:
        result = 0
        for i in range(left, right + 1):
            result += self.nums[i]

        return result

num_array = NumArray([1, 3, 4, 5, 6, 7, 43, 3, 4, 5, 7, 9, 6])

print(num_array.sumRange(1, 5))