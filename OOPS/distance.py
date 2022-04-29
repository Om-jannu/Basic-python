class Distance:
    def distance(self):
        self.feet = int(input("enter distance in feets: "))
        self.inch = int(input("enter distance in inches: "))

    # def distance2(self):
    #     self.feet = int(input("enter distance in feets: "))
    #     self.inch = int(input("enter distance in inches: "))

    def display(self):
        print("sum of two distances in feets : ",self.feet)
        print("sum of two distances in inches : ", self.inch)

    def __add__(self, other):
        R = Distance()
        R.feet = self.feet + other.feet
        R.inch = self.inch + other.inch
        return R

distance1 = Distance()
distance2 = Distance()
print("Enter first distance")
distance1.distance()

print("Enter second distance")
distance2.distance()

distance3=distance1+distance2

print("The sum of both distance is")
distance3.display()




