import csv

#Student class_______________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
class student:
    def __init__(self, name):
        self.name = name
        self.grades = []        

    def addGrade(self, grade):
        if 0 <= grade <= 100:
            self.grades.append(grade)
        else:
            print("Invalid grade")

    def getGrades(self):
        return self.grades
    
    def averageGrade(self):
        return round(sum(self.grades) / len(self.grades))


#Gradebook class_______________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
class gradebook():
    def __init__(self):
        self.students = {}


    def addStudent(self, name):
        if name in self.students:
            print(f"{name} is already in the gradebook")
        else:
            self.students[name] = student(name)
            print(f"Added {name} to the gradebook")


    def enterGrade(self, name, grade):
        if name in self.students:
            self.students[name].addGrade(grade)
            print(f"Added the grade {grade} for {name}") 
        else:
            print(f"{name} is not in the gradebook")

    
    def display(self):
        for name in self.students:
            if len(self.students[name].getGrades()) == 0:
                print(f"{name}: No grades")
            else:
                print(f"{name}: {self.students[name].getGrades()}| Average: {self.students[name].averageGrade()}")
    
    def save(self, filename='CSV files/gradebook.csv'):
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)

            writer.writerow(["Name", "Grade"])

            for i, student in enumerate(self.students):
                name = self.students[student].name
                grade = self.students[student].getGrades()
                row = []

                row.append(name)
                for j in range(len(grade)):
                    row.append(grade[j])
                row.append(self.students[student].averageGrade())
                
                print(row)
                writer.writerow(row)


    def load(self, gb, filename='CSV files/gradebook.csv'):
        try:
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                name = self.students

                self.students.clear()
                next(reader)  

                for row in reader:
                    gb.addStudent(row[0])
                    for i in range(1, len(row)-1):
                        gb.enterGrade(row[0], int(row[i]))
                       
        except FileNotFoundError:
            print("Can't find file - No Joke... Please Save Jokes First")
        

#Menu function____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
def menu():
    gb = gradebook()
    
    while True:
        print("\n\n-------Gradebook Menu-------\n1. Add student\n2. Add grade\n3. Display gradebook\n4. Save gradebook to file\n5. Load gradebook from file\n6. Exit")
        choice = int(input("\nEnter your choice (1-6): "))
        if choice == 1:
            name = input("Enter the student's name: ")
            gb.addStudent(name)
        elif choice == 2:
            name = input("Enter the student's name: ")
            try:
                grade = int(input("Enter the student's grade(0-100): "))
                gb.enterGrade(name, grade)
            except ValueError:
                print("Invalid grade")
        elif choice == 3:
            gb.display()
        elif choice == 4:
            gb.save()
        elif choice == 5:
            gb.load(gb)
        elif choice == 6:
            break
        else:
            print("Invalid choice")

menu()
