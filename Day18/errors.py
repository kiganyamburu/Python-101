try:
    num = int(input("Enter a number: "))
    print("30 divided by", num, "is:",30/num)
except ZeroDivisionError as err:
    print(err,"You cant divide by zero")
    
except ValueError as err:
    print("Bad value!")


except:
    print("Invalid input")
else:
    print("30 divided by", num, "is:", 30/num)    

print("** thank you for playing")

# try:
    # code you want to run
# except:
    # executed if error occurs
# else:
    # executed if  no error occurs
# finally:
    # always executed