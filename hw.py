



Apple=40.00
Banana=30.00
Fish=100.00
Bread=45.00
Milk=20.00
price=0.00

print("Apple: Php 40.00")
print("Banana: Php 30.00")
print("Fish: Php 100.00")
print("Bread: Php 45.00")
print("Milk: Php 20.00")

while True:
    choice=input('\nChoose an item: Apple, Banana, Fish, Bread, Milk\n')
    if choice == 'Apple':
        choice=input('Would you like to pick another order? y/n\n')
        if choice == 'y':
            choice=input('\nChoose an item: Apple, Banana, Fish, Bread, Milk\n')
        else:
            for cost in price:
                sum += cost
                break
                print("Total cost: Php",sum)
                print(" ")
    elif choice == 'Banana':
        choice=input('Would you like to pick another order? y/n\n')
        if choice == 'y':
            choice=input('\nChoose an item: Apple, Banana, Fish, Bread, Milk\n')
        else:
            for cost in price:
                sum += cost
                break
                print("Total cost: Php",sum)
                print(" ")
    elif choice == 'Fish':
        choice=input('Would you like to pick another order? y/n\n')
        if choice == 'y':
            choice=input('\nChoose an item: Apple, Banana, Fish, Bread, Milk\n')
        else:
            for cost in price:
                sum += cost
                break
                print("Total cost: Php",sum)
                print(" ")
    elif choice == 'Bread':
        choice=input('Would you like to pick another order? y/n\n')
        if choice == 'y':
            choice=input('\nChoose an item: Apple, Banana, Fish, Bread, Milk\n')
        else:
            for cost in price:
                sum += cost
                break
                print("Total cost: Php",sum)
                print(" ")
    elif choice == 'Milk':
        choice=input('Would you like to pick another order? y/n\n')
        if choice == 'y':
            choice=input('\nChoose an item: Apple, Banana, Fish, Bread, Milk\n')
        else:
            for cost in price:
                sum += cost
                break
                print("Total cost: Php",sum)
                print(" ")
    else: 
        print("Error!")
    break
