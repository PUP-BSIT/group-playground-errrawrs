# Example dictionary
numbers = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Dictionary comprehension with if-else condition
result = {key: ('even' if value % 2 == 0 else 'odd') for key, value in numbers.items()}

print(result)
