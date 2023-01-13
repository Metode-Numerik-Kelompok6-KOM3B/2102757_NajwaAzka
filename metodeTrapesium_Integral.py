# Algoritma metode Integral

e= 2.71828
def f(x):
    pepega = eval(fx)
    return pepega

def trapezoidal(x,y,z): 
    h = (y - x) / z
    sum = f(x)+f(y)
    
    for i = 1 : z -1
        k = x + i*h
        sum = sum+ 2 * f(k)
        
    sum = sum* h/2
    return sum
    
f= inline('4*x-x^2','x')

x = input('masukkan batas bawah integrasi :')
y = input(' masukkan batas atas integrasi :')
z = input('masukkan jumlah segmen N :')

hasil = trapezoidal(x, y, z) #untuk menampilkan hasil
print("Hasil dari metode trapesium: %0.6f" % (hasil))


