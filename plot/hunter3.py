import numpy as np
from adjustText import adjust_text
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.lines as mlines

def calc(ori, verbose=0):
    a = np.array(ori)
    asum = sum(a)
    a = a/asum
    ent = sum([-x*np.log2(x) for x in a])
    print(asum, ent)
    return asum ,ent

res = []
labels = []
ori = [ 166.6,  400.2,  639.2] 
x, y = calc(original)
ori_, = plt.plot(x, y, "ro",  color='black')
plt.text(x, y, 'original')

plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
plt.xlabel('sum of resources consumed by all agents in a single game')
plt.ylabel('entropy')

#Method I
res = []
labels = []

labels.append('negative step function')
ori = [ 174.2,  291.6,  339.8]
res.append(calc(ori))

labels.append('step function')
ori = [ 172.5,  342.5,  535.6]
res.append(calc(ori))

labels.append('exponential')
ori = [ 168.3,  379.6,  646.3]
res.append(calc(ori))

res = np.array(res)
x, y = res[:,0], res[:,1]
go1, = plt.plot(x, y, "ro", color='g')
texts = []
for i in range(3): texts.append(plt.text(x[i], y[i], labels[i]))
adjust_text(texts)

#Method 2
res = []
labels = []
ori = 
res.append(calc(ori))
labels.append('τ=10')
ori =
res.append(calc(ori))
labels.append('τ=8')
ori =
res.append(calc(ori))
labels.append('τ=6')

res = np.array(res)
x, y = res[:,0], res[:,1]
go2, = plt.plot(x, y, "ro",  color='r')
texts = []
for i in range(0,3): texts.append(plt.text(x[i], y[i], labels[i]))
adjust_text(texts)

res = []
labels = []
ori =
res.append(calc(ori))
labels.append('τ=6')
ori =
res.append(calc(ori))
labels.append('τ=8')
ori =
res.append(calc(ori))
labels.append('τ=10')

res = np.array(res)
x, y = res[:,0], res[:,1]
go3, = plt.plot(x, y, "ro", color='b')
texts = []
for i in range(3): texts.append(plt.text(x[i], y[i], labels[i]))
adjust_text(texts)

plt.legend([go1, go2, go3], ['Method I', 'Method II (step function)', 'Method II (negative step function)'], loc=3)
plt.title('Hunter Prey (3 players)')

plt.savefig('hunterprey3')
plt.show()
input()
