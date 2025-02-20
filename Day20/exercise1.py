print("Lambdas exercise")


def f(x): return x + 5
# f = lambda x: x + 5
print(f(2))



def strip_spaces(str):
    return "str".join(str.split(" "))

strip_spaces1 = lambda str:" ".join(str.split(""))
print(strip_spaces("monty python flaying circus"))



# list with no duplicates
def join_list_no_duplicates(list_a, list_b):
    return list(set(list_a + list_b))
list_a = [1,2,3,4]
list_b = [3,4,5,6, 7]
join_list_no_duplicates1  = lambda list_a, list_b: list(set(list_a + list_b))
print(join_list_no_duplicates(list_a, list_b))