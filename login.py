# Login form usinf File Handling

filename = "users.txt"

try:
     open("C:\\Users\\Priyanka Gupta\\Desktop\\Python Programming\\Python Mini Projects\\Login Registration Form\\users.txt",'x').close()
except FileNotFoundError:
    print("File not found")
````````````````````````````````
except Exception as E:
    print("An error occurred.")    


def register():
    user = input("Enter new username :") 
    pwd = input("Enter new password :")
    
    with open("C:\\Users\\Priyanka Gupta\\Desktop\\Python Programming\\Python Mini Projects\\Login Registration Form\\users.txt",'a') as file:
        file.write(f"{user}\n{pwd}")
    print("Registration Successfully!")    

def login():
    user = input("Enter username :")    
    pwd = input("Enter Password :")
    
    with open("C:\\Users\\Priyanka Gupta\\Desktop\\Python Programming\\Python Mini Projects\\Login Registration Form\\users.txt","r") as f:
        users = f.readlines()

    for u in users:
        saved_user ,saved_pwd = u.strip().split(",")
        if saved_user == user and saved_pwd == pwd:
            print("Login Successful!\nWelcom",user)
            return
            print("Invalid username or password")

while True:
    print("----------------------Login Form Registration------------------------------------------")            
    print("1. Register\n2. Login\n3. Exit")

    choice = input("Enter choice (1-3) :")

    if choice == '1':
        register()

    elif choice == '2':
        login()    

    elif choice == '3':
        print("Existing...")    
        break

    else:
        print("Invalid choice!\nTry agin..")




