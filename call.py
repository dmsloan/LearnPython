#this script demonstrates calling a function from a function.

grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def grades_sum(scores):
  total = 0
  for score in scores: 
    total += score
  return total

print(grades_sum(grades))

def grades_average(grades_input):
  sum_of_grades = grades_sum(grades_input) #calls the grades_sum function and stores the result in sum_of_grades
  average = sum_of_grades / float(len(grades_input)) #calculates the average grade
  return average #returns the average grade

print(grades_average(grades))