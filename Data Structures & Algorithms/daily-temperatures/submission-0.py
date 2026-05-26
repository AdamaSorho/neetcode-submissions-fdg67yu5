class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = [] # pair: temperature, index

        for i, temperature in enumerate(temperatures):
            while stack and temperature > stack[-1][0]:
                stackT, stackI = stack.pop()
                result[stackI] = i - stackI

            stack.append((temperature, i))

        return result
