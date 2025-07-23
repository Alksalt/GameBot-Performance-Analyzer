from collections import deque
class Solution:
    def canJump(self, nums: list[int]) -> bool: #simple if we can only with mx_jump
        if not nums:
            return False
        n = len(nums)

        i = 0
        while i < n - 1:
            i = i + nums[i]
            if i > n - 1 or ((i < n -1) and (nums[i] ==0)):
                return False
        return True

    def canJump2(self, nums: list[int]) -> bool:
        if not nums:
            return False
        max_reach = 0
        for i, jump in enumerate(nums):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + jump)
            if max_reach >= len(nums) - 1 :
                return True
        return True

    def jump(self, nums: list[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0

        farthest = 0
        jumps = 0
        current_end = 0

        for i in range(n - 1):

            if i > farthest:
                return -1

            farthest = max(farthest, i + nums[i])
            if current_end == i:
                jumps += 1
                current_end = farthest

            if current_end >= n - 1:
                break

        return jumps

    def canReach(self, arr: list[int], start: int) -> bool:
        visited = set()
        queue = deque([start])
        n = len(arr)
        while queue:
            i = queue.popleft()

            right = i + arr[i]
            left = i - arr[i]
            if i in visited:
                continue
            else:
                visited.add(i)
            if right < n:
                if arr[right] == 0:
                    return True
                queue.append(right)
            if left >= 0:
                if arr[left] == 0:
                    return True
                queue.append(left)

        return False
arr = [4,2,3,0,3,1,2]
start = 5


nums = [2, 3, 1, 1, 4]
nums2 = [3,1,1,5,1]
nums3 = [3,2,1,0,4]
nums4 = [2, 1, 1, 1]
nums5 = [2, 3, 1, 0,  1, 1, 3]
sol = Solution()
print(sol.canReach(nums5, 5))