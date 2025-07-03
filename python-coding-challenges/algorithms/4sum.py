class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        result = []
        n = len(nums)

        for first in range(n - 3):
            if first > 0 and nums[first] == nums[first - 1]:
                continue

            for second in range(first + 1, n - 2):
                if second > first + 1 and nums[second] == nums[second - 1]:
                    continue

                left = second + 1
                right = n - 1

                while left < right:
                    current = nums[first] + nums[second] + nums[left] + nums[right]
                    if current == target:
                        result.append([nums[first], nums[second], nums[left], nums[right]])
                        left += 1
                        right -= 1

                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1

                    elif current < target:
                        left += 1
                    else:
                        right -= 1

        return result

sol = Solution()
print(sol.fourSum([1, 0, -1, 1, -2, 1, 2, 3, 4, 4, -4, 4], 6))