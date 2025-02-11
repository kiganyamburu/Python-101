def calculator(num1, num2, mode):
    if mode == "+":
        return num1 + num2
    elif mode == "-":
        return num1 - num2
    elif mode == "/":
        if num2 / 0:
            return "Error: Divisible by zero"
        return num1 / num2
    elif mode == "*":
        return num1 * num2
    elif mode == "c2f":
        return (num1 * 9/5) + 32
    else:
        return "Invalid mode"
    
    num1 = float(input("Enter num1: "))
    num2 = float(input("Enter num2: "))
    mode = input("Enter the operation(+, -, *, /, c2f): ")
    
    result = calculator(num1, num2, mode)
    print("Result:", result)
    






# Create a calculator which handles +,-,*,/ and outputs answer based on the mode/ operator used
# Hint: use 3 separate inputs 
# Bonus: Extend functionality with extra mode so it also does celsius to fahrenheit conversion
# formula is: temp in C*9/5 + 32 = temp in f
