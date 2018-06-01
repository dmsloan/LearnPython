def median(numlist):
    numListSort = sorted(numlist)
    med = None
    if len(numListSort) % 2 > 0:
        med = (numListSort[int(len(numListSort)/2-.5)])
    else:
        med = ((numListSort[int(len(numListSort)/2)] + numListSort[int(len(numListSort)/2-1)])/2)
    print(med)
    return(med)
median([4, 5, 5, 4])