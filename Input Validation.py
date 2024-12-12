def validate_input(input_value):
    if not input_value.isdigit():
        raise ValueError("Input must be a number")
    if int(input_value) < 0:
        raise ValueError("Input must be a positive number")
    return int(input_value)

try:
    user_input = input("Enter a positive number: ")
    validated_input = validate_input(user_input)
    print(f"Validated input: {validated_input}")
except ValueError as e:
    print(f"Error: {e}")
