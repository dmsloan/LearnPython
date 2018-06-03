doubles_by_3 = [x * 2 for x in range(1, 6) if (x * 2) % 3 == 0]

# Complete the following line. Use the line above for help.

even_squares = [x ** 2 for x in range(1, 11) if x % 2 == 0]
print(even_squares)

cubes_by_four = [c ** 3 for c in range(1, 11) if (c ** 3) %4 == 0]
print(cubes_by_four)

threes_and_fives = [x for x in range(1,16) if x % 3 == 0 or x % 5 == 0]
print(threes_and_fives)