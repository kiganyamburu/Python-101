def greeting(name, age=28, color="red"):
 #Greets user with “name” from “input box” and “age”, if available, default age is used   
   print("Hello "  +  name.capitalize() + ", you will be " + str(age+1) +" next birthday!")
   print(f"Hello {name.capitalize()}, you will be {age+1} next birthday!")
   print(f"We hear you like the color {color.lower()}!")

greeting("brian", 27,"Blue")
