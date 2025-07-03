class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if nums:
            k = 1
        else:
            return 0
        i = 1
        n = len(nums)
        while i < n:
            if nums[k - 1] == nums[i]:
                i += 1
            else:
                nums[k] = nums[i]
                k += 1
                i += 1
        nums[:] = nums[:k]
        return k, nums



ar = [1,1,2,2,3,3,3,4]
ar2 = [1,2]
k = 2
i = 3
s = Solution()
print(s.removeDuplicates(ar))