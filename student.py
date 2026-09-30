students = []

def add_student(name, roll):
    students.append({"name": name, "roll": roll})

def display_students():
    for s in students:
        print(s)

def search_student(roll):
    for s in students:
        if s["roll"] == roll:
            return s

add_student("Arun Studet", 101)
add_student("asif", 102)

display_students()
print(search_student(101))