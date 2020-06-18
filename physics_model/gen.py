import numpy as np
import matplotlib.pyplot as plt
import math

bubble_speed = 3.6  #in cms
water_height = 7    #in cm
time_to_top =  water_height/bubble_speed
total_gas = 90     #in cm^3
dissolving_rate = 20    #time to dissolve in s
gas_per_second = total_gas/dissolving_rate
gas_leaving_per_second = gas_per_second*0.75
t = np.arange(0., 80., 0.1)
res=0.1
air_volume = np.empty(len(t))


step = 0
maximum = 0 
air_volume[0]=0
for i in t:
    if t[step]<time_to_top:
        air_volume[step] = air_volume[step-1] + gas_per_second*res
        step += 1
    elif t[step] >= time_to_top:
        if t[step] < dissolving_rate:
            air_volume[step]=air_volume[step-1] + gas_per_second*res
            air_volume[step]= air_volume[step] - gas_leaving_per_second*res
            step += 1
        else:
                toset = air_volume[step-1] - gas_leaving_per_second*res
                if toset < 1:
                    break
                else:
                    air_volume[step] = toset
                    step += 1



water_volume = 2000  #cm3
Fa = air_volume/water_volume

V = 1470/(np.sqrt(1+(1.49*10000*Fa)))

f=V/(4*(12*0.01))


#start of in vino veritas model
H=13.8     #height in cm
pg=2.5      #glass density gcm3
a=0.5     #thickness
y=6*np.power(10,11)     #youngs modulus dyn/cm2
pl=1        #water density
R=3.25          #glass radius density
Hw=6         #height of water cm

def get_harmonics(m,n,hl):
    f=(1/(12*math.pi))*np.sqrt((3*y)/pg)*(a/(np.power(R,2)))*np.sqrt(   ((np.power((np.power(n,2)-1),2)) + np.power(((m*R)/H),4))  / (1+(1/(np.power(n,2) ))))
    
    fl= f/(np.sqrt(((1+(((a*pl*R)/(5*pg*a))*(hl/H)**4)))))

    return fl


for j in air_volume:
    print(j)


#plt.plot(t,Fa)
plt.plot(t,f)
#plt.plot(t,air_volume)
plt.hlines(get_harmonics(1,1,Hw),0,80)
plt.hlines(get_harmonics(1,2,Hw),0,80)
plt.hlines(get_harmonics(1,3,Hw),0,80)
plt.hlines(get_harmonics(0,0,Hw),0,80)
plt.hlines(get_harmonics(2,0,Hw),0,80)
plt.hlines(get_harmonics(2,1,Hw),0,80)

plt.show()


