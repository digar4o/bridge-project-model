import numpy as np
import matplotlib.pyplot as plt

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





for j in air_volume:
    print(j)


plt.plot(t,Fa)
plt.plot(t,f)
#plt.plot(t,air_volume)
plt.show()


