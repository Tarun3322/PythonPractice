class Employee:
    def __init__(self, name, id, location):
        self.name = name
        self.id = id
        self.location = location

    def prnt(self):
        print(self.name + " is working in " + self.location + " location" + ", whose id is " + self.id + ".")

emp1 = Employee("Tarun", "0210487", "HYD")
emp2 = Employee("Seethayya","10811","VSKP")

emp1.prnt()
emp2.prnt()