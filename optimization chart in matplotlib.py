import math
import matplotlib.pyplot as plt 
l = float(input("L?"))
e = float(input("e?"))
f = 0
lst = []
flst = []
while True:
    ls = l * f
    lc = l - ls
    ds = ls/4
    ss = ds * ds
    rc = lc/(2*math.pi)
    sc = (math.pi) * rc * rc
    m = ss + sc
    lst.append(m)
    f += e
    flst.append(f)
    if l/100 <= f:
        break

print(lst)
print(flst)
plt.plot(flst, lst)
plt.xlabel('x - axis') 
plt.ylabel('S') 
plt.show()