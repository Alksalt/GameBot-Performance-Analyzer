class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        i1 = m - 1
        i2 = n - 1
        k = m + n - 1
        while i2 >= 0:
            if i1 >= 0 and nums1[i1] > nums2[i2]:
                nums1[k] = nums1[i1]
                i1 -= 1
            else:
                nums1[k] = nums2[i2]
                i2 -= 1
            k -= 1
l1 = [1,2,3,0,0,0]
m = 3
l2 = [2,5,7]
n = 3

s = Solution()
s.merge(l1,3,l2,3)
print(l1)

