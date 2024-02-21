""" problem : a matrix is diagonally dominant if all diagonal elements
              >  non diag elements for all rows."""


def diagdom(matrix: list, n: int) -> bool:
    M = matrix
    k = 0
    for i in range(n):
        rowsum = 0
        diag = M[i][i]
        for j in range(n):
            rowsum += M[i][j]
        if diag <= rowsum - diag:
            return False
        else:
            k = k + 1
            if k == n:
                return True


if __name__ == '__main__':
    mat = [[1, 1, 1, 1],
           [2, 22, 2, 2],
           [3, 3, 33, 3],
           [4, 4, 4, 455]]
    print(diagdom(mat, 4))