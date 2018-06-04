first = 0b1110  #0b designates the number as binary
second = 0b101

print(first) #converts the incomming binary number to base 10
print (bin(first)) #keeps the incomming binary number binary
print(bin(12)) #converts a number to binary

print(int("111",2) )#Converts a non-integer input into an integer in base 10,
                    #first paramater is the non-integer second is the base that 
                    #the non-integer is
print(int("0b100",2))
print(int(bin(5),2))
# Print out the decimal equivalent of the binary 11001001.
print(int("0b11001001",2))
# you could also use:
print(int("11001001",2))

# Shift operators can only be done on intergers
# Left Bit Shift (<<)
print("Before shifting left two places",bin(second))
left=second<<2
print("After shifting left two places",bin(left))
   
# Right Bit Shift (>>)  
right=first>>2
print(first)

#bitwise and operator is "&"
print(bin(0b1110 & 0b101))

#bitwise or operator is "|"
print(bin(0b1110 | 0b101))

#The XOR (^) or exclusive or operator compares two numbers on a bit level and
#returns a number where the bits of that number are turned on if either of the
#corresponding bits of the two numbers are 1, but not both.
print("The following is XOR")
print(bin(first))
print(bin(second))
print(bin(first^second))

#The bitwise NOT operator (~) just flips all of the bits in a single number.
#What this actually means to the computer is actually very complicated,
#so we're not going to get into it. Just know that mathematically, this is
#equivalent to adding one to the number and then making it negative.

print("print ~42 yeilds", ~42)

def check_bit4(input):
  mask = 0b1000
  print(bin(input))
  if (bin(input)&mask) > 0:
    return("on")
  else:
    return("off")

check_bit4(0b11011)