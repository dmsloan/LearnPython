def remove_duplicates(numlist):
    noDup = list()
    for num in numlist:
        if not num in noDup:
            noDup.append(num)
    print(noDup)
    return(noDup)

remove_duplicates([1, 1, 2, 2, 2, 4])