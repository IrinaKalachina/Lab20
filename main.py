def add_two_numbers(a, b):
    return a + b

def multiply_two_numbers(a, b):
    return a * b

def calculator(operation, a, b):
    if operation == 'addition':
        return add_two_numbers(a, b)
    elif operation == 'multiplication':
        return multiply_two_numbers(a, b)
    else:
        return None


result = calculator('addition', 4, 5)
print(result)

result = calculator('multiplication', 4, 5)
print(result)