n = int(input())
students = [input().split() for _ in range(n)]

students.sort(key=lambda x: (x[1]))

for student in students:
    print(student[0], end=" ")
