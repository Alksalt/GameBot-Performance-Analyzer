class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        middle = len(nums) // 2

        while left <= right:

            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                left = middle + 1
                middle = (left + right) // 2
            else:
                right = middle - 1
                middle = (left + right) // 2
        return left



ar = [1,4,6,7,8,9,10,11,14,16]
target = 1

s = Solution()
print(s.searchInsert(ar, target))