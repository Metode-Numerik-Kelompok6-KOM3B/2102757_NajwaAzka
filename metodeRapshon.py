#Algoritma Metode Rapshon

def f(x):
    return x**3 - 6*x +2 

def g(x):
    return 3*x**2 -6

def newtonRaphson(x0,e,N):
    step = 1
    flag = 1
    condition = True
    while condition:
        if g(x0) == 0.0:
            print('Divide by zero error!')
            break
        x1 = x0 - f(x0)/g(x0)
        print('Iterasi-%d, x1 = %0.6f dan f(x1) = %0.6f' % (step, x1, f(x1)))
        x0 = x1
        step = step + 1
        if step > N:
            flag = 0
            break
        condition = abs(f(x1)) > e
    
    if flag==1:
        print('\nRequired root is: %0.8f' % x1)
        
    else:
        print('\nNot Convergent.')


x0 = input('Enter Guess: ')
e = input('Tolerable Error: ')
N = input('Maximum Step: ')

x0 = float(x0)
e = float(e)

N = int(N)

newtonRaphson(x0,e,N)