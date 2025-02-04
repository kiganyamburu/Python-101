msg =  "my name is peter mburu"
print(msg.replace("peter", "john"))

# string are immutable

msg1 = msg.replace("peter", "Alexander")
print(msg1)


print("peter" in msg)


name = "TERRY"
color = "Red"
msg2 = '[' + name + '] loves the color ' + color + ' ! '
msg3 = f'[{name.capitalize()}] loves the color {color.lower()} !'
print(msg2)
print(msg3)