from random import randint

numbers = [randint(0,13) for x in range(10)]
print(*numbers)
numbers.sort(key=lambda x: x**2)
print(*numbers)