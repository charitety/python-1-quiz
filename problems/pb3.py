def youngest_student(students):
    # min = 0
    # youngest = ""
    #
    # for student in students:
    #     if min > students[student]:
    #         min = students[student]
    #         youngest = student
    # return youngest

    youngest = min(students)

    return youngest




students = {"Alice": 18, "Bob": 20, "Charlie": 19, "David": 22, "Jay": 20}
print(youngest_student(students))  # Expected output: "Alice"
