#!/usr/bin/python3
""" N queens
"""

if __name__ == '__main__':

    import sys

    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        size = int(sys.argv[1])
    except BaseException:
        print("N must be a number")
        sys.exit(1)
    if size < 4:
        print("N must be at least 4")
        sys.exit(1)

    def startSolve():
        b = [[0 for j in range(size)] for i in range(size)]
        checkRecursive(b, 0)
        return

    def checkRecursive(b, c):
        if (c == size):
            solution(b)
            return True
        ret = False
        for i in range(size):
            if (checkPosition(b, i, c)):
                b[i][c] = 1
                ret = checkRecursive(b, c + 1) or ret
                b[i][c] = 0
        return ret

    def checkPosition(b, r, c):
        for i in range(c):
            if (b[r][i]):
                return False
        i = r
        j = c
        while i >= 0 and j >= 0:
            if(b[i][j]):
                return False
            i = i - 1
            j = j - 1
        i = r
        j = c
        while j >= 0 and i < size:
            if(b[i][j]):
                return False
            i = i + 1
            j = j - 1
        return True

    def solution(b):
        solve = []
        for i in range(size):
            for j in range(size):
                if(b[i][j] is 1):
                    solve.append([i, j])
        print(solve)
        solve.clear()
    startSolve()
