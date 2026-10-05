class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        totalsum = 0
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if len(mat) - 1 - i == j or i == j:
                    totalsum += mat[i][j]
        return totalsum
        