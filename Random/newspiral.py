# 
# def printSpiral(matrix):
#   result = []
#   rows = len(matrix)
#   topRow = 0
#   btmRow = rows -1
#   leftCol = 0
#   rightCol = len(matrix[0]) -1
#
#   if rows == 0:
#       return result
#
#   while (topRow <= btmRow and leftCol <= rightCol):
#     for i in range(leftCol, rightCol +1):
#       result.append(matrix[topRow][i])
#     topRow += 1
#
#     for i in range(topRow, btmRow+1):
#       result.append(matrix[i][rightCol])
#     rightCol -= 1
#
#     if topRow <= btmRow:
#       for i in range(rightCol, leftCol-1,-1):
#         result.append(matrix[btmRow][i])
#     btmRow -= 1
#
#     if leftCol <= rightCol:
#       for i in range(btmRow, topRow-1,-1):
#         result.append(matrix[i][leftCol])
#     leftCol += 1
#
#   return result


def printSpiral(matrix):
    result = []
    while matrix:
        result += matrix.pop(0)
        if matrix and matrix[0]:
            for row in matrix:
                result.append(row.pop())
        if matrix:
            result += matrix.pop()[::-1]
        if matrix and matrix[0]:
            for row in matrix[::-1]:
                result.append(row.pop(0))
    return result






print printSpiral([ [1,    2,   3,  4, 5],
                         [6,    7,   8,  9,   10],
                         [11,  12,  13,  14,  15],
                         [16,  17,  18,  19,  20] ])
