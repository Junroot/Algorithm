
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


n = int(input())
nodes = [Node(chr(ord('A') + i)) for i in range(n)]


def get_node(data):
    if data == ".":
        return None
    return nodes[ord(data) - ord('A')]


def preorder(node):
    if node is None:
        return ""
    return node.data + preorder(node.left) + preorder(node.right)


def inorder(node):
    if node is None:
        return ""
    return inorder(node.left) + node.data + inorder(node.right)


def postorder(node):
    if node is None:
        return ""
    return postorder(node.left) + postorder(node.right) + node.data


for i in range(n):
    parent, left, right = input().split()
    parent_node = get_node(parent)
    parent_node.left = get_node(left)
    parent_node.right = get_node(right)


print(preorder(nodes[0]))
print(inorder(nodes[0]))
print(postorder(nodes[0]))