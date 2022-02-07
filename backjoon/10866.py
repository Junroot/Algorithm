import sys


class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class Deque:
    def __init__(self):
        self.start = None
        self.end = None
        self.length = 0

    def push_front(self, x):
        new_node = Node(x)
        if self.length == 0:
            self.end = new_node
        else:
            self.start.prev = new_node
            new_node.next = self.start
        self.start = new_node
        self.length += 1

    def push_back(self, x):
        new_node = Node(x)
        if self.length == 0:
            self.start = new_node
        else:
            self.end.next = new_node
            new_node.prev = self.end
        self.end = new_node
        self.length += 1

    def pop_front(self):
        if self.length == 0:
            return -1
        front = self.start
        next = self.start.next
        front.next = None
        if next is not None:
            next.prev = None
        self.start = next
        self.length -= 1
        return front.data

    def pop_back(self):
        if self.length == 0:
            return -1
        back = self.end
        next = self.end.prev
        back.prev = None
        if next is not None:
            next.next = None
        self.end = next
        self.length -= 1
        return back.data

    def size(self):
        return self.length

    def empty(self):
        if self.length == 0:
            return 1
        return 0

    def front(self):
        if self.length == 0:
            return -1
        return self.start.data

    def back(self):
        if self.length == 0:
            return -1
        return self.end.data


n = int(sys.stdin.readline())
deque = Deque()
for _ in range(n):
    command = list(sys.stdin.readline().strip().split())
    if command[0] == "push_back":
        deque.push_back(command[1])
    elif command[0] == "push_front":
        deque.push_front(command[1])
    elif command[0] == "pop_front":
        print(deque.pop_front())
    elif command[0] == "pop_back":
        print(deque.pop_back())
    elif command[0] == "size":
        print(deque.size())
    elif command[0] == "empty":
        print(deque.empty())
    elif command[0] == "front":
        print(deque.front())
    else:
        print(deque.back())
