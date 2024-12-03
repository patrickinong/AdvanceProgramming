import csv

class Student:
    def __init__(self, student_number, name, coursework_marks, exam_mark):
        self.student_number = student_number
        self.name = name
        self.coursework_marks = coursework_marks
        self.exam_mark = exam_mark

    def total_coursework(self):
        return sum(self.coursework_marks)

    def overall_percentage(self):
        total_marks = self.total_coursework() + self.exam_mark
        return (total_marks / 160) * 100

    def grade(self):
        percentage = self.overall_percentage()
        if percentage >= 70:
            return 'A'
        elif percentage >= 60:
            return 'B'
        elif percentage >= 50:
            return 'C'
        elif percentage >= 40:
            return 'D'
        else:
            return 'F'

    def total_marks(self):
        return self.total_coursework() + self.exam_mark

def load_students(filename='studentMarks.txt'):
    students = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        num_students = int(next(reader)[0])
        for row in reader:
            student_number = int(row[0])
            name = row[1]
            coursework_marks = list(map(int, row[2:5]))
            exam_mark = int(row[5])
            students.append(Student(student_number, name, coursework_marks, exam_mark))
    return students

def view_all_students(students):
    for student in students:
        print(f"Name: {student.name}, Number: {student.student_number}, Total Coursework: {student.total_coursework()}, Exam: {student.exam_mark}, Percentage: {student.overall_percentage():.2f}%, Grade: {student.grade()}")
    
    average_percentage = sum([student.overall_percentage() for student in students]) / len(students)
    print(f"\nTotal students: {len(students)}, Average percentage: {average_percentage:.2f}%")

def view_individual_student(students, student_number=None, name=None):
    for student in students:
        if student_number == student.student_number or name.lower() in student.name.lower():
            print(f"Name: {student.name}, Number: {student.student_number}, Total Coursework: {student.total_coursework()}, Exam: {student.exam_mark}, Percentage: {student.overall_percentage():.2f}%, Grade: {student.grade()}")
            return
    print("Student not found!")

def student_with_highest_score(students):
    highest = max(students, key=lambda s: s.total_marks())
    print(f"Highest Scorer: {highest.name} with total marks {highest.total_marks()}")

def student_with_lowest_score(students):
    lowest = min(students, key=lambda s: s.total_marks())
    print(f"Lowest Scorer: {lowest.name} with total marks {lowest.total_marks()}")

def main():
    students = load_students()
    
    while True:
        print("\nMenu:")
        print("1. View all student records")
        print("2. View individual student record")
        print("3. Show student with highest total score")
        print("4. Show student with lowest total score")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            view_all_students(students)
        elif choice == '2':
            student_number = int(input("Enter student number (or 0 to search by name): "))
            if student_number != 0:
                view_individual_student(students, student_number=student_number)
            else:
                name = input("Enter student name: ")
                view_individual_student(students, name=name)
        elif choice == '3':
            student_with_highest_score(students)
        elif choice == '4':
            student_with_lowest_score(students)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == '__main__':
    main()
