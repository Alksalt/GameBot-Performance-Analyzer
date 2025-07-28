class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        d_with_idx = {}
        for i, num in enumerate(nums):
            if num in d_with_idx and i - d_with_idx[num] <= k:
                return True
            d_with_idx[num] = i
        return False


nums = [1,2,3,1]
k = 3
sol = Solution()
print(sol.containsNearbyDuplicate(nums,k))