import heapq

n = int(input())
numbers = list(map(int, input().split()))

pq = [(-1, numbers[0])]

for i in range(1, n):
    max_length = 1
    temp_pq = pq[:]
    while temp_pq:
        length, number = heapq.heappop(temp_pq)
        length = -length
        if number < numbers[i]:
            max_length = length + 1
            break
    heapq.heappush(pq, (-max_length, numbers[i]))

print(-heapq.heappop(pq)[0])
