from fuctions import register_student, show_students, search_ID, update_info, delete_st

p = "e"
student_list = {}
# The options are printed
while p == "e":
    print("\n---MENU---")
    print("1.register student")
    print("2.show list student")
    print("3.search ID")
    print("4.update information")
    print("5.delete student")
    print("6.exit")
    #Ask which option you wish to perform
    options = input("Which option do you wish to perform?: ")

    #These are the conditions to which the user can access
    if options == "1":
        k = "t"
        name_id = input("enter the student ID: ") #enter values ​​they are requesting
        while not name_id.isdigit(): #validate that they are numbers
            name_id = input("Error, enter the student ID: ") #repeat, enter values ​​they are asking for
        name = input("enter name: ")
        years = input("Enter the student's age: ") #enter values ​​they are requesting
        while not years.isdigit():
            years = input("Error, enter the student age: ") #repeat, enter values ​​they are asking for

        course= input("Enter the course: ") #enter values ​​they are requesting
        while not course.isdigit():
            course = input("Error, enter the course: ") #repeat, enter values ​​they are asking for

        while k == "t":
            status = input("status (Inactive/active): ").lower()
            if status == "inactive":
                register_student(student_list, name_id, name, years, course, status) #enter the function
                k = "r"
            elif status == "active":
                register_student(student_list, name_id, name, years, course, status) #enter the function
                k = "r"
            else:
                print("invalid option.")
                continue

    elif options == "2":
        show_students(student_list) #enter the function
    elif options == "3":
        se_id = input("enter the student ID: ")
        while not se_id.isdigit():
            se_id = input("invalid ID, enter valid ID: ")
        search_ID(student_list, se_id) #enter the function
    elif options == "4":
        se_id = input("enter the student ID: ")
        while not se_id.isdigit():
            se_id = input("invalid ID, enter valid ID: ")
        update_info(student_list, se_id) #enter the function
    elif options == "5":
        delete_st(student_list) #enter the function
    elif options == "6":
        p = "r"
    else:
        print("invalid option.") #In such a case, the user does not enter an option from those already indicated, this will appear