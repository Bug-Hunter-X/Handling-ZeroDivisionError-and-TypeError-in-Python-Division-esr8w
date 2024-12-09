def function_with_uncommon_error(a, b):
    try:
        if not isinstance(a,(int,float)) or not isinstance(b,(int,float)):
            raise TypeError("Operands must be numbers")
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero")
        return None 
    except TypeError as e:
        print(f"Error: {e}")
        return None
    else:
        return result

# Example usage
print(function_with_uncommon_error(10, 2))  # Output: 5.0
print(function_with_uncommon_error(10, 0))  # Output: Error: Division by zero; None
print(function_with_uncommon_error(10, "hello")) # Output: Error: Operands must be numbers; None
print(function_with_uncommon_error("hello",2)) # Output: Error: Operands must be numbers; None