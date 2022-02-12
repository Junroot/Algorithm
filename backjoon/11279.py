from sys import stdin


class PriorityQueue:

    def __init__(self):
        self.list = []

    def push(self, data):
        self.list.append(data)
        now = len(self.list) - 1
        while now > 0:
            parent_index = self.parent(now)
            if self.list[parent_index] >= data:
                break
            self.list[now] = self.list[parent_index]
            now = parent_index
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
            left_index = self.left(now)
            right_index = self.right(now)
            next = now
            if left_index < len(self.list) and self.list[left_index] > data:
                self.list[now] = self.list[left_index]
                next = left_index
            if right_index < len(self.list) and self.list[right_index] > self.list[left_index] and self.list[right_index] > data:
                self.list[now] = self.list[right_index]
                next = right_index
            if now == next:
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
