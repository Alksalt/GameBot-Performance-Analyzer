class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        if nums:
            k = 0
        else:
            return 0

        i = 0
        n = len(nums)
        while i < n:

            if nums[i] == val:
                i += 1
            else:
                nums[k] = nums[i]
                k += 1
                i += 1
        nums[:] = nums[:k]
        return k, nums

ar = [2,3,3,2,1]
val = 2

s = Solution()
print(s.removeElement(ar, 2))