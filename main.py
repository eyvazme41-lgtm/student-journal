students = {
    "s01": {"name": "Teston", "group": "Python263", "grades": [12, 12, 12]},
    "s02": {"name": "Kate", "group": "Python263", "grades": []},
    "s03": {"name": "Tom", "group": "CSharp263", "grades": [11]},
    "s04": {"name": "Bob", "group": "CSharp263", "grades": [7, 2]},
    "s05": {"name": "Arthur", "group": "Python263", "grades": []},
    "s06": {"name": "Jane", "group": "CSharp263", "grades": [12, 11, 12]},
    "s07": {"name": "Sam", "group": "Python263", "grades": [9, 8, 9]},
    "s08": {"name": "Todd", "group": "Python263", "grades": [9, 8, 9]},
    "s09": {"name": "Rick", "group": "Python262", "grades": [12, 12, 12, 11, 12]},
    "s10": {"name": "Alice", "group": "CSharp263", "grades": [4, 3, 5]},
}

all_commands = {
    "help": "Show all commands ",
    "exit": "Ends program",
    "st": "Show all student data",
    "st <ID>": "Shows selected student data"
}




while True:
    entered = input("Enter command: ").split()
    command = entered[0]
    

    print()
    if command == "help":
        for key in all_commands.keys():
            print(f"{key} - {all_commands[key]}")
    elif command == "exit":
        print("Goodbye!")
        break



    elif command == "st":
        if len(entered) > 1:
            st_id = entered[1]

            if st_id not in students:
                print("Student ID not found!")
                continue

            student = students[st_id]
            grades = student["grades"].copy()
            
            for i in range(len(grades)):
                grades[i] = str(grades[i])
            if len(grades) == 0:
                grades_str = "Empty grades"
            else:
                grades_str = " ".join(grades)

            grades = student["grades"]
            grades_summ = 0

            for grade in grades:
                grades_summ += grade

            if len(grades) > 0:
                avg_grade = grades_summ / len(grades)
            else:
                avg_grade = "N/A"

            print(f"ID: {st_id}")
            print(f"Name: {student["name"]}")
            print(f"Group: {student["group"]}")
            print(f"Grades: {grades_str}")
            print(f"Average: {avg_grade}")


        else:
            print("ID - Name - Group - Grades")
            for st_id in students.keys():
                student = students[st_id]
                grades = student["grades"].copy()

                for i in range(len(grades)):
                   grades[i] = str(grades[i])
                if len(grades) == 0:
                   grades_str = "Empty grades"
                else:
                    grades_str = " ".join(grades)

                print(f"{st_id} - {student["name"]} - {student["group"]} - {grades_str}")

    else:
        print("Command not found. Enter 'help' for all commands")
    print()


    all_commands = {
    "help": "Show all commands ",
    "exit": "Ends program",
    "st": "Show all student data",
    "st <ID>": "Shows selected student data"
    "st_add: Add new student"
}

while True:
    entered = input("Enter command: ").split()
    command = entered[0]
    print()
     
