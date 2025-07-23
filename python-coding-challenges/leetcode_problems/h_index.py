class Solution:
    def hIndex2(self, citations: list[int]) -> int:

        citations.sort()
        n = len(citations)

        for i in range(n):
            h = n - i
            if citations[i] >= h:
                return h
        return 0
    def hIndex(self, citations: list[int]) -> int:
        # with binary search
        middle = len(citations) // 2
        
        return middle






citations = [1,2,3,4,5,6,7,8,9,10]
c2 =[25, 8, 5, 3, 3, 3]
s = [0, 1, 3, 5, 6]
sol = Solution()
print(sol.hIndex(c2))