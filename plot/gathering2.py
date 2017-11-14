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
original = [561.0, 1385.7]
x, y = calc(original)
ori_, = plt.plot(x, y, "ro",  color='black')
plt.text(x, y, 'original')

#calculate
x_ = np.linspace(1500, 2000, 500)
def f(x):
    a = original[0]/x
    return calc([a, 1-a])[1]

y_ = [f(xx) for xx in x_]
line, = plt.plot(x_, y_, '-.')
#plt.legend([line], ['boundary'])
#
plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))

plt.xlabel('sum of resources consumed by all agents in a single game')
plt.ylabel('entropy')


res = []
labels = []
ori = [ 594.93, 1308.9]
res.append(calc(ori))
labels.append('τ=10')

ori = [  601.45,  1269.09]
res.append(calc(ori))
labels.append('τ=8')
ori = [ 726.21,  806.42]
res.append(calc(ori))
labels.append('τ=6')

res = np.array(res)
x, y = res[:,0], res[:,1]
go1, = plt.plot(x, y, "ro",  color='r')
texts = []
for i in range(1,3): texts.append(plt.text(x[i], y[i], labels[i]))
adjust_text(texts)
texts.append(plt.text(x[0], y[0], labels[0], position=(x[0]+3, y[0])))

res = []
labels = []
ori = [ 817.4,  943.1]
res.append(calc(ori))
labels.append('negative step function')
ori = [ 662.2,  1190.6]
res.append(calc(ori))
labels.append('step function')
ori = [  727.6,  1055.1]
res.append(calc(ori))
labels.append('exponential')

res = np.array(res)
x, y = res[:,0], res[:,1]
go2, = plt.plot(x, y, "ro", color='g')
texts = []
for i in range(3): texts.append(plt.text(x[i], y[i], labels[i]))
adjust_text(texts)

res = []
labels = []
ori = [ 750.86,  960.35]
res.append(calc(ori))
labels.append('τ=6')
ori =[  696.93,  1207.15]
res.append(calc(ori))
labels.append('τ=8')
ori =[  595.08,  1292.54]
res.append(calc(ori))
labels.append('τ=10')

res = np.array(res)
x, y = res[:,0], res[:,1]
go3, = plt.plot(x, y, "ro", color='b')
texts = []
for i in range(3): texts.append(plt.text(x[i], y[i], labels[i]))
adjust_text(texts)

plt.legend([line,  go2, go1, go3], ['Boundary', 'Method I', 'Method II (step function)', 'Method II (negative step function)'])
plt.title('Gathering Game (2 players)')

plt.savefig('gathering2')
plt.show()
input()
