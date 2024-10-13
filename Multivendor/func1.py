
def artOperation(a:int,b:int) ->int:
    x= a+b
    y= a-b
    z= a*b
    c = a/b  
    return x, y, z, c
b= artOperation(9,5)
print("Summation: ", b[0])
print("Sabistruction: ", b[1])
print("Multiplication: ", b[2])
print("Divition: ", b[3])

