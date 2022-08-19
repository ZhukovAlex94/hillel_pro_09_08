from dataclasses import dataclass


@dataclass
class Student:
    name: str
    surname: str
    marks: list[int]

    def get_average(self) -> float:
        return sum(self.marks)/len(self.marks)


def main():
    with open("src_14.txt", "r") as file:
        data = file.readlines()

    students: list[Student] = []
    for line in data:
        name, surname, *marks = line.split()
        students.append(Student(name, surname, [int(mark) for mark in marks]))

    for student in students:
        if student.get_average() < 5:
            print(student.name, student.surname)

    print()

    average_marks = [student.get_average() for student in students]
    print(sum(average_marks)/len(average_marks))

    with open("output.txt", "w") as file:
        for student in students:
            name = f"{student.surname} {student.name[0]}.".ljust(20)
            print(f"{name} {student.get_average():.2f}", file=file)

            # file.write(f"{name} {student.get_average():.2f}\n")


if __name__ == "__main__":
    main()
