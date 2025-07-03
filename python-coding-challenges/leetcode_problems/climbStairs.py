class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        first = 1
        second = 2
        for _ in range(3, n +1):
            third = first + second
            first = second
            second = third
        return second

    def climbStairs2(self, n, first=1, second=2) -> int:
        if n == 2:
            return second
        if n == 1:
            return first
        third = first + second
        return self.climbStairs2(n-1, second, third)



s = Solution()

print(s.climbStairs(5))
print(s.climbStairs2(5))