class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = len(nums) - 1
        current = k
        while k >= 0:
            if nums[k] == val:
                if k == current:
                    nums[k] = "_"
                    k -= 1
                    current -= 1
                    continue
                nums[k] = nums[current]
                nums[current] = "_"
                k -= 1
                current -= 1
            else:
                k -= 1

        return current + 1, nums

    def removeElement_two_pointer(self, nums: list[int], val: int) -> int:
        end = len(nums) - 1
        start = 0
        while start <= end:
            if nums[end] == val:
                nums[end] = "_"
                end -= 1
            if nums[start] == val:
                nums[start] = nums[end]
                nums[end] = '_'
                start += 1
                end -= 1
            else:
                start += 1

        return start, nums
    def trird(self, nums: list[int], val: int) -> int:
        n = len(nums)
        new = [None] * len(nums)
        i1 = i2 = 0
        while i1 <= n - 1:
            if nums[i1] == val:
                i1 += 1
            else:
                new[i2] = nums[i1]
                i1 += 1
                i2 += 1
        return i2, new
    def forth(self, nums: list[int], val: int) -> int:
        write = 0
        for read in range(len(nums)):
            if nums[read] != val:
                nums[write] = nums[read]
                write += 1

        return write



l = [3,2,2,3,4,5,5,2,1,3]
val = 3
sol = Solution()
#print(sol.removeElement(l, val))
#print(sol.removeElement_two_pointer(l, val))
print(sol.forth(l, val))