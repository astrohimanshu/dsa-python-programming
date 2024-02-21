# problem : print square matrix elements in clockwise spiral


# required functions
def firstrow(M, col):
    for i in range(col):
        print(M[0][i])
    del M[0]


def lastcol(M, row):
    for i in range(row):
        print(M[i][-1])
        del M[i][-1]


def lastrowrev(M, col):
    for i in range(col):
        print(M[-1][col - i - 1])
    del M[-1]


def firstcolrev(M, row):
    for i in range(row):
        print(M[row - i - 1][0])
        del M[row - i - 1][0]

 
def spiral(matrix: list, n: int) -> 'prints spiral elements':
    global M
    M = matrix
    row = n
    col = n
    if n == 1:
        print(M[0])
    elif n % 2 == 0 and M:
        for i in range(int(n / 2)):
            firstrow(M, col)
            row = row - 1

            lastcol(M, row)
            col = col - 1

            lastrowrev(M, col)
            row = row - 1

            firstcolrev(M, row)
            col = col - 1

    else:
        for i in range(int(n / 2) + 1):
            firstrow(M, col)
            row = row - 1
            if len(M) == 0:
                break

            lastcol(M, row)
            col = col - 1

            lastrowrev(M, col)
            row = row - 1

            firstcolrev(M, row)
            col = col - 1


if __name__ == '__main__':
    MM = [[12, 21, 31, 41, 51],
          [20, 33, 45, 71, 23],
          [62, 27, 19, 34, 12],
          [23, 14, 34, 52, 34],
          [11, 23, 34, 23, 90]]
    print([spiral(MM, 5)])
