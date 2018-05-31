def product(numlist):
    ans = 0
    for num in numlist:
        if ans == 0:
            ans = num
        else:
            ans *= num
    print(ans)
    return(ans)

product([4,5,5])