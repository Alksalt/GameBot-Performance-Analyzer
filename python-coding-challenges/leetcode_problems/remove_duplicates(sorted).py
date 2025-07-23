class Solution:
    def removeDuplicates2(self, nums: list[int]) -> int:
        if not nums:
            return 0
        write = 1
        scan = 0
        for read in range(1,len(nums)):
            if nums[scan] == nums[read]:
                continue
            else:
                nums[write] = nums[read]
                scan = read
                write += 1
        return write

    def removeDuplicates(nums: list[int]) -> int:
        if not nums:
            return 0

        write = 1
        count = 1

        for read in range(1, len(nums)):
            if nums[read] == nums[read - 1]:
                count += 1
            else:
                count = 1  # new number, reset count

            if count <= 2:
                nums[write] = nums[read]
                write += 1

        return write


l = [1,1,1,2,2,2,3]
d = [1,1,2,2]
l2 = [1,1,2,2,]
sol = Solution()
print(sol.removeDuplicates(l))
