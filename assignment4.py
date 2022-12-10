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


def add_student():
    print("-------------------------")
    print("Add Information regarding student")
    print("-------------------------")
    global student_details
    global data_for_students


    student_data = []
    for field in student_details:
        value = input("Enter " + field + ": ")
        student_data.append(value)

    with open(data_for_students, "a", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerows([student_data])

    print("Data saved successfully")
    input("Press any button to continue")
    return


def view_students():
    global student_details
    global data_for_students

    print("--- Student Records ---")

    with open(data_for_students, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for x in student_details:
            print(x, end='\t |')
        print("\n-----------------------------------------------------------------")

        for row in reader:
            for item in row:
                print(item, end="\t |")
            print("\n")

    input("Press any button to continue")

def searching__student():
    global student_details
    global data_for_students

    print("--- Search Student ---")
    roll = input("please Enter roll no. of the student to search: ")
    with open(data_for_students, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for comumns1 in reader:
            if len(comumns1) > 0:
                if roll == comumns1[0]:
                    print("----- Student Found -----")
                    print("Roll: ", comumns1[0])
                    print("Name: ", comumns1[1])
                    print("Age: ", comumns1[2])
                    print("Email: ", comumns1[3])
                    print("Phone: ", comumns1[4])
                    break
        else:
            print("Roll No. not found in our database")
    input("Press any button to continue")

