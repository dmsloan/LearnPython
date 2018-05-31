
def purify(numlist):
    evenList = list()
    for num in numlist:
        if num % 2 == 0:
            evenList.append(num)
    print(evenList)
    return(evenList)

purify([1,2,3,4,5,6,7,8,9])