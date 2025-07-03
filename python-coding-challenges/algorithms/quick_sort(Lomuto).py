def swap(a,b,arr):
    if a != b:
        arr[a], arr[b] = arr[b], arr[a]

def partition(elements, start, end):
    pivot = elements[end]
    i = start
    for j in range(start, end):
        if elements[j] <= pivot:
            print(f'swapinng {elements[j]} and  {elements[i]}')
            swap(j,i,elements)
            i += 1
            print(f'elements= {elements}, i= {i}')
    swap(i, end, elements)

    return i


def quick_sort(elements, start, end):
    if len(elements)== 1:
        return
    if start < end:
        pi = partition(elements, start, end)
        quick_sort(elements, start, pi-1)
        quick_sort(elements, pi+1, end)


    return elements

a = [4,5,6,89,2,44,34,78,9,0,11]
b = [12,13,15,17,18,19,11]
print(quick_sort(a, 0, len(a)-1))