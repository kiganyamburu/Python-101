print("Lambdas exercise")


def f(x): return x + 5
# f = lambda x: x + 5
print(f(2))



def strip_spaces(str):
    return "str".join(str.split(" "))

strip_spaces1 = lambda str:" ".join(str.split(""))
print(strip_spaces("monty python flaying circus"))