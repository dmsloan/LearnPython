def quad(a,b,c):
    underSquareRoot = (b**2-(4*a*c)) # you must put the * betwwen numbers to multiply, no 4ac
    if underSquareRoot < 0:
        print("No real solution")
        return()
    else:
        squareRoot = underSquareRoot**(1/2) #this line is underSquareRoot to the 
                                            #1/2 power, its equal to the square root without loading a library
        print("X=(",(-b+squareRoot)/(2*a),",",(-b-squareRoot)/(2*a),")")        
quad(5,6,1)