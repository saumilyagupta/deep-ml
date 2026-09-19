import numpy as np 
def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:

    a = np.array(a)
    b = np.array(b)
    try:
        return  np.matmul(a, b)
    except:
        return -1
    # return 