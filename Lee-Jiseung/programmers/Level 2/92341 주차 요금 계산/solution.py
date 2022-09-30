import math

def solution(fees, records):
    answer = []
    parkingTimes = [0 for _ in range(10000)]
    startTimes = [-1 for _ in range(10000)]
    
    for record in records:
        info = record.split(' ')
        times = list(map(int, info[0].split(':')))
        time = times[0]*60 + times[1]
        num = int(info[1])
        
        if startTimes[num] >= 0:
            parkingTimes[num] += time - startTimes[num]
            startTimes[num] = -1
        else:
            startTimes[num] = time
        
    for i, startTime in enumerate(startTimes):
        if startTime >= 0:
            parkingTimes[i] += 23*60 + 59 - startTime
    
    for parkingTime in parkingTimes:
        if parkingTime == 0:
            continue
            
        if parkingTime <= fees[0]:
            answer.append(fees[1])
        else:
            answer.append(fees[1] + math.ceil((parkingTime - fees[0]) / fees[2]) * fees[3])
            
    return answer