import matplotlib.pyplot as plt
import numpy as np
#входные данные
m = 10**(-27)
h_p = 10**(-27)
def U(X): # потенциал
    if X >= 0 and X < 1:
        return 100
    else:
        return 0
x = np.arange(-1, 3, 0.01)
plt.figure(0)
plt.xlabel('x')
plt.ylabel('U(x)')
plt.plot(x, [U(i) for i in x])
def T(e): # коэффициент прохождения через барьер в заисимости от энергии
    j = (-1)**0.5
    n = 100
    h = 1/n
    k = (e**0.5)
    x = np.arange(0, 1, 1/n)
    u = [(-2 + (h**2)*(e - U(i))) for i in x]
    q = -1/(u[n-1]/2 + j*k*h)
    R = [q]
    for i in range(n):
        q = -1/(u[n-1-i] + q)
        R.append(q)
    psy0 = (2*j*k*h)/((R[n-1])+(u[0]/2)+j*k*h)
    psy = [psy0]
    for i in range(n):
        psy0 = R[n-1-i]*psy0
        psy.append(psy0)
    return abs(psy[n-1])**2
E = np.arange(0.01, 400, 0.01)
Tt = [T(i) for i in E]
# График
plt.figure(1)
plt.xlabel('E')
plt.ylabel('T(E)')
plt.plot(E, Tt)
plt.show()
