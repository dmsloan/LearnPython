def mediana(numlist):
    numListSort = sorted(numlist)
    print(numlist)
    print(numListSort)
    print(numListSort[3])
    if len(numListSort) % 2 > 0:
        print(numListSort[int(len(numListSort)/2-.5)])
    else:
        

    for num in numlist:
        if not num in noDup:
            noDup.append(num)
    print(noDup)
    return(noDup)

mediana([7, 12, 3, 1, 6])