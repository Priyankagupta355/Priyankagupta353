# menu

menu = {
    "Pasta":50,
    "Pizza":40,
    "Momos":70,
    "Burger":60,
    "Coffee":80,
    "Chocalate Shake":70,
    "French Fries":50
}

# greet
print("Welcome to Python Restaurant\nHere's menu:")

# Display menu-
print("Pasta: Rs50\nPizza: Rs40\nMomos: Rs70\nBurger: Rs60\nCoffee: Rs80\nChocalate Shake: Rs70\nFrench Fries: Rs50")


order_total =0
item_1 = input("Enter the name of item that you want to Order :")

if item_1 in menu:

    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your Ordered.")

else:
    print(f"Ordered item {item_1} has not available Yet!")    


another_Order = input("Do you want to add Another item?(Yes/No):")

if another_Order == 'Yes':
    item_2 = input("Enter the  name of second item :")
    
    if item_2 in menu:
        order_total +=menu[item_2]
        print(f"Your item {item_2} has been added to your Ordered.")

    else:
        print(f"Ordered item {item_2} has not available Yet!")    


print(f"Your total Amount of items to Pay is :{order_total}")        