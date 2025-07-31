#student gradebook manag

gradebook = {}
def calculate_grade(grade):
    if grade >= 90:
        return "A"
    elif grade >= 80:
        return "B"
    elif grade >=70:
        return "C"
    elif grade >= 60:
        return "D"
    else:
        return "F"

def add_student(gradebook):
    name = input("Enter student name: ")
    if name in gradebook:
        print(f"{name} Already exists!")
    else:
        gradebook[name]=[]
        print(f"{name} has been added")
    
def add_grade(gradebook):
    name = input("Enter student name: ")
    if name not in gradebook:
        print(f"{name} not found.")
        return
    try:
        grade = float(input("Enter grade (0-100): "))
        if 0 <= grade <=100:
            gradebook[name].append(grade)
            print(f"Grade added for {name}.")
        else:
            print("Invalid grade. Must be between 0 and 100.")
    except ValueError:
        print("Please enter a valid number.")

def view_student_report(gradebook):
    name= input("Enter student name: ")
    if name not in gradebook:
        print(f"{name} not found")
        return
    grade = gradebook[name]
    if not grade:
        print(f"No grades record for {name}")
        return
    avg = sum(grade) / len(grade)
    grade_value = calculate_grade(avg)
    print(f"{name}'s Average: {avg:.2f} Grade: {grade_value}")
    print(f"Grade: {grade}")

def class_statistics(gradebook):
    if not gradebook:
        print("No students in gradebook")
        return
    total_grade =[]
    student_average = {}

    for student, grade in gradebook.items():
        if grade:
            avg = sum(grade) / len(grade)
            student.averages[student] = avg
            total_grade.extend(grade)
    if not student_average:
        print("No grades to calculate statistics.")
        return
    
    class_avg = sum(total_grade) / len(grade)
    highest_average= max(student_average, key=student_average.get)
    lowest_average = min(student_average, key=student_average)

    print(f"Class Average: {class_avg:.2}")
    print(f"Top Student: {highest_average}")
    print(f"Lowest averate: {lowest_average}")

while True:
    print("\n_____Student GRADEBOOK MANAGER______")
    print("1. Add student")
    print("2. Add grade")
    print("3. view student report")
    print("4. class statistics")
    print("5. Exit")
    choice = input("Choose your operation: ")

    if choice == '1':
        add_student(gradebook)
    elif choice == '2':
        add_grade(gradebook)
    elif choice == '3':
        view_student_report(gradebook)
    elif choice == '4':
         class_statistics(gradebook)
    elif choice == '5':
        print("Exiting gradebook. Goodbye")
        
        break
    else:
        print("Invalid choice.")
        

