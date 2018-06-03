my_list = list(range(16))

#lambda is a keyword that creates the anonymous function.
print(filter(lambda x: x % 3 == 0, my_list))

languages = ["HTML", "JavaScript", "Python", "Ruby"]

# Add arguments to the filter()

#the followind line is for python 2 and does 
print(filter(lambda x: x == "Python", languages))

#the followind line is for python 3
print(list(filter(lambda x: x == "Python", languages)))


squares = [x ** 2 for x in range(1,11)]

print(list(filter(lambda x: x >= 30 and x <= 70, squares)))

