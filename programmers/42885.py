def solution(people, limit):
    answer = 0
    people.sort(reverse=True)
    front = 0
    back = len(people) - 1
    while back >= front:
        if people[front] + people[back] <= limit:
            back -= 1
        front += 1
        answer += 1
    return answer
