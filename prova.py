from math import sin, cos, sqrt, acos
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

h=1
x=h
X=0
M=4
g=-9.81
k=20
X0=(M*g)/k

m=1

kc=0
K=0
u=0
U=0
EL=0
E=0


v=0.0
V=0.0

t=0
dt=0.0001

cars=[]
gorm=[]
fuck=[]
merda=[]

def collisione(v1, v2):
    u1 = (v1*(m-M)/(m+M)) + (2.0*v2*M/(m+M))
    u2 = (2.0*v1*m/(m+M)) + (v2*(M-m)/(m+M))
    return u1, u2



for i in range(10000000):
    fuck.append(i*dt)
    cars.append(x)
    gorm.append(X0)

    kc=(m*v*v)/2
    K=(M*V*V)/2
    u=-(m*g*x)
    U=-(M*g*X0)
    EL=(k*X0*X0)/2
    E=kc+K+u+U+EL

    #print("Kpal:",kc," Ksba:", K," Ppal:", u," Psba:", U," elas:", EL," mec:", E)
   
    x1=x
    X1=X

    F=-k*(X0-X)+M*g
    A=F/M
    v=v+g*dt
    V=V+A*dt
    x=x+v*dt
    X0=X0+V*dt

   
    merda.append(E)
    E=0

    if x<=X0:
        v,V= collisione(v,V)
        x=x1
        X=X1



fig, ax = plt.subplots()  
ax.plot(fuck, cars, 'red');
ax.plot(fuck, gorm);


fig2, ae = plt.subplots()
ae.plot(fuck, merda, 'pink');
plt.grid()

plt.show()
