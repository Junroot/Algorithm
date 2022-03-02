from sys import stdin


class PriorityQueue:

    def __init__(self):
        self.list = []

    def push(self, data):
        self.list.append(data)
        now = len(self.list) - 1
        while now > 0:
            parent = self.parent(now)
            if self.list[parent] <= data:
                break
            self.list[now] = self.list[parent]
            now = parent
        self.list[now] = data

    def pop(self):
        if len(self.list) == 0:
            return 0
        result = self.list[0]
        data = self.list.pop()
        if len(self.list) == 0:
            return result
        now = 0
        while now < len(self.list):
            left = self.left(now)
            right = self.right(now)
            next = now
            if left < len(self.list) and data > self.list[left]:
                self.list[now] = self.list[left]
                next = left
            if right < len(self.list) and self.list[left] > self.list[right] and data > self.list[right]:
                self.list[now] = self.list[right]
                next = right
            if next == now:
                break
            now = next
        self.list[now] = data
        return result

    def parent(self, index):
        return (index - 1) // 2

    def left(self, index):
        return index * 2 + 1

    def right(self, index):
        return index * 2 + 2


n = int(stdin.readline())
pq = PriorityQueue()
for _ in range(n):
    x = int(stdin.readline())
    if x == 0:
        print(pq.pop())
    else:
        pq.push(x)
