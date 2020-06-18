# You're given a two-dimensional array (a matrix) of potentially unequal
# height and width containing only 0 s and 1 s. Each 0 represents land,
# and each 1 represents part of a river. A river consists of any number of
# 1 s that are either horizontally or vertically adjacent (but not diagonally
# adjacent). The number of adjacent 1 s forming a river determine its size.
# Write a function that returns an array of the sizes of all rivers represente


def riverSizes(matrix:[][]) -> list:
    # Write your code here.
    pass



# Test cases:
assert riverSizes(matrix = [
 [1, 0, 0, 1, 0],
 [1, 0, 1, 0, 0],
 [0, 0, 1, 0, 1],
 [1, 0, 1, 0, 1],
 [1, 0, 1, 1, 0],
]) == [1, 2, 2, 2, 5]
