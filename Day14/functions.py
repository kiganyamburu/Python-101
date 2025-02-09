# Functions in programming are reusable blocks of code that perform a specific task. They help organize code, make it more readable, and avoid repetition.
# always declare function before using them.
# above where you are going to use them.
# A parameter in function is something like a variable 

def greeting(name, age = "28"):
    print(f"Hello {name}, your are {age}!")
    

name = input("Enter your name: ")   
greeting(name, "32")      
greeting("judith")      