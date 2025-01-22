# 1 From the sting "Welcome to Python 101: Strings", extract tex and create/print a new string that says *"1 Welcome RIng to Tyler" *Every first letter in a word should be capitalized(title format) 
# 2. Print the same string backwards 


msg = "Welcome to Python 101: Strings"
new_msg = msg[0:7] + ' ' + msg[25:30]+' ' + msg[8:10]+' ' + msg[8] + msg[12] + msg[2] + msg[1] + msg[25]
print(new_msg.title())
print(new_msg[::-1])
