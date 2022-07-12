from itertools import islice
from time import perf_counter
from random import randint

# src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# Скорость лучше проверять на большом списке:
src = [randint(0, 100) for i in range(1000)]

# Решим стандартным способом
start_slow = perf_counter()
unique_nums_slow = [num for num in src if src.count(num) == 1]
print(unique_nums_slow)
print(perf_counter() - start_slow)

# Решим с помощью множеств:
start_set = perf_counter()
unique_nums = set()
tmp = set()
for num in src:
    if num not in tmp:
        unique_nums.add(num)
    else:
        unique_nums.discard(num)
    tmp.add(num)

# Т.к. вывод уникальных чисел нужен по порядку, то понадобится использование List Comprehension:
unique_nums_ord = [num for num in src if num in unique_nums]
print(unique_nums_ord)
print(perf_counter() - start_set)
# В итоге скорость при большом списке в 10 раз (а то и больше) выше по сравнению с решением "в лоб"



# Можно решить с помощью генератора и ф-ии islice(), что сэкномит память,
# но не время (по сравнению со стандартным методом):
start_islice = perf_counter()
unique_nums_gen = (num for num in src if src.count(num) == 1)
print(*islice(unique_nums_gen, len(src)-1))
print(perf_counter() - start_islice)
