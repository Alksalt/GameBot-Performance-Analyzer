def buble_sort(lst:list) -> list:
    n = len(lst)
    for pass_el in range(n-1):
        swapped = False
        for i in range(n-1 - pass_el):
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
                swapped = True
        if not swapped:
            break

    return lst

def buble_sort_for_dict(lst:list) -> list:
    n = len(lst)
    for pass_el in range(n-1):
        swapped = False
        for i in range(n-1 - pass_el):
            if lst[i]['transaction_amount'] > lst[i+1]['transaction_amount']:
                lst[i], lst[i+1] = lst[i+1], lst[i]
                swapped = True
        if not swapped:
            break

    return lst

elements = [
    {'name': 'alice',   'transaction_amount': 750,  'device': 'iphone-11'},
    {'name': 'bob',     'transaction_amount': 150,  'device': 'samsung S10'},
    {'name': 'carol',   'transaction_amount': 1200, 'device': 'google pixel'},
    {'name': 'dan',     'transaction_amount': 90,   'device': 'vivo'},
    {'name': 'eve',     'transaction_amount': 330,  'device': 'iphone-8'},
    {'name': 'frank',   'transaction_amount': 500,  'device': 'samsung S22'},
    {'name': 'grace',   'transaction_amount': 600,  'device': 'iphone-12'},
    {'name': 'heidi',   'transaction_amount': 110,  'device': 'xiaomi'},
    {'name': 'ivan',    'transaction_amount': 210,  'device': 'nokia'},
    {'name': 'judy',    'transaction_amount': 950,  'device': 'oneplus'},
    {'name': 'mallory', 'transaction_amount': 300,  'device': 'oppo'},
    {'name': 'trent',   'transaction_amount': 870,  'device': 'pixel 7'},
]
#print(buble_sort([44,76,1,99,209,21,11,14,67,156,23]))
print(buble_sort_for_dict(elements))