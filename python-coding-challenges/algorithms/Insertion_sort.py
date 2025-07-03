def sort_arr(lst):
    for i in range(1, len(lst)):
        pointer = i-1
        current = lst[i]
        while pointer >= 0 and current < lst[pointer]:
            lst[pointer + 1] = lst[pointer]
            pointer -= 1
        lst[pointer+1] = current
    return lst



a = [22,28,11,12,7,3,45,56,31,1]
new = [11,22,28]
c = 11
l= sort_arr(a)
print(l)