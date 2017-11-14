import numpy as np

def calc(ori, verbose=0):
    a = np.array(ori)
    asum = sum(a)
    a = a/asum
    ent = sum([-x*np.log2(x) for x in a])
    print(asum, ent)
    return asum ,ent

dic={}
ori = []
ori.append([ 211.2,  478.8])
dic[0] = calc(ori[-1])
ori.append( [ 192.,  496.])
dic[1] = calc(ori[-1])
ori.append([193.8, 492.8])
dic[2] = calc(ori[-1])
ori.append([224.8, 444.2])
dic[3] = calc(ori[-1])
#[ 143.8  176.6]

#print(dic)
print('player_0', end='')
for i in range(len(dic)):
    print(' & {:.0f}'.format(ori[i][0]), end='')
print('\\\\')

print('player_1', end='')
for i in range(len(dic)):
    print(' & {:.0f}'.format(ori[i][1]), end='')
print('\\\\')

print('sum', end='')
for i in range(len(dic)):
    print(' & {:.0f}'.format(dic[i][0]), end='')
print('\\\\')

print('entropy', end='')
for i in range(len(dic)):
    print(' & {:.4f}'.format(dic[i][1]), end='')
print('\\\\')
