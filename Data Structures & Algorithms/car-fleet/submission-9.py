class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        time = [0] * len(position)
        for i in range(len(time)):
            time[i] = (position[i], speed[i])

        time.sort(reverse=True)
        stack, res = [], 0

        for i in range(len(time)):
            time[i] = (target - time[i][0]) / time[i][1]

            if not stack:
                stack.append(time[i])
                res += 1
            elif stack[-1] >= time[i]:
                stack.append(time[i])
            else:
                while stack and stack[-1] < time[i]:
                    stack.pop()
                if not stack:
                    res += 1
                stack.append(time[i])

        return res
            

        


        