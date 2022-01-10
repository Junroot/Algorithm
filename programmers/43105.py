def solution(triangle):
    values = [[triangle[0][0]]]
    for i in range(1, len(triangle)):
        values.append([])
        for j in range(i + 1):
            left = 0
            right = 0
            if j != 0:
                left = values[i - 1][j - 1]
            if j != i:
                right = values[i - 1][j]
            values[i].append(max(left, right) + triangle[i][j])
    return max(values[len(triangle) - 1])
