class Course:
    def __init__(self, name, ratings):
        self.name = name
        self.ratings = ratings
    
    def average(self):
        numberOfRatings = len(self.ratings)
        avg = sum(self.ratings)/numberOfRatings
        print("Average Ratings for ", self.name," Is", avg)
        
    
c1 = Course('Python Course', [1,2,3,4])
print(c1.name)
print(c1.ratings)
c1.average()

c2 = Course("Python with Django", [5,3.5,5,4.5])
print(c2.name)
print(c2.ratings)
c2.average()
