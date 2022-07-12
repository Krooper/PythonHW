from time import perf_counter
from itertools import islice
from random import randint

src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
# Скорость лучше проверять на большом списке:
# src = [randint(0, 100) for i in range(1000)]

# Стандартный метод решения с созданием нового списка:
start = perf_counter()
result = []
i = 1
while i < len(src):
    if src[i] > src[i-1]:
        result.append(src[i])
    i += 1
print(result)
print(perf_counter() - start)



# Правктически то же самое, но с использованием множества:
start_speed = perf_counter()
result_set = set()
i = 1
while i < len(src):
    if src[i] > src[i-1]:
        result_set.add(src[i])
    else:
        result_set.discard(src[i])
    i += 1
print(result_set)
print(perf_counter() - start_speed)
# Время выполнения чуть быстрее, чем стандартным методом

# Для оптимизации памяти делаем через генераторное выражение
# учитывая, что первый элемент брать не надо - добавляем условие j > 0:
result_gen = (src[j] for j in range(len(src)) if j > 0 and src[j] > src[j-1])

# Можно с помощью вызова next():
# start_next = perf_counter()
# for j in range (6):
#     print(next(result_gen))
# print(perf_counter() - start_next)


# Но лучше с помощью islice() - это быстрее:
start_islice = perf_counter()
print(*islice(result_gen, len(src)-1))
print(perf_counter() - start_islice)
# Время выполнения всегда разное, но не более 0.00023770000188960694
# Это значительно быстрее чем через next(), если нам нужно получить сразу все значения
# Пусть такой способ решения всё еще дольше, чем стандартный, он значительно экономит паямть
# (генератор занимает 1 строчку)



