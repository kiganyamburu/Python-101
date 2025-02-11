def calc(num1, num2, mode):
    num1 = 3
    num2 = 3
    mode = "+", "-", "/", "*", "c2f"
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
    
    num1 = float(input("Enter num1" ))
    num1 = float(input("Enter num2" ))
    num = float(input("Enter num2" ))
    
calc(3, 3, "+")







# Create a calculator which handles +,-,*,/ and outputs answer based on the mode/ operator used
# Hint: use 3 separate inputs 
# Bonus: Extend functionality with extra mode so it also does celsius to fahrenheit conversion
# formula is: temp in C*9/5 + 32 = temp in f
