is_raining = False
is_cold = False
print("Good morning")
if is_raining and is_cold:
    print("Bring umbrella and jacket")
elif is_raining and not(is_cold):
    print("Bring umbrella")
elif not(is_raining and is_cold):
    print("Bring jacker")
else:
    print("Umbrella optional")