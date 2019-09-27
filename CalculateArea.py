'''
    This Application is to calculate areas for different shapes (Rectanle , Square , Circle)
    using OPP Concepts in python
'''

class Shape():
    def __init__(self):
        pass

    def get_area(self):
        pass

class Rectangle(Shape):
    def __init__(self,l,b):
        self.l = l
        self.b = b

    def get_area(self):
        return self.l * self.b


class Circle(Shape):
    PI = 3.14
    def __init__(self,radius):
        self.radius = radius

    def get_area(self):
        return self.PI * self.radius * self.radius
    
class Square(Shape):
    def __init__(self,side):
        self.side = side

    def get_area(self):
        return  self.side ** 2


class Main():
    def __init__(self):
        self.choice = None
        self.choices = ("Rectangle","Square","Circle")

    def getShapeObject(self):
        if self.choice == 1 :
            data = input("Input Length and Width of Rectangle : ")
            dataList = data.split(" ")
            l = int(dataList[0])
            w = int(dataList[1])
            return Rectangle(l,w)
        elif self.choice == 2:
            data = input("Input Length of Square : ")
            l = data.split(" ")
            l = int(l[0])
            return Square(l)
        elif self.choice == 3:
            data = input("Input Radius of Circle : ")
            r = data.split(" ")
            r = int(r[0])
            return Circle(r)
        else:
            return None

    def play(self):
        print("Welcome To Area Calculation App")
        
        while True:
            print("Your Menu : ")
            print("1. Rectangle")
            print("2. Square")
            print("3. Circle")
            print("4. Quit")
            
            try:
                self.choice = int(input("\n Enter your Choice[1,2,3,4] "))

                if(self.choice in [1,2,3,4]):
                    if(self.choice == 4):
                        break
                    else:
                        shape = self.getShapeObject()
                        print(shape.get_area())
                else:
                    print("Wrong Choice! Please Choose one from menu")
                    continue
            
            except ValueError as ve:
                print("Value Error")
                print("Wrong Choice! Please Choose one from menu")
                continue
            
                            

c = Main()
c.play()



