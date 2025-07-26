def next_greater_element(arr):
    n = len(arr)
    stack = []
    result = [-1] * n
    
    for i in range(n):
        while stack and arr[i] > arr[stack[-1]]:
            result[stack.pop()] = arr[i]
        
        stack.append(i)
    return result


"""
0 = in stack = 1
1 = [0]



"""
arr = [1, 4, 6, 3, 2, 7]
arr2 = [1, 2, 3, 4, 5, 6, 7]

print(next_greater_element(arr))