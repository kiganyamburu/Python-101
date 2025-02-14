#It’s...not really an adventure game...#Ver 1.0
#Your village is being attacked by 'a germanic tribe' and you need to run to the stores and get the right things to save your village, and probably some good looking girl or boy you want to marry. All prices in gold pieces excl. VAT... chop chop!! ze german are coming!
#The code should allow you to get 1 thing from each store and each item you get should be removed from the store inventory, then do same for next store...
# one way to buy by typing the key 'newt' in an input box...or something
# at end you should print the 'items' you have taken..in this version you don't have to pay for stuff or add it up
#ver 1.2 add ability to exit a store without buying and go to next by typing 'exit', and to exit if a non-existant item is bought(typed)
#Add purse with 1000 gold pieces and payment for the items during or at end of code and show a message about total cost and how much gold you have left
#ver 1.4 random bug fix, ' browser compatibility', refactoring code... basically being lazy ..stop scrolling TikTok/Facebook! ;-)
#Ver 1.5 print inventory before and after purchases as one department_store of stuff(combine inventories from all stores into one...pretend Big Biz bought all the local stores, and want constant reporting for inventory management...)
# as in all games there is a special way to do this that actually makes money and solves the problem...can you find 'them'? Do you know why? May require knowledge of actual python 'lore'

#create stores
stores = [
    {'name': 'Freelancing Shop', 'brian': 70, 'black knight': 20, 'biccus diccus': 100, 'grim reaper': 500, 'minstrel': -15},
    {'name': 'Antique Shop', 'french castle': 400, 'wooden grail': 3, 'scythe': 150, 'catapult': 75, 'german joke': 5},
    {'name': 'Pet Shop', 'blue parrot': 10, 'white rabbit': 5, 'newt': 2}
]

gold = 1000  # Player's starting gold
inventory = []  # Player's collected items

def print_inventory():
    """Prints the current inventory of all stores combined."""
    print("\nCurrent Store Inventory:")
    department_store = {}
    for store in stores:
        for item, price in store.items():
            if item != 'name':
                department_store[item] = department_store.get(item, 0) + 1
    for item, count in department_store.items():
        print(f"{item}: {count} left")

def shopping():
    global gold
    print_inventory()
    
    for store in stores:
        print(f"\nYou have entered {store['name']}. You have {gold} gold pieces.")
        while True:
            print("Available items:")
            for item, price in store.items():
                if item != 'name':
                    print(f"{item}: {price} gold")
            
            choice = input("What do you want to buy? (type 'exit' to leave): ").strip().lower()
            
            if choice == 'exit':
                break
            elif choice in store and store[choice] <= gold:
                gold -= store[choice]
                inventory.append(choice)
                del store[choice]  # Remove item from store
                print(f"You bought {choice}! Remaining gold: {gold}")
                break  # Move to the next store
            else:
                print("Invalid choice or not enough gold! Moving to the next store...")
                break  # Move to the next store if item doesn't exist or can't be bought

    print("\nShopping completed!")
    print(f"Items collected: {inventory}")
    print(f"Gold left: {gold}")
    print_inventory()

    # Special way to profit 😉
    if 'minstrel' in inventory:
        print("\nThe minstrel starts singing... and people throw money at you! You gain 50 gold!")
        gold += 50
        print(f"New gold balance: {gold}")

shopping()





