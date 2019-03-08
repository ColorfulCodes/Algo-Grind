# given 2d array print array in spiral form
def spiral(matrix):
        result = []
        row =len(matrix)
        if row == 0:
            return result
        l = 0
        colIndex = len(matrix[0]) -1
        t = 0
        b = row-1

        while l <= colIndex  and t <= b:

            # move right & grab row
            for i in range(l, colIndex+1):
                result.append(matrix[l][i])
            #one row down, increment
            t +=1
            # move down, start i at next index since already
            #grabbed above
            for i in range(t, b+1):
                result.append(matrix[i][colIndex])
            # -1 col since one col is now complete
            colIndex -=1


            if t <= b:
                # move left/back wards starting at 2 or so to
                # before -1
                for i in range(colIndex, l-1, -1):
                    result.append(matrix[b][i])
                # -1 a row, one other row complete
                b -=1

            if l <= colIndex:
                # move up
                for i in range(b, t-1, -1):
                    result.append(matrix[i][l])
                l +=1
        return result

# def spiral(matrix):
#     # first row: everything to the right
#     #
#     res = []
#     if not matrix:
#         return []
#     i,j,di,dj = 0,0,0,1
#     m, n = len(matrix),len(matrix[0])
#     for v in xrange(m * n):
#         res.append(matrix[i][j])
#         matrix[i][j] = ''
#         if matrix[(i+di)%m][(j+dj)%n] == '':
#             di, dj = dj, -di
#         i += di
#         j += dj
#     print (res)
#     return res
#
#
print spiral([
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
])



#
# def spiral(matrix):
#
#     if matrix == []:
#       return matrix
#
#     l = 0
#     r = len(matrix[0]) - 1
#     t = 0
#     b = len(matrix) - 1
#
#     ret = []
#     while l < r and t < b:
#         # top
#         for i in range(l, r):
#             ret.append(matrix[t][i])
#         # right
#         for i in range(t, b):
#             ret.append(matrix[i][r])
#         # bottom
#         for i in range(r, l, -1):
#             ret.append(matrix[b][i])
#         # left
#         for i in range(b, t, -1):
#             ret.append(matrix[i][l])
#
#         l += 1
#         r -= 1
#         t += 1
#         b -= 1
#michaelpiazza

#     # single square
#     if l == r and t == b:
#         ret.append(matrix[t][l])
#     # vertical line
#     elif l == r:
#        for i in range(t, b + 1):
#            ret.append(matrix[i][l])
#    # horizontal line
#     elif t == b:
#        for i in range(l, r + 1):
#            ret.append(matrix[t][i])
#    return ret
# spiral([
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ])
#
#

# Solution 3
#
# def spiral(matrix):
#     ret = []
#     while matrix:
#         ret += matrix.pop(0)
#         if matrix and matrix[0]:
#             for row in matrix:
#                 ret.append(row.pop())
#         if matrix:
#             ret += matrix.pop()[::-1]
#         if matrix and matrix[0]:
#             for row in matrix[::-1]:
#                 ret.append(row.pop(0))
#     return ret
#
# spiral([
#  [ 1, 2, 3,"a" ],
#  [ 4, 5, 6,"b" ],
#  [ 7, 8, 9 ,"c"]
# ])
