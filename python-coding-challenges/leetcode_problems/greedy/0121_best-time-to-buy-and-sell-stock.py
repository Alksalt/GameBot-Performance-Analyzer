
"""
Problem: 0121. Best Time to Buy and Sell Stock
Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

Description:
    Find the maximum profit from buying and selling a stock once or multiple times given daily prices.

Approach:
    Track min price for single transaction; accumulate profits for multiple transactions.

Time Complexity: O(N)
Space Complexity: O(1)
"""

class Solution:
    def maxProfit2(self, prices: list[int]) -> int:
        if not prices:
            return 0
        n = len(prices)

        min_price = prices[0]
        max_profit = 0
        for i in range(1, n):
            current = prices[i] - min_price
            if current > max_profit:
                max_profit = current
            if prices[i] < min_price:
                min_price = prices[i]

        return max_profit


    def maxProfit3(self, prices: list[int]) -> int:

        if not prices:
            return 0

        max_profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                max_profit += prices[i] - prices[i-1]
        return max_profit

    """def maxProfit(self, prices: list[int]) -> int:
        if not prices:
            return 0
        n = len(prices)
        max_profit = []
        temp_profit = 0
        count = 0
        for i in range(1, n):
            if prices[i] > prices[i-1] and count < 2:
                temp_profit += prices[i] - prices[i-1]

            elif prices[i] < prices[i-1] and count < 2:
                if temp_profit > 0:
                    max_profit.append(temp_profit)
                    temp_profit = 0
                    count += 1

            if prices[i] > prices[i - 1] and count == 2:
                temp_profit += prices[i] - prices[i - 1]

            elif prices[i] < prices[i - 1] and count == 2:
                if temp_profit > max_profit[0]:
                    max_profit[0] = prices[i] - prices[i-1]
                    temp_profit = 0
                elif temp_profit > max_profit[1]:
                    max_profit[1] = prices[i] - prices[i - 1]
                    temp_profit = 0
                else:
                    temp_profit = 0
        if i == n-1:
            if temp_profit and count < 2:
                max_profit.append(temp_profit)
            elif temp_profit and count == 2:
                if temp_profit > max_profit[0]:
                    max_profit[0] = prices[i] - prices[i-1]
                    temp_profit = 0
                elif temp_profit > max_profit[1]:
                    max_profit[1] = prices[i] - prices[i - 1]
                    temp_profit = 0
                else:
                    temp_profit = 0

        return sum(max_profit)

prices = [1,2,3,4,5,1,2,3,4,5,1,2,3]
sol = Solution()
print(sol.maxProfit(prices))"""
