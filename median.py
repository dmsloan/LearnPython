import statistics
def mediana(numlist):
    numListSort = sorted(numlist)
    print(numlist)
    print(numListSort)
    print(statistics.median(numlist))

    for num in numlist:
        if not num in noDup:
            noDup.append(num)
    print(noDup)
    return(noDup)

mediana([7, 12, 3, 1, 6])