def merge_sorted_lists(l1,l2):
    i1 = i2 = 0
    n1 = len(l1)
    n2 = len(l2)
    new_list = []
    while i1 < n1 and i2 < n2:

        if l1[i1] >= l2[i2]:
            new_list.append(l2[i2])
            i2 += 1
        else:
            new_list.append(l1[i1])
            i1 += 1

        if i1 == n1:
            new_list += l2[i2:]
        elif i2 == n2:
            new_list += l1[i1:]
    return new_list

def merge_rec(l1,l2,i1=0,i2=0,new_list=None):
    if new_list is None:
        new_list = []
    if i1 == len(l1):
        new_list += l2[i2:]
        return new_list
    elif i2 == len(l2):
        new_list += l1[i1:]
        return new_list

    if l1[i1] >= l2[i2]:
        new_list.append(l2[i2])
        i2 += 1
        return merge_rec(l1,l2,i1=i1,i2=i2,new_list=new_list)
    else:
        new_list.append(l1[i1])
        i1 += 1
        return merge_rec(l1, l2, i1=i1, i2=i2, new_list=new_list)

def merge_sort(lst):
    if len(lst) <= 1:
        return lst

    mid = len(lst) //2
    l1 = merge_sort(lst[:mid])
    l2 = merge_sort(lst[mid:])

    i1 = i2 = 0
    new_list = []
    while i1 < len(l1) and i2 < len(l2):

        if l1[i1] >= l2[i2]:
            new_list.append(l2[i2])
            i2 += 1
        else:
            new_list.append(l1[i1])
            i1 += 1

    new_list += l1[i1:]
    new_list += l2[i2:]

    return new_list


list1 = [1,4,7,10,11]
list2 = [5,7,9,10,15,18,20,45]
list3 = [44,6545,22,34,1,2,34,56,78,99]
l = [1,4, 5, 7,7, 9, 10,10,11]


print(merge_sorted_lists(list1,list2))
print(merge_rec(list1,list2))
print(merge_sort(list3))