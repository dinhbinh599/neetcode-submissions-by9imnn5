class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        L = 1
        R = max(piles)

        minEatingSpeed = R

        while L <= R:
            mid = L + (R - L) // 2

            totalHour = self.calculateTotalHour(piles, mid)

            if totalHour <= h:
                R = mid - 1
                minEatingSpeed = mid
            else:
                L = mid + 1

        return int(minEatingSpeed)

    def calculateTotalHour(self, piles: List[int], speed: int) -> int:
        totalHour = 0
        for pile in piles:
            totalHour += math.ceil(pile / speed)

        return totalHour

