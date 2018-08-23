def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    # the following works but it is total crap, see the bottom for the proper way
    x = base
    
    if exp == 0:
        return 1
    elif exp == 1:
        return base
    else:
        for i in range(2,exp+1):
            x = x * base
        print (x)

iterPower(3,4)

# ans=1
# for i in range(exp):
#     ans = ans * base    
# print (ans)