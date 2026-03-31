class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            L = 0
            R = len(row) - 1

            while L <= R:
                mid = L + (R - L) // 2

                if row[mid] == target:
                    return True
                elif target > row[mid]:
                    L = mid + 1
                else:
                    R = mid - 1

        return False  