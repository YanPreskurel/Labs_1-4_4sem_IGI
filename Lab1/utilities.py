def func_math_operation(first_number, second_number, operation):
    if operation == 'add':
        return float(first_number) + float(second_number)
    elif operation == 'sub':
        return float(first_number) - float(second_number)
    elif operation == 'mul':
        return float(first_number) * float(second_number)
    elif operation == 'div':
        return float(first_number) / float(second_number)
    else:
        return "Unknown operation"
