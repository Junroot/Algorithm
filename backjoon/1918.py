infix = input()
result = ""

stack = []

for i in range(len(infix)):
    if "A" <= infix[i] <= "Z":
        result += infix[i]
    elif infix[i] == "+" or infix[i] == "-":
        while stack and stack[len(stack) - 1] != "(":
            result += stack.pop()
        stack.append(infix[i])
    elif infix[i] == "*" or infix[i] == "/":
        while stack and (stack[len(stack) - 1] == "*" or stack[len(stack) - 1] == "/"):
            result += stack.pop()
        stack.append(infix[i])
    elif infix[i] == "(":
        stack.append(infix[i])
    elif infix[i] == ")":
        while stack and stack[len(stack) - 1] != "(":
            result += stack.pop()
        stack.pop()

stack.reverse()
result += "".join(stack)

print(result)
