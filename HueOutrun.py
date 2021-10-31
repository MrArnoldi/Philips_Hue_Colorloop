import time
from qhue import Bridge
ip = "GW_IP"
username = "SECRET_KEY"

bridge = Bridge(ip, username)
progress_range = range(0, 1000)
progress = min(progress_range)
progress_increment = 5

#Hue = 0 - 655035 HSV color gambit
#Cyan 31857
#Hot pink 60073
#print(bridge.lights())
#print(type(bridge.lights()))

zahlen = [zahl for zahl in bridge.lights()]

#for x in range(len(zahlen)):
#    print("Nr: {}, Name: {}".format(zahlen[x], bridge.lights[zahlen[x]]()["name"]))

lights = {9: [40000, 57000], 12: [57000, 40000], 17: [40000, 57000]}
for light in lights:
    #print("Nr: {}, Sat: {}".format(light, bridge.lights[light]()["state"]["sat"]))
    bridge.lights[light].state(on=True)

time.sleep(0.5)

for light in lights:
    bridge.lights[light].state(bri=254, hue=progress, sat = 254)

while True:
    time.sleep(0.1)
    percentage = progress/(max(progress_range)-min(progress_range)) 
    for light, interval in lights.items():
        hue = interval[0] + (interval[1] - interval[0]) * percentage
        bridge.lights[light].state(bri=254, hue=int(hue), sat = 254)

    progress += progress_increment
    
    if not (progress in progress_range):
        if progress > max(progress_range):
            progress_increment = -abs(progress_increment)
        else:
            progress_increment = abs(progress_increment)
    

# b.lights[12].state(on=True)
# b.lights[9].state(on=True)
# b.lights[17].state(on=True)
# b.lights[12].state(bri=254, hue=35000)
# b.lights[9].state(bri=254, hue=35000)
# b.lights[17].state(bri=254, hue=35000)
#b.lights[]


# while True:
#     print(i)
#     time.sleep(0.1)
#     b.lights[12].state(bri=254, hue=i)
#     b.lights[9].state(bri=254, hue=i)
#     b.lights[17].state(bri=254, hue=i)
#     if (switch == 0):
#         i += 500
#         if i > 60000:
#             switch = 1
#     elif (switch == 1):
#         i -= 500
#         if i < 35000:
#             switch = 0
