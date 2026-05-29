class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        for row in matrix:
            if target <= row[-1]:
                l, r = 0, len(row)
                while l <= r:
                    m = l + ((r - l) // 2)

                    if target < row[m]:
                        r = m - 1
                    elif target > row[m]:
                        l = m + 1
                    else:
                        return True
                return False

        return False

        