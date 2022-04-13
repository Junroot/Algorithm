x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

dx1 = x2 - x1
dx3 = x4 - x3
dy1 = y2 - y1
dy3 = y4 - y3

if dx3 * dy1 == dx1 * dy3:
    if dx1 != 0 and (y1 - y3) * dx1 * dx3 == x1 * dx3 * dy1 - x3 * dx1 * dy3 and \
            min(max(x1, x2), max(x3, x4)) >= max(min(x1, x2), min(x3, x4)):
        print(1)
    elif dx1 == 0 and x1 == x3 and \
            min(max(y1, y2), max(y3, y4)) >= max(min(y1, y2), min(y3, y4)):
        print(1)
    else:
        print(0)
else:
    if dx1 == 0:
        y = dy3 * (x1 - x3) + dx3 * y3
        threshold1 = min(y1, y2) * dx3
        threshold2 = max(y1, y2) * dx3
        if min(x3, x4) <= x1 <= max(x3, x4):
            if dx3 > 0 and threshold1 <= y <= threshold2:
                print(1)
            elif dx3 < 0 and threshold2 <= y <= threshold1:
                print(1)
            else:
                print(0)
        else:
            print(0)
    elif dx3 == 0:
        y = dy1 * (x3 - x1) + dx1 * y1
        threshold1 = min(y3, y4) * dx1
        threshold2 = max(y3, y4) * dx1
        if min(x1, x2) <= x3 <= max(x1, x2):
            if dx1 > 0 and threshold1 <= y <= threshold2:
                print(1)
            elif dx1 < 0 and threshold2 <= y <= threshold1:
                print(1)
            else:
                print(0)
        else:
            print(0)
    else:
        x = (x1 * dx3 * dy1 - x3 * dx1 * dy3 + (dx1 * dx3) * (y3 - y1))
        threshold1 = max(min(x1, x2), min(x3, x4)) * (dx3 * dy1 - dx1 * dy3)
        threshold2 = min(max(x1, x2), max(x3, x4)) * (dx3 * dy1 - dx1 * dy3)

        if dx3 * dy1 > dx1 * dy3 and threshold1 <= x <= threshold2:
            print(1)
        elif dx3 * dy1 < dx1 * dy3 and threshold2 <= x <= threshold1:
            print(1)
        else:
            print(0)
