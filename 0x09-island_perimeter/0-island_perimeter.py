#!/usr/bin/python3
"""
Island Perimeter
"""

def island_perimeter(grid):
    rows, cols = len(grid), len(grid[0])
    perimeter = 0
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                # Count top and bottom neighbors
                if row == 0 or grid[row-1][col] == 0:
                    perimeter += 1
                if row == rows-1 or grid[row+1][col] == 0:
                    perimeter += 1
                # Count left and right neighbors
                if col == 0 or grid[row][col-1] == 0:
                    perimeter += 1
                if col == cols-1 or grid[row][col+1] == 0:
                    perimeter += 1
    return perimeter
