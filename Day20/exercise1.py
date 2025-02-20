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



# complete
#Complete the function so it returns a function
#def create_quad_func(a,b,c):
#    '''return function f(x) = ax^2 + bx + c'''
#    return lambda x:
#f = create_quad_func(2,4,6)
#g = 
#print(f(2))
#print(g(2))
def create_quad_func(a, b, c):
    '''return function f(x) = ax^2 + bx + c'''
    return lambda x: a*x**2 + b*x + c

f = create_quad_func(2, 4, 6)
g = create_quad_func(1, -3, 2)  # Example of a different quadratic

print(f(2))  # Output: 22 (2*2^2 + 4*2 + 6)
print(g(2))  # Output: 0 (1*2^2 - 3*2 + 2)


