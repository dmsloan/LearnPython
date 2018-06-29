a=2
b=2

print(id(a))
print(type(a))
print(a)

print(id(b))
print(type(b))
print(b)

b = b+1

print(id(b))
print(type(b))
print(b)

# class Car(object):
#   condition = "new"
#   def __init__(self, model, color, mpg):
#     self.model = model
#     self.color = color
#     self.mpg   = mpg
    
#   def drive_car(self):
#     self.condition = "used"
#   def display_car(self):
#     print( "This is a %s %s with %s MPG." % (self.color, self.model, str(self.mpg)))

# my_car = Car("DeLorean", "silver", 88)

# my_car.drive_car()
# print(my_car.condition)

class Point3D(object):
  def __init__(self, x, y, z):
    self.x = x
    self.y = y
    self.z = z
  def __repr__(self):
    return("(%d, %d, %d)" % (self.x, self.y, self.z))
  
my_point = Point3D(1, 2, 3)
print(my_point)

hourly_pay = float(input("Please input pay rate: "))
hours_worked = float(input("Please input hours worked: "))
pay = hourly_pay * hours_worked

print("Your check will be $", pay)