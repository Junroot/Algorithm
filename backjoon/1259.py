import sys


def is_palindrome(number):
    length = len(number)
    for i in range(length // 2):
        if number[i] != number[length - i - 1]:
            return False
    return True


while True:
    number = sys.stdin.readline().strip()
    if number == "0":
        break
    if is_palindrome(number):
        print("yes")
    else:
        print("no")