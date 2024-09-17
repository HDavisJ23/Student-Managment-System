print("Welcome to Group 1 Student Management System")
print("             MENU                   ")
print("Please make a selection: \n1. View Student info \n2. Update Student Data \n3. View All Students \n4. Exit")
Menu = int(input("Enter a Menu # to proceed "))

class Student:
    def __init__(self, FirstName, LastName, StudentID, Classification):
        self.FirstName = FirstName
        self.LastName = LastName
        self.StudentID = StudentID
        self.Classification = Classification
    def __str__(self):
        return f"Student Name: {self.FirstName} {self.LastName}, ID: {self.StudentID}, {self.Classification}"
    def __update_Student__(self, FirstName=None, LastName=None, StudentID=None, Classification = None):
        if FirstName: self.FirstName = FirstName
        if LastName: self.LastName = LastName
        if StudentID: self.StudentID =StudentID
        if Classification: self.Classification = Classification

# Utilize a list to store student information
Students = [ Student("Ethan", "Waler", "V0001", "Sophomore"),
    Student("Sophia","Martinez", "V0002", "Sophomore"),
    Student("Liam", "Johnson", "V0003", "Sophomore"),
    Student("Olivia", "Brown", "V0004","Graduate"),
    Student("Noha", "Smith", "V0005", "Graduate"),
    Student("Ava", "Wilson", "V0006", "Sophomore"),
    Student("James", "Davis", "V0007", "Freshman"),
    Student("Isabella", "Garca", "V0008", "Graduate"),
    Student("William", "Lee", "V0009", "Sophomore"),
    Student("Mia", "Anderson", "V0010", "Junior"),
]
totalStudents = len(Students)
if (Menu == 1):
        
    student_number = int(input(f"Enter Student# between 1 and {totalStudents} : " ))

    if 1<= student_number <= len(Students):
        print(Students[student_number - 1])
    else: 
        print("Invalid entry student", student_number ,"does not exist")
elif (Menu == 2):
    print("You select to update student info")
    print("please select a student")
    student_number = int(input(f"Enter Student# between 1 and {totalStudents} : " ))
    if (1<= student_number <= totalStudents):
        student = Students[student_number-1]
        print(f"You have selected to update {student}")

elif (Menu == 3):
    for i in range (len(Students)):        
        print(f"Students{i + 1}: {Students[i]}, email")

elif (Menu == 4):
    print("Exiting the program... \nGoodbye!")
    exit()

      

