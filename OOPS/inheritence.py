
class Parent():
    def show(self):
        print("Inside Parent")
class Parent1():
    def display(self):
        print("Inside Parent1")

class Child1(Parent,Parent1):
    def show(self):
        print("Inside Child1")
class Child(Parent):
    def show(self):
        print("Inside Child")
        super().show()

class Grandchild(Child):
    def show(self):
        print("inside Grandchild")
        Parent.show(self)
        # Parent.show(self)

# Driver's code
a = Child()
b = Grandchild()
c= Child1()
a.show()
print("__________________________________________")
b.show()
print("__________________________________________")
c.show()
print("__________________________________________")
c.display()

# b.show()