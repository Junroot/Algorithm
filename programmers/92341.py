class Record:
    def __init__(self):
        self.time_in = None
        self.total_time = 0

    def enter(self, time_in):
        self.time_in = time_in

    def exit(self, time_out):
        self.total_time += time_out - self.time_in
        self.time_in = None

    def get_total_time(self):
        if self.time_in is not None:
            return self.total_time + (23 * 60 + 59 - self.time_in)
        return self.total_time


def solution(fees, records):
    base_minutes, base_fee, unit_time, unit_fee = fees[0], fees[1], fees[2], fees[3]
    cars = dict()

    for record in records:
        time, car_number, entrance = record.split()

        hour, minute = time.split(":")
        time = int(hour) * 60 + int(minute)

        if entrance == "IN":
            if car_number not in cars:
                cars[car_number] = Record()
            cars[car_number].enter(time)
        else:
            cars[car_number].exit(time)

    answer = []
    for car_number in sorted(cars.keys()):
        fee = base_fee
        print(car_number, cars[car_number].get_total_time())
        extra_fee = ((cars[car_number].get_total_time() - 1 - base_minutes) // unit_time + 1) * unit_fee
        if extra_fee > 0:
            fee += extra_fee
        answer.append(fee)

    return answer


print(solution([180, 5000, 10, 600],
               ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN",
                "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))
