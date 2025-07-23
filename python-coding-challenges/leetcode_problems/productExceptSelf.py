
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        answer = [1] * n

        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in reversed(range(n)):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer


nums = [1,2,3,4]
Output = [24,12,8,6]
sol = Solution()
print(sol.productExceptSelf(nums))
