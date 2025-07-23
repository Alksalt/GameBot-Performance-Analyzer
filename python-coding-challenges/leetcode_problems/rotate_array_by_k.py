class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        k = k % n

        nums.reverse()
        i1, i2 = 0, k - 1

        while i1 < i2:
            nums[i1], nums[i2] = nums[i2], nums[i1]
            i1 += 1
            i2 -= 1

        i1, i2 = k, n - 1

        while i1 < i2:
            nums[i1], nums[i2] = nums[i2], nums[i1]
            i1 += 1
            i2 -= 1

    def rotate2(self, nums: list[int], k: int) -> None:
        n = len(nums)
        k %= n  # normalise k
        if k == 0:  # nothing to do
            return

        
        tail = nums[-k:]
        return tail

    def rotate3(self, nums: list[int], k: int) -> None:
        n = len(nums)
        k %= n
        if k == 0:
            return


        tail = nums[-k:]
        nums[k:] = nums[:-k]
        nums[:k] = tail
        return nums


nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
sol = Solution()
print(sol.rotate3(nums, k))

