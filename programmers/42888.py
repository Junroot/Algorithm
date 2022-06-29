def solution(record):
    nicknames = dict()
    for r in record:
        r = r.split()
        if r[0] == "Enter" or r[0] == "Change":
            nicknames[r[1]] = r[2]

    answer = []
    for r in record:
        r = r.split()
        if r[0] == "Enter":
            answer.append("{}님이 들어왔습니다.".format(nicknames[r[1]]))
        elif r[0] == "Leave":
            answer.append("{}님이 나갔습니다.".format(nicknames[r[1]]))
    return answer
