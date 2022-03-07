def time_to_ms(time):
    hour, minute, second = time.split(":")
    millisecond = "".join(second.split("."))

    return (int(hour) * 60 + int(minute)) * 60 * 1000 + int(millisecond)


def second_to_ms(second):
    result = 0
    digit_count = 0
    for c in second:
        if "0" <= c <= "9":
            result = result * 10 + int(c)
            digit_count += 1
    while digit_count < 4:
        result *= 10
        digit_count += 1
    return result


def solution(lines):
    processing_times = []
    for line in lines:
        date, response_time, processing_seconds = line.split()

        response_ms = time_to_ms(response_time)
        processing_ms = second_to_ms(processing_seconds)
        processing_times.append((response_ms - processing_ms + 1, response_ms))

    result = 0
    for start_line_index, (request_ms, response_ms) in enumerate(processing_times):
        count = 1
        for i in range(start_line_index + 1, len(processing_times)):
            if processing_times[i][0] < response_ms + 1000:
                count += 1
        result = max(result, count)

    return result
