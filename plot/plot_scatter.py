import numpy as np
def calc(ori, verbose=0):
    a = np.array(ori)/50
    asum = sum(a)
    a = a/asum
    ent = sum([-x*np.log(x) for x in a])
    print(asum, ent)
    return asum ,ent

res = []
# original
ori = [ 13759.,  45466.,  66657.,  98969.]
res.append(calc(ori))
# exponential
ori = [ 22645., 47844., 56759., 84674.]
res.append(calc(ori))
# step function
ori = [ 34902., 37013., 55380., 48336.]
res.append(calc(ori))
# negative step function



