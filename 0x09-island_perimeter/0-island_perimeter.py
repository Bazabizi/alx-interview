#!/usr/bin/python3
"""
Island Perimeter
"""

def island_perimeter(grid):
    """
     returns the perimeter of the island described in grid
    :param grid:
    :return:
    """
    rows = len(grid)
    cols = len(grid[0])

    perimeter = 0
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                adjacent = 0
                if row > 0 and grid[row-1][col] == 1:
                    adjacent += 1
                if row < rows-1 and grid[row+1][col] == 1:
                    adjacent += 1
                if col > 0 and grid[row][col-1] == 1:
                    adjacent += 1
                if col < cols-1 and grid[row][col+1] == 1:
                    adjacent += 1
                
                perimeter += 4 - adjacent
    return perimeter
