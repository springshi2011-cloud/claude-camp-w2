#safe calculator

def safe_calculator():
    while True:

#get 1st number from user and handle non-numeric input
        num1_input = input("Enter the first number or quit: ").strip()
        if num1_input.lower() == 'quit':
            print("Goodbye!")
            break
        try:
            num1 = float(num1_input)
        except ValueError:
            print("Error: Invalid input. Please enter a numeric value for the first number.")
            continue

#get operator and 2nd number from user and handle non-numeric input and division by zero    
        operator = input("Enter an operator (+, -, *, /) or quit: ").strip()
        if operator.lower() == 'quit':
            print("Goodbye!")
            break

        num2_input = input("Enter the second number or quit: ").strip()
        if num2_input.lower() == 'quit':
            print("Goodbye!")
            break
        try:
            num2 = float(num2_input)
        except ValueError:
            print("Error: Invalid input. Please enter a numeric value for the second number.")
            continue

#calculate the result based on the operator and handle division by zero

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
                continue
            else:
                result = num1 / num2
        else:
            print("Error: Invalid operator. Please use +, -, *, or /.")
            continue

        print(f"The result of {num1} {operator} {num2} is: {result}")
  
if __name__ == "__main__":    
    safe_calculator()   