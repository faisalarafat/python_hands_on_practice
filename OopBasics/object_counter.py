class ObjectCounter:
    numberOfObjects = 0
    def __init__(self):
        ObjectCounter.numberOfObjects+=1
    @staticmethod
    def displayCount():
        print(ObjectCounter.numberOfObjects)

objectOne = ObjectCounter()
objectTwo = ObjectCounter()
ObjectCounter.displayCount()