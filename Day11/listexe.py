sales_week1 = [7,3,42,19,15,35,9]
sales_week2 = [12,4,26,10,7,28]

sales = []
new_day = input("Enter #of Lemonade for new day: ")
sales_week2.append(int(new_day))
# sales.extend(sales_week1)
# sales.extend(sales_week2)
sales = sales_week1 + sales_week2
sales.sort()
worst_day_prof = sales[0] * 1.5
best_day_prof = sales[0] * 1.5
print(f"worst day profit:${worst_day_prof}")
print(f"best day profit:${best_day_prof}")
print(f"worst day profit:${worst_day_prof + best_day_prof}")