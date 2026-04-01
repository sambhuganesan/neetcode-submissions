class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        k = n-1

        for i in range(0, n //2 + 1):
            for j in range(i, k -i):
                temp = matrix[i][j]
                matrix[i][j] = matrix[k-j][i]
                matrix[k-j][i] = matrix[k-i][k-j]
                matrix[k-i][k-j] = matrix[j][k-i]
                matrix[j][k-i] = temp
        return