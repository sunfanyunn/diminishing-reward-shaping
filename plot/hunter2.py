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
original = [ 188.6,  493.9]
x, y = calc(original)
ori_, = plt.plot(x, y, "ro",  color='black')
plt.text(x, y, 'original')

#calculate
#x_ = np.linspace(600, 800, 500)
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


# Method I
#res = []
#labels = []
#ori = [ 195.8,  334.1]
#res.append(calc(ori))
#labels.append('negative step function')
#ori = [ 193.1,  446.3]
#res.append(calc(ori))
#labels.append('step function')
#ori = [ 197.7,  473.4]
#res.append(calc(ori))
#labels.append('exponential')

#res = np.array(res)
#x, y = res[:,0], res[:,1]
#go2, = plt.plot(x, y, "ro", color='g')
#texts = []
#for i in range(3): texts.append(plt.text(x[i], y[i], labels[i]))
#adjust_text(texts)

res = []
labels = []

# Method II (step function)
res = []
labels = []
#ori = [ 174.4,  513.1]
#res.append(calc(ori))
#labels.append('τ=10')
################################
ori = [192., 496.]
res.append(calc(ori))
labels.append('τ=8')

ori = [193.8, 492.8]
res.append(calc(ori))
labels.append('τ=6')

ori = [ 224.8, 444.2]
res.append(calc(ori))
labels.append('τ=4')
#################################
ori = [ 211.2,  478.8]
res.append(calc(ori))
labels.append('τ=2')

res = np.array(res)
x, y = res[:,0], res[:,1]
go1, = plt.plot(x, y, "ro",  color='r')
texts = []
for i in range(len(x)): texts.append(plt.text(x[i], y[i], labels[i]))
adjust_text(texts)


# Method II (negative ...)
res = []
labels = []
ori = [ 143.8, 176.6]
res.append(calc(ori))
labels.append('τ=2')
##################################
ori = [222.0, 321.6]
res.append(calc(ori))
labels.append('τ=4')

ori = [200.4,477.6]
res.append(calc(ori))
labels.append('τ=6')

ori = [ 188.2,  487. ]
res.append(calc(ori))
labels.append('τ=8')
###################################
# pretty much the same shit
#ori =
#res.append(calc(ori))
#labels.append('τ=10')

res = np.array(res)
x, y = res[:,0], res[:,1]
go3, = plt.plot(x, y, "ro", color='b')
texts = []
for i in range(3): texts.append(plt.text(x[i], y[i], labels[i]))
adjust_text(texts)

#plt.legend([line,  go2, go1, go3], ['Boundary', 'Method I', 'Method II (step function)', 'Method II (negative step function)'])

plt.savefig('hunterprey2')
plt.show()
input()
