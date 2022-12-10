import csv

student_details = ['roll', 'name', 'age', 'email', 'phone']
data_for_students = 'students.csv'


def display_menu():
    print("---------------------------------------")
    print(" Student Data Management System for DAV public school")
    print("---------------------------------------")
    print("1. Add New Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Quit")