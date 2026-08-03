class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # while any of the position < target, pos[i] + target[i].
        # if at any point, any of the position = other position,
        # combine them and pass both as 1 carFleet witht he speed
        # being the front one's

        carSpeed = []
        for i in range(len(position)):
            carSpeed.append((position[i], speed[i]))

        carSpeed = sorted(carSpeed, reverse=True)
        # print(carSpeed)

        stacks = []

        for i in range(len(carSpeed)):
            time = (target - carSpeed[i][0]) / carSpeed[i][1]
            if not stacks:
                stacks.append(time)
            if stacks and time > stacks[-1]:
                stacks.append(time)            

        return len(stacks)
        