n = int(input())

bigger_bag_count = n // 5
remainder = n - bigger_bag_count * 5

bigger_bag_count -= remainder % 3
if bigger_bag_count < 0:
    print(-1)
else:
    smaller_bag_count = (n - bigger_bag_count * 5) // 3
    print(bigger_bag_count + smaller_bag_count)
