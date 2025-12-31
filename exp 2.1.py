student_ids = ('S1', 'S2', 'S3')

students = {
    'S1': {'name': 'Ravi', 'marks': 85},
    'S2': {'name': 'Meena', 'marks': 62},
    'S3': {'name': 'Kiran', 'marks': 40}
}

def get_grade(marks):
    if marks >= 80:
        return "A"
    elif marks >= 60:
        return "B"
    elif marks >= 40:
        return "C"
    else:
        return "Fail"

print("STUDENT REPORT")
print("-" * 40)

for sid in student_ids:
    data = students[sid]
    grade = get_grade(data['marks'])

    print("Student ID :", sid)
    print("Name       :", data['name'])
    print("Marks      :", data['marks'])
    print("Grade      :", grade)
    print("-" * 40)
