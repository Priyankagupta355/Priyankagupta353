contact = {}

print("--------------------Contact Book App---------------------------------")
print("1. Create Contact")
print("2. View all Contact")
print("3. Delete Contact")
print("4. Seacrch Contact")
print("5. Update Contact")
print("6. Exist Contact")

choice = input("Enter your Choice (1-6):")

if choice == '1':
    name = input("Enter Your Name :")
    age = int(input("Enter your age :"))
    email = input("Enter Your email :")
    Contact_No = input("Enter your Contact Number:")

    if name in contact:
        print("Contact already exists")

    else:
        contact[name] = age,email,Contact_No
        print("Contact added Successfully..")


elif choice == '2':
    if not contact:
        print("Contact not found..")
    else:
        for name,age,email,Contact_No in contact.items():
            print('Contact List')
            print(f"{name} : {age,email,Contact_No}")

elif choice == '3':
    name = input("Enter contact name that you want to delete :")              
    if name in contact:
        del contact[name]
        print('Contact {name} has been deleted Successfully')
    else:
        print(f"Contact {name} doesn't exist")    

elif choice == '4':
    name = input("Enter search contact name :")
    if name in contact:
        print("{name} has been added in your contact-List")
    else:
        print(f"{name} doesn't exist this contact name")    

elif choice == '5':
    name = input("Enter update contact name :")
    if name in contact:
        contact[name] = ""
        print(f"Updated contact name is : {name}")
    else:
        print("Contact name doesn't exists..")    

elif choice == '6':
    print("Closing the Contact App...")

else:
    print('Invalid Range\nplease enter in between range(1-6):')

            



        

