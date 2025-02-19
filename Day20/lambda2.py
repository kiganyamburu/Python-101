monty_python = ["John Marwood Cleese", "Eric Idle", "Michael Edward Palin", "Terrence Vance Gilliam", 'Terry Graham Perry Jones', 'Graham Arthur Chapman']
def sort_name(name):
    return name(name)
monty_python.sort(key = lambda name:name.split(" ")[-1])
print(monty_python)
monty_python.sort(key= sort_name)
print(monty_python)