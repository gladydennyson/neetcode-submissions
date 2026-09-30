class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        cars = sorted(zip(position, speed), reverse=True)

        fleets = 0
        # previous_time = 0

        # for pos, spd in cars:
        #     time = (target - pos) / spd

        #     if time > previous_time:
        #         fleets += 1
        #         previous_time = time

        # return fleets

        # sol 2

        stack = []

        for pos, speed in cars:
            time = (target - pos) / speed
            if not stack or time > stack[-1]:
                stack.append(time)
                fleets+=1
            
        return(len(stack))

