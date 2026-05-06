numbers = [23,2,14,54,35,21,85,11,24,26]

print(list(map(lambda x: x**2, numbers)))

print(list(filter(lambda x: x%3 == 0, numbers)))

print(list(sorted(numbers, key=lambda x: x, reverse=True)))

#pyMiss1