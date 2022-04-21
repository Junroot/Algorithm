room_count = int(input())
rooms = list(map(int, input().split()))
capacity_of_main_examiner, capacity_of_sub_examiner = map(int, input().split())

examiner_count = 0

for student_count in rooms:
    examiner_count += 1
    if student_count > capacity_of_main_examiner:
        examiner_count += (student_count - capacity_of_main_examiner - 1) // capacity_of_sub_examiner + 1

print(examiner_count)
