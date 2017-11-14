import numpy as np

def calc(ori, verbose=0):
    a = np.array(ori)

    asum = sum(a)
    a = a/asum
    ent = sum([-x*np.log2(x) for x in a])
    print(asum, ent)
    return asum ,ent

ori = []

dic = {}

orii = [ 166.6,  400.2,  639.2]
ori.append(orii)
dic[0] = calc(ori[-1])

orii = [ 177.4,  383.,   645.4]
ori.append(orii)
dic[1] = calc(ori[-1])

orii = [ 182.6, 407.4, 488.2]
ori.append(orii)
dic[2] = calc(ori[-1])

orii = [ 195.4,  289.2,  325.8]
ori.append(orii)
dic[3] = calc(ori[-1])

orii = [ 131.,   162.,   179.8]
ori.append(orii)
dic[4] = calc(ori[-1])

ori = np.array(ori)

#print(dic)
print('player_0', end='')
for i in range(len(dic)):
    print(' & {:.0f}'.format(ori[i][0]), end='')
print('\\\\')

print('player_1', end='')
for i in range(len(dic)):
    print(' & {:.0f}'.format(ori[i][1]), end='')
print('\\\\')

print('player_2', end='')
for i in range(len(dic)):
    print(' & {:.0f}'.format(ori[i][2]), end='')
print('\\\\')

print('sum', end='')
for i in range(len(dic)):
    print(' & {:.0f}'.format(dic[i][0]), end='')
print('\\\\')

print('entropy', end='')
for i in range(len(dic)):
    print(' & {:.4f}'.format(dic[i][1]), end='')
print('\\\\')
