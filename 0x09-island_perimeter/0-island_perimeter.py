#!/usr/bin/python3
""" Island Perimeter mandatory """


def check0(n):
    """check zero
    """
    if (n == 0):
        return 1
    return 0


def island_perimeter(grid):
    """
    Island perimeter
    """
    row = len(grid)
    col = len(grid[0])
    assert (1 <= row and col <= 100), "length must be between 1 an 100"

    p = 0
    for i in range(row):
        for j in range(col):
            assert (grid[i][j] == 0) or (grid[i][j] == 1),\
                                        "grid numbers must be 0 or 1"
            if grid[i][j] == 1:
                if i-1 < 0:
                    p += 1
                else:
                    p += check0(grid[i-1][j])
                if j-1 < 0:
                    p += 1
                else:
                    p += check0(grid[i][j-1])

                try:
                    p += check0(grid[i+1][j])
                except IndexError:
                    p += 1
                try:
                    p += check0(grid[i][j+1])
                except IndexError:
                    p += 1

    return p
