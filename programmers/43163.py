from collections import deque


def diff(word1, word2):
    result = abs(len(word1) - len(word2))
    for i in range(min(len(word1), len(word2))):
        if word1[i] != word2[i]:
            result += 1
    return result


def solution(begin, target, words):
    words.append(begin)
    dictionary = {}
    visited = {}
    for word in words:
        dictionary[word] = []
        visited[word] = False
        for key in dictionary.keys():
            if diff(key, word) == 1:
                dictionary[word].append(key)
                dictionary[key].append(word)

    queue = deque([(begin, 0)])

    while queue:
        word = queue.popleft()
        visited[word[0]] = True
        if word[0] == target:
            return word[1]
        if all(visited.values()):
            return 0
        values = dictionary[word[0]]
        for value in values:
            queue.append((value, word[1] + 1))


print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))
