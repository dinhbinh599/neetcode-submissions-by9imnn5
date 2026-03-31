class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = 0
        m = len(matrix) - 1

        colLength = len(matrix[0]) - 1

        searchRowNumber = -1

        while n <= m:
            mid = n + (m - n) // 2

            pos = self.targetPosition(colLength, matrix[mid], target)

            if pos == 0:
                searchRowNumber = mid
                break;
            elif pos == 1:
                n = mid + 1
            elif pos == -1:
                m = mid - 1

        if searchRowNumber != -1:
            row = matrix[searchRowNumber]

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

    def targetPosition(self, colLength: int, row: List[int], target: int) -> int:
        if row[0] <= target <= row[colLength]:
            return 0
        elif target < row[0]:
            return -1
        else:
            return 1