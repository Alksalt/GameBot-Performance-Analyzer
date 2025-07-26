class Solution:
    def missingInteger(self, nums: list[int]) -> int:
        n = len(nums)
        seq_sum = nums[0]

        for i in range(1, n):
            if nums[i] == nums[i - 1] + 1:
                seq_sum += nums[i]
            else:
                break

        seq_set = set(nums)

        while seq_sum in seq_set:
            seq_sum += 1


        return seq_sum

nums = [3,4,5,1,12,14,13]
n = [1,2,3,4,5]

sol = Solution()
print(sol.missingInteger(nums))