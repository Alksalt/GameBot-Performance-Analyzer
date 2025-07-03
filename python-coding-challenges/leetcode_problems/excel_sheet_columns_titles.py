class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = []

        while columnNumber > 0:
            columnNumber -= 1
            reminder = columnNumber % 26
            result.append(chr(ord('A') + reminder))
            columnNumber //= 26

        return ''.join(reversed(result))

    def convertToTitle_two(self, columnNumber: int) -> str:
        if not (0 < columnNumber < 16_385):
            raise ValueError("Incorrect input: columnNumber must be between 1 and 16384")
        if columnNumber < 27:
            return chr(ord('A') + columnNumber - 1)

        if columnNumber < 703:
            columnNumber -= 1
            second = columnNumber % 26
            first = columnNumber // 26
            return chr(ord('A') + first - 1) + chr(ord('A') + second )

        columnNumber -= 1
        third = columnNumber % 26
        columnNumber //= 26
        columnNumber -= 1
        second = columnNumber % 26
        columnNumber //= 26
        first = columnNumber

        return (chr(ord('A') + first - 1) +
                chr(ord('A') + second) +
                chr(ord('A') + third))




n = 1000000000000

sol = Solution()
print(sol.convertToTitle(n))



