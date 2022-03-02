import sys


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def change_next(self, node):
        self.next = node


class Queue:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def push(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        if self.tail is not None:
            self.tail.change_next(node)
        self.tail = node
        self.size += 1

    def pop(self):
        if self.size == 0:
            return -1
        node = self.head
        self.head = self.head.next
        self.size -= 1
        return node.data

    def empty(self):
        if self.size == 0:
            return 1
        return 0

    def front(self):
        if self.size == 0:
            return -1
        return self.head.data

    def back(self):
        if self.size == 0:
            return -1
        return self.tail.data


n = int(sys.stdin.readline())
q = Queue()

for _ in range(n):
    command = list(sys.stdin.readline().strip().split())
    operator = command[0]

    if operator == "push":
        q.push(command[1])
    elif operator == "pop":
        print(q.pop())
    elif operator == "size":
        print(q.size)
    elif operator == "empty":
        print(q.empty())
    elif operator == "front":
        print(q.front())
    else:
        print(q.back())
