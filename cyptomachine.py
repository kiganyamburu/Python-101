print("Project - crypto")
def enigma_light():
# create keys string
    keys ="abcdefghijklmnopqrstuvwxyz"
# autogenerate the values string by offsetting original string
    values = keys[-1] + keys[0:-1]
    # print(keys)
    # print(values)
# create two dictionaries
    dict_e = dict(zip(keys,values))
    dict_d = dict(zip(values, keys))
# of create 1 and then flip
    dict_e = dict(zip(keys, values))
    dict_d = {value:key for key, value in dict_e.items()}
# user input "the message" and mode 
    msg = input("Enter your secrete message quietly: ")
    mode = input("crypto mode:encode (e) or decode (d): ")
# return result
    if mode == "e":
        new_msg = "".join([dict_e[letter] for letter in msg])
    elif mode == "d":
        new_msg = "".join([dict_d[letter] for letter in msg]) 
    return new_msg
    
# clean and beautify the code 

print(enigma_light())
