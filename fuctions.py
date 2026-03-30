

def register_student(student_list, name_id, name, years, course, status):
    name_id = int(name_id)
    years = int(years)
    course = int(course)

    if name_id not in student_list:
        student_list[name_id] = {
            "student": name,
            "age": years,
            "course": course,
            "status": status
        }
    
def show_students(student_list):
    for data, i in student_list.items():
        print(f"ID: {data}")
        print(f"name: {i["student"]} | age: {i["age"]} | course: {i["course"]} | status {i["status"]}")

def search_ID(student_list, se_id):
    se_id = int(se_id)
    for data, i in student_list.items():
        if data == se_id:
            print("student found.")
            print(f"name: {i["student"]} | age: {i["age"]} | course: {i["course"]} | status {i["status"]}")
            return
        
    print("student not found.")

def update_info(student_list, se_id):
    se_id = int(se_id)
    for data, i in student_list.items():
        if data == se_id:
            print("student found.")
            print(f"name: {i["student"]} | age: {i["age"]} | course: {i["course"]} | status {i["status"]}")

    for data, i in student_list.items():
        p = "e"
        if se_id == data:
            name_input = input("enter new name(enter to skip): ")
            new_name = name_input if name_input != "" else None
            while p == "e":
                years_input = input("enter new age(enter to skip): ")
                new_years = years_input if years_input != "" else None
                if new_years is None:
                    p = "r"
                else:
                    try:
                        new_years = int(new_years)
                        p = "r"
                    except ValueError:
                        print("Error, enter integers numbers.")
            p = "e"
            while p == "e":
                course_input = input("enter new course(enter to skip): ")
                new_course = course_input if course_input != "" else None
                if new_course is None:
                    p = "r"
                else:
                    try:
                        new_years = int(new_years)
                        p = "r"
                    except ValueError:
                        print("Error, enter integers numbers.")
            p = "e"
            while p == "e":
                status_input = input("enter new status(enter to skip): ").lower()
                new_status = status_input if status_input != "" else None
                if new_status == "active":
                    i["status"] = new_status
                    p = "r"
                elif new_status == "inactive":
                    i["status"] = new_status
                    p = "r"
                elif new_status is None:
                    i["status"] = i["status"]
                    p = "r"
                else:
                    print("option invalid")
            
            i["student"] = new_name if new_name is not None else i["student"]
            i["age"] = new_years if new_years is not None else i["age"]
            i["course"] = new_course if new_course is not None else i["course"]
    print("student not found.")

def delete_st(student_list):
    p = "t"
    while p == "t":
        for data, i in student_list.items():
            print(f"ID: {data}")
            print(f"name: {i["student"]} | age: {i["age"]} | course: {i["course"]} | status {i["status"]}")
            se_id = input("enter the student ID: ")
            while not se_id.isdigit():
                se_id = input("invalid ID, enter valid ID: ")
            se_id = int(se_id)
            for data, i in student_list.items():
                if data == se_id:
                    print("student found.")
                    print(f"name: {i["student"]} | age: {i["age"]} | course: {i["course"]} | status {i["status"]}")
                    option = input("Are you sure this is the student you want to eliminate?(yes/no): ")
                    if option == "yes":
                        for data in student_list:
                            if data == se_id:
                                student_list.remove(data)
                                print("student delete.")
                                p = "r"
                    elif option == "no":
                        print("The student has not been removed👍")
                        p = "r"
                    else:
                        print("invalid option.")
            print("student not found.")
