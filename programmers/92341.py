from collections import defaultdict


def solution(fees, records):
    default_time, default_fee, time_unit, fee_unit = fees[0], fees[1], fees[2], fees[3]

    total_minutes = defaultdict(int)
    entrance_records = dict()
    max_time = 23 * 60 + 59

    for record in records:
        time, car_id, entrance = record.split(" ")
        hour, minute = map(int, time.split(":"))
        time_minute = hour * 60 + minute
        car_id = int(car_id)
        if entrance[0] == "I":
            entrance_records[car_id] = time_minute
        else:
            total_minutes[car_id] += time_minute - entrance_records[car_id]
            del entrance_records[car_id]

    for car_id in entrance_records.keys():
        total_minutes[car_id] += max_time - entrance_records[car_id]

    answer = []
    for car_id in sorted(total_minutes.keys()):
        total_minute = total_minutes[car_id]
        if total_minute <= default_time:
            answer.append(default_fee)
        else:
            answer.append(default_fee + (total_minute - default_time + time_unit - 1) // time_unit * fee_unit)
    return answer

