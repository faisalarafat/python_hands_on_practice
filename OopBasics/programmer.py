class Programmer:
    def setName(self, firstName):
        self.name = firstName
    def getName(self):
        return self.name
    def setSalary(self, sal):
        self.salary = sal
    def getSalary(self):
        return self.salary
    def setTechnologies(self, techs):
        self.technologies = techs
    def getTechnologies(self):
        return self.technologies
    
p1 = Programmer()
p1.setName("Faisal Arafat")
p1.setSalary(568246)
p1.setTechnologies(["Java", "Hibernate", "Spring", "Python", "Django"])
print(p1.getName())
print(p1.getSalary())
print(p1.getTechnologies())
