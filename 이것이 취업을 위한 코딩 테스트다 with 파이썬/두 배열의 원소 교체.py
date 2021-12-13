n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)
index = 0
count = 0

while count < k and index < len(a):
    if a[index] < b[index]:
        a[index], b[index] = b[index], a[index]
        count += 1
        index += 1
    else:
        break

print(sum(a))
