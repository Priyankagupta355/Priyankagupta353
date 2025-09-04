Student = {}

print("------------------Student Grades Management System------------------------")
print("1. Add a Student")
print("2. Delete a Student")
print("3. Update a Student")
print("4. View the Student")
print("5. EXISTS")

choice = int(input("Enter your choice in between (1-5) :"))

if choice == '1':
    name = input("Enter Student Name : ")
    marks = int(input("Enter Student Marks :"))

