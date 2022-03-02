import sys

sys.setrecursionlimit(10 ** 6)

n = int(input())
inorder = list(map(int, input().split()))
postorder = list(map(int, input().split()))

index_of_inorder = [0 for _ in range(n + 1)]

for index in range(len(inorder)):
    index_of_inorder[inorder[index]] = index


def print_preorder(in_start, in_end, post_start, post_end):
    if in_start > in_end or post_start > post_end:
        return
    parent = postorder[post_end]
    print(parent, end=" ")
    left_length = index_of_inorder[parent] - in_start
    if left_length > 0:
        print_preorder(in_start, index_of_inorder[parent] - 1, post_start, post_start + left_length - 1)
    right_length = in_end - index_of_inorder[parent]
    if right_length > 0:
        print_preorder(index_of_inorder[parent] + 1, in_end, post_end - right_length, post_end - 1)


print_preorder(0, n - 1, 0, n - 1)
