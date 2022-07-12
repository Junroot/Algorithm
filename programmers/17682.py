def parse(dartResult):
    results = []
    state = 0
    buffer = 0
    result = []
    for char in dartResult:
        if state == 0:
            if char.isdigit():
                buffer = buffer * 10 + int(char)
            else:
                result.append(buffer)
                if char == "S":
                    result.append(1)
                elif char == "D":
                    result.append(2)
                else:
                    result.append(3)
                buffer = 0
                state = 1
        else:
            if char.isdigit():
                result.append("")
                buffer = buffer * 10 + int(char)
            else:
                result.append(char)
            results.append(result)
            result = []
            state = 0
    if state == 1:
        result.append("")
        results.append(result)
    return results


def solution(dartResult):
    scores = []
    results = parse(dartResult)
    for result in results:
        scores.append(result[0] ** result[1])
        if result[2] == "*":
            if len(scores) == 1:
                scores[0] *= 2
            else:
                scores[-1] *= 2
                scores[-2] *= 2
        elif result[2] == "#":
            scores[-1] *= -1
    return sum(scores)

print(solution("1S2D*3T"))
