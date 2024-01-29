import functools
class Student:
    def __init__(self, name):
        self.name = name
        self.subject = {}

    def learn(self, subject, hours):
        if subject not in self.subject:
            self.subject[subject] = 0
        self.subject[subject] += hours
        print(f"{self.name} spent {hours} hours learning {subject}.")


def track_progress(func):
    @functools.wraps(func)
    def wrapper(student, subject, hours):
        print(f"Tracking Progress for {student.name} in {subject}...")
        result = func(student, subject, hours)
        print(f"{student.name}'s total hours in {subject}: {student.subject}")
        return result
    return wrapper

@track_progress
def study(student, subject, hours):
    student.learn(subject, hours)

student1 = Student("Tayo")
student2 = Student("Johnpaul")

study(student1, "Python", 2)
study(student2, "Java", 5)