import sys

file_name = "memo.txt"
option = sys.argv[1]
content = sys.argv[2]

if option == "-a":
    with open(file_name, "a") as f:
        f.write(content + "\n")
elif option == "-v":
    with open(file_name, "r") as f:
        print(f.read())
