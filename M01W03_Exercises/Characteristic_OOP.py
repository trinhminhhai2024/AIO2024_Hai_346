# Characteristics of OOP
from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, name: str, yob: int):
        self._name = name
        self._yob = yob

    def get_YoB(self):
        return self._yob

    @abstractmethod
    def describe(self):
        pass


class Student(Person):
    def __init__(self, name: str, yob: int, grade: str):
        super().__init__(name=name, yob=yob)
        self.__grade = grade

    def describe(self):
        print(f"Student Name: {
              self._name} - YoB: {self._yob} - Grade: {self.__grade}")


class Teacher(Person):
    def __init__(self, name: str, yob: int, subject: str):
        super().__init__(name=name, yob=yob)
        self.__subject = subject

    def describe(self):
        print(f"Teacher Name: {
              self._name} - YoB: {self._yob} - Subject: {self.__subject}")


class Doctor(Person):
    def __init__(self, name: str, yob: int, specialist: str):
        super().__init__(name=name, yob=yob)
        self.__specialist = specialist

    def describe(self):
        print(f"Doctor Name: {
              self._name} - YoB: {self._yob} - Specialist: {self.__specialist}")


class Ward:
    def __init__(self, name: str):
        self.__name = name
        self.__list_people = list()

    def add_person(self, person: Person):
        self.__list_people.append(person)

    def describe(self):
        print(f"Ward name:{self.__name}")

        for p in self.__list_people:
            p.describe()

    def count_doctor(self):
        counter = 0
        for p in self.__list_people:
            if isinstance(p, Doctor):
                counter += 1
        return print(f"\nNumber of doctors: {counter}")

    def sort_age(self):
        return self.__list_people.sort(key=lambda x: x.get_YoB(), reverse=True)

    def ave_teacher_yob(self):
        counter = 0
        total_year = 0

        for p in self.__list_people:
            if isinstance(p, Teacher):
                counter += 1
                total_year += p.get_YoB()
        return total_year / counter


student1 = Student(name="studentA", yob=2010, grade="7")
student1.describe()
teacher1 = Teacher(name="teacherA", yob=1969, subject="Math")
teacher1.describe()
teacher2 = Teacher(name="teacherB", yob=1995, subject="History")
teacher2.describe()
doctor1 = Doctor(name="doctorA", yob=1945, specialist="Endocrinologists")
doctor1.describe()
doctor2 = Doctor(name="doctorB", yob=1975, specialist="Cardiologists")
doctor2.describe()

ward1 = Ward(name=" Ward1")
ward1.add_person(student1)
ward1.add_person(teacher1)
ward1.add_person(teacher2)
ward1.add_person(doctor1)
ward1.add_person(doctor2)
# ward1.describe()
ward1.count_doctor()
print("\nAfter sorting Age of Ward1 people")
ward1.sort_age()
ward1.describe()
print(f"\nAverage year of birth (teachers): {ward1.ave_teacher_yob()}")
ward1.ave_teacher_yob()
