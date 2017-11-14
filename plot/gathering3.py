import numpy as np
from adjustText import adjust_text
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.lines as mlines

def calc(ori, verbose=0):
    a = np.array(ori)/10
    asum = sum(a)
    a = a/asum
    ent = sum([-x*np.log2(x) for x in a])
    print(asum, ent)
    return asum ,ent

res = []
labels = []
original = [5022, 11599, 16588]
x, y = calc(original)
ori_, = plt.plot(x, y, "ro",  color='black')
plt.text(x, y, 'original')

#calculate
#x_ = np.linspace(1500, 2000, 500)
#def f(x):
#    a = original[0]/x
#    return calc([a, 1-a])[1]
#
#y_ = [f(xx) for xx in x_]
#line, = plt.plot(x_, y_, '-.')
#plt.legend([line], ['boundary'])

plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))

plt.xlabel('sum of resources consumed by all agents in a single game')
plt.ylabel('entropy')


#Method I
res = []
labels = []
labels.append('negative step function')
#ori = [ 9641.,  9285.,  9120.]
ori = [ 4557*2.  4660*2.  4962*2.]
res.append(calc(ori))

labels.append('step function')
ori = [ 6548.,   8073.,  14611.]
res.append(calc(ori))

labels.append('exponential')
ori = [  4894.,  10935.,  17215.]
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
ori = [  5687.6,  12141.5,  14649.0]
res.append(calc(ori))
labels.append('τ=10')
ori = [  6543.6,  12015.1,  13115.1]
res.append(calc(ori))
labels.append('τ=8')
ori = [ 7795.7,  8787.7,  9281.5]
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
ori = [ 7524.7,  9499.4,  9593.7]
res.append(calc(ori))
labels.append('τ=6')
ori = [  6531.5,  11293.1,  11932.7]
res.append(calc(ori))
labels.append('τ=8')
ori = [  5292.4,  12201.1,  15547.0]
res.append(calc(ori))
labels.append('τ=10')

res = np.array(res)
x, y = res[:,0], res[:,1]
go3, = plt.plot(x, y, "ro", color='b')
texts = []
for i in range(3): texts.append(plt.text(x[i], y[i], labels[i]))
adjust_text(texts)

plt.legend([go1, go2, go3], ['Method I', 'Method II (step function)', 'Method II (negative step function)'], loc=3)
plt.title('Gathering Game (3 players)')

plt.savefig('gathering3')
plt.show()
input()
