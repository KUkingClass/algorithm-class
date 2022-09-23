from math import ceil


def solution(fees, records):
    default_time, default_charge, unit_time, unit_charge = fees
    parking = {}
    for record in records:
        time, car_num, mode = record.split()
        cur_status = parking.get(car_num, ["", 0, 0])
        hour, minute = map(int, time.split(":"))
        minute = 60 * hour + minute

        cur_status[0] = mode
        if mode == "IN":
            cur_status[2] = minute
        else:
            cur_status[1] += minute - cur_status[2]

        parking[car_num] = cur_status

    for key, val in parking.items():
        if val[0] == "IN":
            val[1] += 23 * 60 + 59 - val[2]

        parking[key] = default_charge + ceil(max(0, (val[1] - default_time)) / unit_time) * unit_charge

    return list(zip(*sorted(parking.items())))[1]


if __name__ == '__main__':
    fees = [180, 5000, 10, 600]
    records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
    print(solution(fees, records))
