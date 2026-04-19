class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort(reverse=True)

        stack = []
        last_time = 0
        count = 0
        for pos, spd in cars:
            time = (target - pos) / spd
            if time > last_time:
                count += 1
                last_time = time
            
        return count
        