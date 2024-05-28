class Student:
    def __init__(self, name, surname, age, university, degree):
        self.name = name.title()
        self.surname = surname.title()
        self.age = age
        self.university = university.title()
        self.degree = degree.title()

    @classmethod
    def from_csv(cls, line: str) -> "Student":
        return cls(*line.rstrip().split(","))

if __name__ == '__main__':
    
    with open("./Assets/students.csv","r") as f:
        lines = f.readlines()

    # List Comprehesion solution
    #students_list = [Student.from_csv(line) for line in lines]

    # Map solution
    students_list = map(Student.from_csv, lines)

    for student in students_list:
        print(
            f"Fullname: {student.name} {student.surname}\nAge: {student.age}\nUniversity: {student.university}\nDegree: {student.degree}\n"
        )