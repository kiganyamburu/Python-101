# 📱 Phone Number Formatter
#
# 1. Ask the user to enter a U.S. phone number in **any format**.
number = input("Enter a U.S. phone number: ")
# 2. Use .strip() to remove any leading/trailing spaces.
number = number.strip()
# 3. Replace common separators (-, (, ), .) with spaces.
number = number.replace("-", " ").replace("(", " ").replace(")", " ").replace(".", " ")
# 4. Use .split() to break into chunks, then .join() to merge the digits.
number = "".join(number.split())
# 5. Check if the cleaned number has **exactly 10 digits**.
if len(number) == 10 and number.isdigit():
    # 6. If yes, format it like this: (123) 456-7890
    formatted_number = f"({number[:3]}) {number[3:6]}-{number[6:]}"
    print("Formatted phone number:", formatted_number)
else:
    # 7. If not, print an error message: "Please enter exactly 10 digits."
    print("Please enter exactly 10 digits.")