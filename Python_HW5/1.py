def odd_nums(stop_value, step=2):
    current = 1
    while current <= stop_value:
        yield current
        current += step


odd_to_15 = odd_nums(15)
for i in odd_to_15:
    print(i)
for i in odd_to_15:
    print(i)
