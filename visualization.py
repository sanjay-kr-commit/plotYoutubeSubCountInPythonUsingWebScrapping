from collections import deque
from time import sleep

import matplotlib.pyplot as plt

from youtube import sub_count

page_url = "https://www.youtube.com/@Sanjay-gy6ew"
delay = 1

# MAX NO. OF POINTS TO STORE
que = deque(maxlen=40)

maxHeight=0

while True:
    # GENERATING THE POINTS - FOR DEMO
    perc = sub_count(page_url)
    maxHeight=max(maxHeight,perc)
    print(perc)
    print(maxHeight)
    que.append(perc)

    # PLOTTING THE POINTS
    plt.plot(que)
    plt.scatter(range(len(que)), que)

    # SET Y AXIS RANGE
    plt.ylim(0, maxHeight*2)

    # DRAW, PAUSE AND CLEAR
    plt.draw()
    plt.pause(0.1)
    plt.clf()
    sleep(delay)