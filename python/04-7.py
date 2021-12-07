content = None

with open("test.txt", "r") as f:
    content = f.read()

content = content.replace("java", "python")

with open("test.txt", "w") as f2:
    f2.write(content)
