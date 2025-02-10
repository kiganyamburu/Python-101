def calc():
    temp_cel = int(input("Enter the temperature in celcius: "))
    temp_fer = int(input("Enter the temperature in fer: "))
    convert_from_cel_to_fer = temp_cel * 9/5 + 32
    print(convert_from_cel_to_fer)
calc()
    
    
    
    
    
    
    
# Bonus: Extend functionality with extra mode so it also does celsius to fahrenheit conversion
# formula is: temp in C*9/5 + 32 = temp in 