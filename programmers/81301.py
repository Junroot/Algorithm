number_dictionary = {
    "zero": "0",
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}


def solution(s):
    answer = ""
    word = ""
    for character in s:
        if "0" <= character <= "9":
            answer += character
        else:
            word += character
            if word in number_dictionary:
                answer += number_dictionary[word]
                word = ""
    return int(answer)
