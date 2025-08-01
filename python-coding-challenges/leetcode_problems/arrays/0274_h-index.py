"""
Problem: 0274. H-Index
Link: https://leetcode.com/problems/h-index/

Description:
    Given a list of citations, compute the researcher's h-index.

Approach:
    Sort citations and find the maximum h such that at least h papers have ≥ h citations.

Time Complexity: O(N log N)
Space Complexity: O(1)
"""

class Solution:
    def hIndex2(self, citations: list[int]) -> int:

        citations.sort()
        n = len(citations)

        for i in range(n):
            h = n - i
            if citations[i] >= h:
                return h
        return 0






citations = [1,2,3,4,5,6,7,8,9,10]
c2 =[25, 8, 5, 3, 3, 3]
s = [0, 1, 3, 5, 6]
sol = Solution()
print(sol.hIndex(c2))