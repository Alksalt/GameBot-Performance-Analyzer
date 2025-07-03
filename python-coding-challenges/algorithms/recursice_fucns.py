def recursive_f(people_before=3,sum=4):
    if not people_before:
        return sum
    return recursive_f( people_before - 1, sum + people_before)



def sum_in_list(lst, result=0):
    if not lst:
        return result
    return sum_in_list(lst[:-1], result + lst[-1])


def sum_in_list_two(lst, result=0, i=0):
    if len(lst) == i+1:
        return result
    return sum_in_list(lst, result + lst[i], i + 1)


def power(num=5, p=3, result=1):
    if not p:
        return result
    return power(num, p - 1, result*num)
#print(power())
def negative_power(num=2,p=-2,result=1):
    if not p:
        return 1/result
    return negative_power(num, p + 1, result*num)

#print(negative_power())

def power_full(num=5, p=3,result=1, x=0):
    if not x:
        x = p
    if x > 0 and not p:
        return result
    if x < 0 and not p:
        return 1/result
    if x > 0:
        return power_full(num, p - 1, result*num, x)
    elif x < 0:
        return power_full(num, p + 1, result*num, x)

print(power_full(2,2))


print(3//2)

