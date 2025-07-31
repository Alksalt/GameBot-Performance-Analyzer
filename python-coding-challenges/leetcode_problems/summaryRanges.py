class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        result = []
        n = len(nums)
        start = 0
        for i in range(1, n + 1):

            if i == n or nums[i] != nums[i - 1] + 1:
                if start == i - 1:
                    result.append(str(nums[start]))
                else:
                    result.append(f"{nums[start]}->{nums[i - 1]}")
                start = i
        return result


"""Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]"""
#['0->2', '3->4']

n1 = [0,2,3,4,6,8,9]

n2 = [0,1]

n3 = [0,1,2,4,5,7]

n4 = [1]

n5 = []
sol = Solution()
print(sol.summaryRanges(n1))