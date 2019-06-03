class Student:
    major = "CSE"
    
    def __init__(self, rollNo, name):
        self.rollNo = rollNo
        self.name = name
        
s1 = Student(1, "Faisal")
s2 = Student(2, "Arafat")
print(s1.name)
print(s1.rollNo)
print(s1.major)

print(s2.name)
print(s2.rollNo)
print(s2.major)