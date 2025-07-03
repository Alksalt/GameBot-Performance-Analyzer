import time
import random
def max_sum_array_of_k(array: list, k: int) -> (int, int):
    current_sum = sum(array[:k])
    max_sum = current_sum
    start_index = 0

    for i in range(k, len(array)):

        current_sum += array[i] - array[i - k]
        if current_sum > max_sum:
            max_sum = current_sum
            start_index = i

    return (start_index, max_sum)


a = [random.randint(0,9) for _ in range(1_000_000)]
k = 3
start = time.time()
index, max_sum = max_sum_array_of_k(a,k)
end = time.time()
print(f'time spent: {end-start:.6f}')
print(index, max_sum)
new_array = [a[i+index] for i in range(k)]
print(f'The array: {new_array}, sum: {max_sum}')
