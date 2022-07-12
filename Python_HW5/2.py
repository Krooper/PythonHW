nums = (num for num in range(1, 15 + 1, 2))
# Докажем, что создали именно генератор, выведя тип nums
print(type(nums), *nums)
