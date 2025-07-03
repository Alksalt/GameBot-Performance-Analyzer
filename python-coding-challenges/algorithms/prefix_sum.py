class NumArray:

    def __init__(self, nums: list[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        prefix_sum = [0] * len(self.nums)
        prefix_sum[0] = self.nums[0]
        for i in range(1, len(self.nums)):
            prefix_sum[i] = prefix_sum[i - 1] + self.nums[i]

        result = prefix_sum[right] - prefix_sum[left - 1]
        print(prefix_sum)
        return result

r = 3 + 4 + 5 + 6 + 7



num_array = NumArray([1,3,4,5,6,7,43,3,4,5,7,9,6])

print(num_array.sumRange(1,5))