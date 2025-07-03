def flatten(lst):
    if not lst:
        return []
    first = lst[0]
    rest = lst[1:]
    if isinstance(first, list):
        return flatten(first) + flatten(rest)
    else:
        return [first] + flatten(rest)

#print(flatten([[1, 2], 3, [[4], [5, 6]], 7]))

def count_nested_elements(lst, counter=0):
    """
    Counts all integers in a nested list structure.
    count_nested_elements([1, [2, [3, 4]], 5]) → 5
    """
    if not lst:
        return 0
    first = lst[0]
    rest = lst[1:]
    if isinstance(first, list):
        return count_nested_elements(first) + count_nested_elements(rest)
    else:
        return 1 + count_nested_elements(rest)

#print(count_nested_elements([1, [2, [3, 4]], 5], counter=0))

def flatten_to_list(lst, result=None, depth=0):
    indent = "  " * depth

    if result is None:
        result = []
        print(f"{indent}Creating new result list")

    print(f"{indent}Input list: {lst}")

    if not lst:
        print(f"{indent}Reached empty list, returning: {result}")
        return result

    first = lst[0]
    rest = lst[1:]

    if isinstance(first, list):
        print(f"{indent}Found list: {first} → Recursing into it")
        flatten_to_list(first, result, depth + 1)  # ❗No += here
    else:
        print(f"{indent}Found int: {first} → Appending to result")
        result.append(first)

    print(f"{indent}Done with: {first}, result so far: {result}")
    return flatten_to_list(rest, result, depth)

flatten_to_list([1, 2, [[3, 4]], [5, 6]])