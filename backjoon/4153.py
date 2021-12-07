while True:
    dimensions = list(map(int, input().split()))
    if dimensions[0] == dimensions[1] == dimensions[2] == 0:
        break

    dimensions.sort()
    if dimensions[0] ** 2 + dimensions[1] ** 2 == dimensions[2] ** 2:
        print("right")
    else:
        print("wrong")

