def num_days(month):

    if (
        month == "jan"
        or month == "mar"
        or month == "may"
        or month == "may"
        or month == "jul"
        or month == "nov"
        or month == "dec"
        or month == "aug"
    ):
        print(f"number of days in {month} is 31")

    elif month == "apr" or month == "jun" or month == "sep" or month == "nov":
        print(f"number of days in,{month},is,30")

    else:
        print(f"number of days in {month} is 28")


num_days("feb")
# optimize/shorten the code in the function
# try to reduce the number of conditionals
