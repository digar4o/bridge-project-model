import numpy as np
import matplotlib.pyplot as plt

bubble_speed = 3.6  #in cms
water_height = 7    #in cm
time_to_top =  water_height/bubble_speed
total_gas = 300     #in cm^3
dissolving_rate = 40    #time to dissolve in s
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
                air_volume[step] = air_volume[step-1] - gas_leaving_per_second*res
                step += 1





for j in air_volume:
    print(j)


plt.plot(t,air_volume)
plt.show()


