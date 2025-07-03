import time
def time_it(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f'{func.__name__} took {(end - start) * 1000:.4f} ms')
        return result
    return wrapper
@time_it
def binary_search(lst, target):
    left = 0
    right = len(lst) - 1
    num_of_iter = 0
    while left <= right:
        num_of_iter += 1
        middle = (left + right) // 2
        mid_number = lst[middle]
        if mid_number == target:
            print(f'{num_of_iter}')
            l = []
            l.append(middle)
            r_middle = middle
            l_middle = middle
            while True:
                moved = False

                if r_middle + 1 < len(lst) and lst[r_middle + 1] == lst[middle]:
                    r_middle += 1
                    l.append(r_middle)
                    moved = True

                if l_middle - 1 >= 0 and lst[l_middle - 1] == lst[middle]:
                    l_middle -= 1
                    l.append(l_middle)
                    moved = True

                if not moved:
                    return sorted(l)

        if mid_number < target:
            left = middle + 1
        else:
            right = middle - 1
    return -1
@time_it
def bisearch_rec(lst,target, left=0, right=None, call=0):

    if right is None:
        right = len(lst) - 1

    if left > right:
        return - 1, call

    middle = (left + right) // 2
    if lst[middle] == target:
        return middle, call
    elif lst[middle] < target:
        return bisearch_rec(lst,target, left=middle+1, right=right,call=call+1)
    else:
        return bisearch_rec(lst,target, left=left, right=middle-1,call=call+1)



a = [1,2,3,4,5,6,7,8,9,9,9,9,10,11,12,13,14,15]

print(binary_search(a,9))
print(bisearch_rec(a,22))