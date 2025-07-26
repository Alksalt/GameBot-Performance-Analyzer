class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        nums.sort()

        return 0


target = 7
nums = [2,3,1,2,4,3]
sol = Solution()
print(sol.minSubArrayLen(target,nums))