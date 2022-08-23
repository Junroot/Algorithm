from collections import deque


class Node:
    def __init__(self, char):
        self.char = char
        self.next_nodes = dict()
        self.children_count = 0
        self.is_end = False


def add_word(word, root_node: Node):
    current_node = root_node
    for c in word:
        current_node.children_count += 1
        if c not in current_node.next_nodes:
            current_node.next_nodes[c] = Node(c)

        current_node = current_node.next_nodes[c]
    current_node.children_count += 1
    current_node.is_end = True


def solution(words):
    root_node = Node("")
    for word in words:
        add_word(word, root_node)

    result = 0
    queue = deque([(root_node, 0)])
    while queue:
        current_node, depth = queue.popleft()
        if current_node.children_count == 1:
            result += depth
            continue
        if current_node.is_end:
            result += depth
        for next_node in current_node.next_nodes.values():
            queue.append((next_node, depth + 1))

    return result

print(solution(["go","gone","guild"]))
