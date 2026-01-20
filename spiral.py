matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12]]
    
rows = len(matrix)
cols = len(matrix[0])
    
left = 0
right = cols - 1
top = 0
bottom = rows - 1
    
result = []
    
while left <= right and top <= bottom:
    # 从左往右遍历
    for col in range(left, right + 1):
        result.append(matrix[top][col])
    
    # 从上往下遍历
    for row in range(top + 1, bottom + 1):
        result.append(matrix[row][right])
    
    if left < right and top < bottom:
        # 从右往左遍历
        for col in range(right - 1, left, -1):
            result.append(matrix[bottom][col])
    
        # 从下往上遍历
        for row in range(bottom, top, -1):
            result.append(matrix[row][left])
    
    left = left + 1
    right = right - 1
    top = top + 1
    bottom = bottom - 1
    
print(result)
