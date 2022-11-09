x = [0, 0.52, 0.55, 0.68, 0.91, 0.94, 0.97, 1.03, 1.04, 1.2, 1.3,
     1.35, 1.4, 1.47, 1.6, 1.7, 1.85, 1.95, 1.99, 2.2, 2.28,
     2.45, 2.48, 2.56, 2.63, 2.67, 2.85, 3, 3.39, 3.57, 3.86, 3.99]

print(len(x))



def selection(a, b):
     res = []
     for i in x:
          if i >= a and i<b:
               res.append(i)
     return res
def newl(d):
     num_inter = len(d) - 1
     fenlei = []
     for i in range(len(d) - 1):
          fenlei.append(selection(d[i],d[i+1]))
     return fenlei

def newr(l):
     res = []
     for i in l:
          res.append(round(sum(i)/len(i), 4))
     return res
def newd(r):
     res = [0]
     for i in range(len(r) - 1):
          res.append(round((r[i] + r[i+1])/2, 3))
     res.append(4)
     return res

# 0___0.8___1.6___2.4___3.2___4
l51 = newl([0,0.8,1.6,2.4,3.2,4])
print(l51)
l5r1 = newr(l51)
print(l5r1)
l5d1 = newd(l5r1)
print(l5d1)

# 0___0.7993___1.5498___2.3007___3.1827___4
print('--------------L5 2-----------------')
l52 = newl(l5d1)
print(l52)
l5r2 = newr(l52)
print(l5r2)
l5d2 = newd(l5r1)
print(l5d2)

# L6
print('---------------L6 1-----------------')
l61 = newl([0, 0.667, 1.333, 2, 2.667, 3.333, 4])
print(l61)
l6r1 = newr(l61)
print(l6r1)
l6d1 = newd(l6r1)
print(str(l6d1).replace(', ', '___'))

# l6 2
print('-------------l6 2-------------------')
l62 = newl(l6d1)
print(l62)
l6r2 = newr(l62)
print(l6r2)
l6d2 = newd(l6r2)
print(str(l6d2).replace(', ', '___'))

# l6 3
print('-------------l6 3-------------------')
l63 = newl(l6d2)
print(l63)
l6r3 = newr(l63)
print(l6r3)
l6d3 = newd(l6r3)
print(str(l6d3).replace(', ', '___'))

# l6 4
print('-------------l6 4-------------------')
l64 = newl(l6d3)
print(l64)
l6r4 = newr(l64)
print(l6r4)
l6d4 = newd(l6r4)
print(str(l6d4).replace(', ', '___'))

# l6 4
print('-------------l6 5-------------------')
l65 = newl(l6d4)
print(l65)
l6r5 = newr(l65)
print(l6r5)
l6d5 = newd(l6r5)
print(str(l6d5).replace(', ', '___'))

print('-------------l8 1-------------------')
l81 = newl([0, 0.5, 1.0, 1.5, 2.0, 2.5, 3, 3.5, 4])
print(l81)
l8r1 = newr(l81)
print(l8r1)
l8d1 = newd(l8r1)
print(str(l8d1).replace(', ', '___'))

print('-------------l8 2-------------------')
l82 = newl(l8d1)
print(l82)
l8r2 = newr(l82)
print(l8r2)
l8d2 = newd(l8r2)
print(str(l8d2).replace(', ', '___'))


print('------------------------------------')
a = [[0, 0.52, 0.55, 0.68], [0.91, 0.94, 0.97, 1.03, 1.04, 1.2, 1.3, 1.35, 1.4, 1.47], [1.6, 1.7, 1.85, 1.95, 1.99, 2.2, 2.28], [2.45, 2.48, 2.56, 2.63, 2.67, 2.85, 3], [3.39, 3.57, 3.86, 3.99]]
b = [0.4375, 1.161, 1.9386, 2.6629, 3.7025]

def mse(x, x_hat):
     num = len(x)
     sumnum = 0
     for i in range(num):
          sumnum += (x[i] - x_hat[i]) ** 2
     return round(sumnum / num, 5)


ix = []
for i in range(len(a)):
     for j in a[i]:
          ix.append(i)
x_hat = []
for i in ix:
     x_hat.append(b[i])
print(ix)
print(x_hat)

print(mse(x, x_hat))

