def value_added_task(amount):
    tax = amount * 0.5
    total_amount = amount * 1.25
    return [amount, tax, total_amount]
price = value_added_task()
print(price, type(price))