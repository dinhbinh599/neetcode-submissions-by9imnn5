class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L = 0
        profit = 0

        for R in range(len(prices)):
            if R == 0:
                continue

            if prices[R] < prices[L]:
                L = R
                continue
            
            profit = max(profit, prices[R] - prices[L])

        return profit