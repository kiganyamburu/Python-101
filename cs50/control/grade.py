grade = input("Enter your grade: ").strip()
if "70" >=  grade <= "100":
    print("1st class")
elif "60" <= grade < "70":
    print("2nd class upper")
elif "50" <= grade < "60":
    print("2nd class lower")
elif "40" <= grade < "50":
    print("Pass")
else:
    print("Fail")