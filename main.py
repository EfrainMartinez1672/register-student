from fuctions import register_student, show_students, search_ID, update_info, delete_st

p = "e"
student_list = {}
while p == "e":
    print("\n---MENU---")
    print("1.register student")
    print("2.show list student")
    print("3.search ID")
    print("4.update information")
    print("5.delete student")
    print("6.exit")

    options = input("Which option do you wish to perform?: ")
    if options == "1":
        k = "t"
        name_id = input("enter the student ID: ")
        while not name_id.isdigit():
            name_id = input("Error, enter the student ID: ")
        name = input("enter name: ")
        years = input("Enter the student's age: ")
        while not years.isdigit():
            years = input("Error, enter the student age: ")

        course= input("Enter the course: ")
        while not course.isdigit():
            course = input("Error, enter the course: ")

        while k == "t":
            status = input("status (Inactive/active): ").lower()
            if status == "inactive":
                register_student(student_list, name_id, name, years, course, status)
                k = "r"
            elif status == "active":
                register_student(student_list, name_id, name, years, course, status)
                k = "r"
            else:
                print("invalid option.")
                continue

    elif options == "2":
        show_students(student_list)
    elif options == "3":
        se_id = input("enter the student ID: ")
        while not se_id.isdigit():
            se_id = input("invalid ID, enter valid ID: ")
        search_ID(student_list, se_id)
    elif options == "4":
        se_id = input("enter the student ID: ")
        while not se_id.isdigit():
            se_id = input("invalid ID, enter valid ID: ")
        update_info(student_list, se_id)
    elif options == "5":
        delete_st(student_list)
    elif options == "6":
        p = "r"
    else:
        print("invalid option.")