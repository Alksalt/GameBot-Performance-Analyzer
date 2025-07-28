class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        n = len(nums)
        start = 0
        sub_sum = 0
        best_length = float('inf')

        for end in range(n):
            sub_sum += nums[end]

            while sub_sum >= target:
                best_length = (end + 1 - start) if (end + 1 - start) < best_length else best_length
                start += 1
                sub_sum -= nums[start - 1]



        return 0 if best_length == float('inf') else best_length


target = 7
nums = [2,3,1,2,4,3]
sol = Solution()
print(sol.minSubArrayLen(target,nums))