class Solution:
    def maxArea(self, heights: List[int]) -> int:
        L = 0
        R = len(heights) - 1

        maxValue = 0

        while L < R:
            amount = (R - L) * min(heights[L], heights[R])

            maxValue = max(maxValue, amount)

            if heights[L] < heights[R]:
                L += 1
            else:
                R -= 1

        return maxValue