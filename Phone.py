phoneBook = {}

while True:
    print("..........PhoneBook Application.......")
    # display
    print("1. Add a New Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. List all Contacts")
    print("5. EXIT")

    choice = input("Enter your choice (1-5) :")

    if choice == '1':
        name = input("Enter Contact name :").strip()
        phone = input("Enter Phone number :").strip()
         

        if name in phoneBook:
            print("Contact already exists..") 
        else:
            phoneBook[name] = phone
            print("Contact added Successfully..")   


    elif choice =='2':
        name = input("Enter name to search :")         
        if name in phoneBook:
            print(f"{name}: {phoneBook[name]}")
        else:
            print("Contact Not found")   

    elif choice =='3':
        name = input("Enter name to delete Contact :")         
        if name in phoneBook:
            del phoneBook[name]
            print("Contact deleted Successfully..")
        else:
            print("Contact does not exists..")  

    elif choice == '4':
        if not phoneBook:
            print("Not Contact Found..")
        else:
            print("-----------------Contact List------------------")    
            for name,number in phoneBook.items():
                print(f"{name} : {number}")


    elif choice == '5':
        print("Existing phoneBook,GoodBye!")            
        break
    else:
        print("Invalid choice.\nPlease enter a number between 1-5 :")



     






