# Algoritma metode Bisection

import numpy as np
import matplotlib.pyplot as plt

def f(xc, x) :
    return eval(xc)

fx = input("Masukan f(x) =")
a = eval(input("Masukan nilai a = "))
b = eval(input("Masukan nilai b = "))
c = 0

epsilon = eval (input("Masukan nilai e = "))
j = eval (input("Masukan batas iterasi ="))

def biseksi(a, b, epsilon):
    if f(fx, a) * f(fx, b) > 0:
                print("Tidak memiliki akar persamaan")
    else:
        print("|   n   |   a   |   c   |   b   |  f(a) |  f(c) |  f(b) | (a-b) |")
        i=1
        while(abs(a-b) > epsilon and i<=j):
            c = (a+b)/2
            if(f(fx,a)*f(fx,c) < 0):
                print("|   %d   |%7.3f|%7.3f|%7.3f|%7.3f|%7.3f|%7.3f|%7.3f| [a,c] |"%(i,a,c,b, f(fx,a), f(fx,c), f(fx,b), abs(a-b)))
                b = c
                i+=1
            else:
                print("|   %d   |%7.3f|%7.3f|%7.3f|%7.3f|%7.3f|%7.3f|%7.3f| [c,b] |"%(i,a,c,b, f(fx,a), f(fx,c), f(fx,b), abs(a-b)))
                a = c
                i+=1        
        print("Akar hampiran adalah %7.3f"%(c))
        return(c)

biseksi(a, b, epsilon)
c = np.linspace(a, b, 100)
plt.plot(c, f(fx, c))
plt.grid()
plt.show()