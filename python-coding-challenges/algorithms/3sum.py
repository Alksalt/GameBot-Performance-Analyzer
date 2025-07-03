class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []
        n = len(nums)

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j = i + 1
            k = n - 1

            while j < k:
                current = nums[i] + nums[j] + nums[k]
                if current == 0:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1

                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1

                elif current < 0:
                    j += 1
                else:
                    k -= 1

        return result

sol = Solution()
print(sol.threeSum([1,0,-1,1,-2,1,2,3,4,4,-4,4,]))