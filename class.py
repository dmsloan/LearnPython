class Animal(object):
  """Makes cute animals."""
  is_alive = True
  def __init__(self, name, age):
    self.name = name
    self.age = age
  # Add your method here!
  def description(self):
    print(self.name)
    print(self.age)

hippo = Animal("Hipp", 4)

print(hippo.name)

hippo.description()


class Employee(object):
  def __init__(self, name):
    self.name = name
  def greet(self, other):
    print("Hello, %s" % other.name)

class CEO(Employee):
  def greet(self, other):
    print("Get back to work, %s!" % other.name)

ceo = CEO("Emily")
emp = Employee("Steve")
emp.greet(ceo)
# Hello, Emily
ceo.greet(emp)
# Get back to work, Steve!

#the following demonstrates the use of the "super" call
class Employee1(object):
  """Models real-life employees!"""
  def __init__(self, employee_name):
    self.employee_name = employee_name

  def calculate_wage(self, hours):
    self.hours = hours
    return hours * 20.00

class PartTimeEmployee(Employee1):
  def full_time_wage(self, hours):
    return super(PartTimeEmployee, self).calculate_wage(hours)
  
  def calculate_wage(self, hours):
    self.hours = hours
    return hours * 12.00

  milton = PartTimeEmployee("Milton")
  print(milton.full_time_wage(10))