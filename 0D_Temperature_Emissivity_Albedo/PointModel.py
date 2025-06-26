
import numpy as np
import matplotlib.pyplot as plt


R=6371e03 #m Earth's radius
h=8.3e03 #m vertical extent of the air layer
ro= 1.2 #kg/m3 density of air
c=1000 #J/kg K specific heat of air
a=np.linspace(0.1,0.9,199) #different types of albedo
S=1361 #W/m2 solar constant
e=np.linspace(0.1,0.9,199) #different types of emissivity
s=5.67e-08 #W/m2 K4 stefan-boltzmann constant

def Temp(aa,ee):
    return ((1-aa)*S/(4*ee*s))**(0.25)





T=np.zeros((len(a),len(e)))

for i in range(len(a)):
    for j in range(len(e)):
        T[i][j]=round(Temp(a[i],e[j])-273.15,-1)


albedo=np.zeros((len(a),len(a)))
for i in range(len(a)):
    albedo[:][i]=a[i]

emissivity=np.zeros((len(e),len(e)))
for i in range(len(e)):
    emissivity[i]=e


albedo=albedo.flatten()
emissivity=emissivity.flatten()
T=T.flatten()

plt.scatter(albedo, emissivity,c=T)
plt.xlabel("albedo")
plt.ylabel("emissivity")
plt.colorbar(label="Temperature Values of Corresponding colors")
plt.show()