from collections import Counter
def dif_betw_two_str(a,b):
    c_a = Counter(a)
    c_b = Counter(b)
    return list((c_b - c_a).keys())


def top_frequent_words(words,k):
    c = Counter(words)
    sorted_words = sorted(c.items(), key=lambda x: (-x[1], x[0]))
    result = [word for word, freq in sorted_words[:k]]
    return result


print(top_frequent_words(
    ["banana", "apple", "orange", "banana", "apple",
     "bad", "juice", "apple", ],
    2))