def function_with_uncommon_error(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero")
        return None  #Or raise a custom exception
    except TypeError:
        print("Error: Invalid type for operands")
        return None #Or raise a custom exception
    else:
        return result

# Example usage
print(function_with_uncommon_error(10, 2))  # Output: 5.0
print(function_with_uncommon_error(10, 0))  # Output: Error: Division by zero; None
print(function_with_uncommon_error(10, "hello")) # Output: Error: Invalid type for operands; None