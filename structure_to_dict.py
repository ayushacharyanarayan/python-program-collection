"""Converting different data structures into a dictionary."""


# 1. List of pairs -> dictionary
def pairs_to_dict(pairs):
    return dict(pairs)


# 2. Two lists (keys, values) -> dictionary
def lists_to_dict(keys, values):
    return dict(zip(keys, values))


# 3. Class object -> dictionary
class Student:
    def __init__(self, name, course, year):
        self.name = name
        self.course = course
        self.year = year

    def to_dict(self):
        return {"name": self.name, "course": self.course, "year": self.year}


if __name__ == "__main__":
    pairs = [("name", "Dimpal"), ("course", "B.Tech CSE"), ("year", 2)]
    print("From pairs   :", pairs_to_dict(pairs))

    keys = ["name", "course", "year"]
    values = ["Dimpal", "B.Tech CSE", 2]
    print("From 2 lists :", lists_to_dict(keys, values))

    student = Student("Dimpal", "B.Tech CSE", 2)
    print("From object  :", student.to_dict())
    print("Using vars() :", vars(student))
