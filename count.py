def count(sequence, item):
    quan = 0
    for num in sequence:
        if num == item:
            quan += 1
    print(quan)
    return(quan)

count([1, 2, 1, 1, 1], 4)