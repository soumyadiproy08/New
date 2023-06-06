from math import *
from collections import *
from sys import *
from os import *
from typing import List

def setZeros(matrix: List[List[int]]) -> None:
	# Write your code here.
    R = len(matrix)
    C = len(matrix[0])
    rows, cols = set(), set()

    # Essentially, we mark the rows and columns that are to be made zero
    for i in range(R):
        for j in range(C):
            if matrix[i][j] == 0:
                rows.add(i)
                cols.add(j)
    print(rows,cols)
    # Iterate over the array once again and using the rows and cols sets, update the elements
    for i in range(R):
        for j in range(C):
            if i in rows or j in cols:
                matrix[i][j] = 0

# Example usage
matrix = [
    [1,1,1,1],
    [1,0,0,1],
    [1,1,0,1],
    [1,1,1,1]
]

setZeros(matrix)
print(matrix)

# Print the modified matrix
# for row in matrix:
#     print(row)