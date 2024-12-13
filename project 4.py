import csv

students = []
studGrade = []
grades = [[-1]]
added = False

def menu():
    print("\n\n1. Add a student: \n2. Enter a grade: \n3. Display gradebook: \n4. Save gradebook to file: \n5. Load gradebook from file: \n6. Exit: ")
    choice = int(input("Enter your choice (1-6): "))
    if choice == 1:
        student()
    if choice == 2:
        grade()
    if choice == 3:
        display()
    if choice == 4:
        save()
    if choice == 5:
        load()
    if choice == 6:
        quit()

def student():
    name = input("\n\nEnter the student's name: ")
    students.append(name + ": ")
    print(f"Added {name} to the gradebook")
    menu()

def grade():
    global added, grades, students, studGrade
    name = input("\n\nEnter the student's name: ")
    for i in range(0,len(students)):
        if (name + ": ") == students[i]:
            if grades[0][0] == -1:
                grades[i][0] = int(input(f"Enter {name}'s grade: "))
            else:
                grades[i].append(int(input(f"Enter {name}'s grade: ")))
                while len(grades[i]) > 4:
                    print(f"Only 4 grades are allowed for {name}")
                    print(f"Removed {grades[i][0]} for {name}")
                    grades[i].remove(grades[i][0])   
            added = True
            print(f"Added {grades[i][len(grades[i])-1]} for {name}")
    if added == False:
        print("Student not found")

    added = False
    menu()

def display():
    global students, grades
    for i in range(0,len(students)):
        print(students[i], end = "")
        if grades == []:
            print("No grades entered", end = "")
        else:
            for j in range(0,len(grades[i])):
                print(grades[i][j], end = " ")
        print("")
    menu()

def save():
    with open('CSV files/gradebook.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        for student, grade in zip(students, grades):
            writer.writerow([student] + grade)
    menu()

def load():
    global students, grades, studGrade
    with open('CSV files/gradebook.csv', 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            students.append(row[0])
            for i in range(1,len(row)):
                if i > 4:
                    break
                studGrade.append(row[i])
            if grades[0][0] == -1:
                grades[0] = studGrade
            else:
                grades.append(studGrade)
            studGrade = []
    menu()

menu()
        