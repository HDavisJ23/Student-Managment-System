# simple Welcome that displays once at the top of the program
print("Welcome to Group 1 Student Management System")

# create class for Students with functions to Idenify Names, and ID and classification
class Student:
    def __init__(self, FirstName, LastName, StudentID, Classification):
        self.FirstName = FirstName
        self.LastName = LastName
        self.StudentID = StudentID
        self.Classification = Classification

    # Class Function to display students information
    def __str__(self):
        return f"Student Name: {self.FirstName} {self.LastName}, ID: {self.StudentID}, {self.Classification}"
    def __update_Student__(self, FirstName=None, LastName=None, StudentID=None, Classification = None):

    # Class Function to update stdent information 
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
# Calling Variable totalStudents to get size of the student list
totalStudents = len(Students)

# ###### WE COULD DEFINE A DELETE FUNCTION TO REMOVE STUDENTS FROM THE LIST YOU AND USE ETHER del or pop()
# https://www.youtube.com/watch?v=yOgrzw1FW3I or https://www.youtube.com/watch?v=qLKXbc_PBso or https://www.youtube.com/watch?v=7TY58o67Ryk

# Initialize menu at 0 to use in while loop so updates can stay relevent while program is running
Menu = 0
while (0 <= Menu <= 4):
    print("\n             MENU                   ")
    print("Please make a selection: \n1. View Student info \n2. Update Student Data \n3. View All Students \n4. Exit")    

    Menu = int(input("\nEnter a Menu # to proceed "))

    # Created options for Users when Menu 1 is selected (Here it only print class student str's return)
    if (Menu == 1):
            
        student_number = int(input(f"Enter Student# between 1 and {totalStudents} : " ))

        if 1<= student_number <= len(Students):
            print(Students[student_number - 1])
        else: 
            print("Invalid entry student", student_number ,"does not exist")

    # Use elif for when option 2 is selected Menu = 2 
    elif (Menu == 2):
        print("You select to update student info")
        print("please select a student")
        student_number = int(input(f"Enter Student# between 1 and {totalStudents} : " ))
        if (1<= student_number <= totalStudents):
            student = Students[student_number-1]
            print(f"You have selected to update {student}")
            FirstName = input("Enter new FirstName: ")
            student.__update_Student__(
                FirstName=FirstName
                # ##### SOMEONE ELSE CAN ADD THE ADDITIONAL INFORMATION TO UPDATE FOLLOW MY FIRSTNAME                
            )
            print(f"Student# {student_number} information is now: {student}")
            
    # Menu = 3 this option just print all of Students information by interating in a loop line by line
    elif (Menu == 3):
        for i in range (len(Students)):        
            print(f"Students{i + 1}: {Students[i]}, email")

    #M Menu 4 is selected. Exit the program. This is the proper of exiting, all updates are also lost
    elif (Menu == 4):
        print("Exiting the program... \nGoodbye!")
        exit()
      

