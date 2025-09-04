rent = int(input("Enter Your Hostel/flat Rent :"))
food = int(input("Enter the amount of food item :"))
electricity = int(input("Enter Your Electricity spend : :"))
charge_per_unit = int(input("Enter the charge per unit ="))
persons = int(input("Enter the number of persons living in room/flat ="))

total_bill = electricity + charge_per_unit
output = (food + rent + total_bill) // persons

print("Each person will pay =", output)
