def swap(a,b,arr):
    if a != b:
        arr[a], arr[b] = arr[b], arr[a]

def partition(elements, start, end):
    pivot_i = start
    pivot = elements[pivot_i]

    while start < end:
        while start < len(elements) and elements[start] <= pivot:
            start += 1
        while elements[end] > pivot:
            end -= 1
        if start < end:
            swap(start, end, elements)
    swap(pivot_i, end, elements)
    return end

def quick_sort(elements,start,end):
    if start < end:
        pi = partition(elements,start, end)
        quick_sort(elements, start, pi-1)
        quick_sort(elements,pi+1, end)
    return elements


a = [11,9,29,7,2,15,28]
print(quick_sort(a,0, len(a)-1))