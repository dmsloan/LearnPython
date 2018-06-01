#this script demonstrates calling a function from a function.

grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

def grades_sum(scores):
  total = 0
  for score in scores: 
    total += score #adds score to the total
  return total

print(grades_sum(grades))

def grades_average(grades_input):
  sum_of_grades = grades_sum(grades_input) #calls the grades_sum function and stores the result in sum_of_grades
  average = sum_of_grades / float(len(grades_input)) #calculates the average grade
  return average #returns the average grade

print(grades_average(grades))

def grades_variance(scores):
  average = grades_average(scores) #calls the grades_average function
  variance = 0 #place holder for the variance variable
  for score in scores:  #loops throuth the scores list one score at a time.
    variance += (average - score) ** 2  # the ** 2 means to the power of 2
  variance = variance/float(len(scores))
  return variance

print(grades_variance(grades))

def grades_std_deviation(variance):
  return variance ** 0.5

variance = grades_variance(grades)
print(grades_std_deviation(variance))