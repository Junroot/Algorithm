def solution(N, number):
    cache = [[] for i in range(9)]
    for i in range(1, 9):
        cache[i].append(int(str(N) * i))
        for j in range(1, i // 2 + 1):
            for left in cache[j]:
                for right in cache[i - j]:
                    cache[i].append(left + right)
                    if left > right:
                        cache[i].append(left - right)
                    else:
                        cache[i].append(right - left)
                    cache[i].append(right * left)
                    if left != 0:
                        cache[i].append(right // left)
                    if right != 0:
                        cache[i].append(left // right)
        if number in cache[i]:
            return i
    return -1
