class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        i = 0
        while i < len(position):
            x = position[i]
            v = speed[i]
            cars.append([x, v])
            i += 1
        cars = sorted(cars, key = lambda x: x[0], reverse = True)
        arrival_times = []
        for car in cars:
            arrival_time = (target - car[0])/car[1]
            arrival_times.append(arrival_time)
            
        i = 0
        count = 0
        tmp = 0
        while i < len(arrival_times):
            if i == 0:
                tmp = arrival_times[i]
                count += 1
                i += 1
                continue
            else:
                if tmp < arrival_times[i]:
                    tmp = arrival_times[i]
                    count += 1
            i += 1
        return count 