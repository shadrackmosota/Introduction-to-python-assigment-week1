def perform_operation():
    # Get the two numbers
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    # Get the operation
    operation = input("Enter the operation (addition, subtraction, multiplication, division): ")

    # Perform the operation
    if operation == "addition":
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
    elif operation == "subtraction":
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
    elif operation == "multiplication":
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")
    elif operation == "division":
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Invalid operation. Please enter a valid operation (addition, subtraction, multiplication, or division).")