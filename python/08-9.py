with open("sample.txt", "r") as file:
    numbers = list(map(int, file.readlines()))
    total = sum(numbers)
    avg = total / len(numbers)

    with open("result.txt", "w") as file2:
        file2.write(",".join([str(total), str(avg)]))
