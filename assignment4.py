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
        print("\n----------------------------------")

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


def updating_student_dets():
    global student_details
    global data_for_students

    print("--- Update Student ---")
    roll = input(" please Enter roll no. of student to update the details: ")
    index_of_students = None
    updated_data = []
    with open(data_for_students, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if roll == row[0]:
                    index_of_students = counter
                    print("Student Found: at index ",index_of_students)
                    student_data = []
                    for field in student_details:
                        value = input("Enter " + field + ": ")
                        student_data.append(value)
                    updated_data.append(student_data)
                else:
                    updated_data.append(row)
                counter += 1


    
    if index_of_students is not None:
        with open(data_for_students, "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(updated_data)
    else:
        print("Roll No. not found in our database")

    input("Press any key to continue")


def delete_student():
    global student_details
    global data_for_students

    print("--- Delete Student ---")
    roll = input("Enter roll no. to delete: ")
    student_found = False
    updated_data = []
    with open(data_for_students, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        counter = 0
        for row in reader:
            if len(row) > 0:
                if roll != row[0]:
                    updated_data.append(row)
                    counter += 1
                else:
                    student_found = True

    if student_found is True:
        with open(data_for_students, "w", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerows(updated_data)
        print("Roll no. ", roll, "deleted successfully")
    else:
        print("Roll No. not found in our database")

    input("Press any key to continue")

while True:
    display_menu()

    choice = input("Enter your choice: ")
    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        searching__student()
    elif choice == '4':
        updating_student_dets()
    elif choice == '5':
        delete_student()
    else:
        break

print("-------------------------------")
print(" Thank you for using our system")
print("-------------------------------")
