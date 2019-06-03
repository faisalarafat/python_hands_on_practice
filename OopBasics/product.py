class Product:
    def __init__(self):
        self.name = 'IPhone'
        self.description = 'This is an awesome Smartphone'
        self.price = 700
        
    # Instance Method for Display Product details
    def display(self):
        print(self.name)
        print(self.description)
        print(self.price)

p1 = Product()
p1.display()

p2 = Product()
p2.display()