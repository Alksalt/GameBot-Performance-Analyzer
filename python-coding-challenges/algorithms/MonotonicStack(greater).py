a = [1,-2, 2,2, 4,-5,8,10, -8, 11,2,3,4,5]

def next_greter_value(array: list[int]) -> list:
    n = len(array)
    stack = [0]
    result = [-1] * n
    for i in range(n):
        while stack and array[i] > array[stack[-1]]:
            result[stack.pop()] = array[i]
        stack.append(i)
    return result

print(next_greter_value(a))