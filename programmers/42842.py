def solution(brown, yellow):
    row = round(((brown + 4) / 2 + ((brown + 4) ** 2 / 4 - 4 * (brown + yellow)) ** 0.5) / 2)
    column = round(((brown + 4) / 2 - ((brown + 4) ** 2 / 4 - 4 * (brown + yellow)) ** 0.5) / 2)
    return [row, column]
