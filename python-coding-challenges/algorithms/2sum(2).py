class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        n = len(numbers)
        left = 0
        right = n - 1
        while left < right:
            current = numbers[left] + numbers[right]
            if current == target:
                return [left +1, right +1]
            elif current < target:
                left += 1
            else:
                right -= 1
        return []




sol = Solution()
num = sorted([1,2,3,4,6,8,11,2,1,2,3,5,7,4])

print(sol.twoSum(num, 8))