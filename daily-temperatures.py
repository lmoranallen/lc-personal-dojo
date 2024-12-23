
def dailyTemperatures(temperatures: list[int]) -> list[int]:
    stack = []
    _N = len(temperatures)
    result = [0] * _N


    for i in range(_N):
        while len(stack) and temperatures[stack[len(stack)-1]] < temperatures[i]:
            elem = stack.pop()
            result[elem] = i - elem
        
        stack.append(i)
    return result


print(dailyTemperatures([73,74,75,71,69,72,76,73]))
print(dailyTemperatures([30,40,50,60]))
print(dailyTemperatures([30,60,90]))



# Still don't completely understand the structure and patterns around monotonic stacks. 
# Link that provided the basic building blocks of said structure:
# https://leetcode.com/discuss/study-guide/2347639/A-comprehensive-guide-and-template-for-monotonic-stack-based-problems