l = [i ** 2 for i in range(1, 11)]
# Should be [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print(l)
print(l[2:9:2]) #prints out l beginning at the thire element because a list begins at zero, then prints through element 8, skippes every other one

my_list = list(range(1,11)) #this generates a list from 1 to 10

print(my_list)
print(my_list[::2]) #prints out my_list beginning at 0 and ending at the next to the last element skipping every other one

backwards = my_list[::-1]
print(backwards)


to_one_hundred = list(range(101))
#to_one_hundred = range(101) this may work in python two but it does not work in 3

backwards_by_tens = to_one_hundred[::-10]
print(backwards_by_tens)

to_21 = list(range(1,22))
odds = to_21[::2]
middle_third = to_21[7:14]

print(middle_third)
