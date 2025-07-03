temps = [73, 74, 75, 71, 69, 72, 76, 73]

def temp(array: list[int]) -> list:
    n = len(array)
    stack = []
    result = [0] * n

    for i in range(n):
        while stack and array[i] > array[stack[-1]]:
            v = stack.pop()
            result[v] = i - v
        stack.append(i)


    return result

print(temp(temps))

