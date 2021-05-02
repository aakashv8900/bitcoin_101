import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import animation
from datetime import datetime
import json

with open('data.json') as f:
  data = json.load(f)

x = []
y = []

def plot():
    timestamp = datetime.now()
    timestamp = timestamp.strftime("%H:%M:%S")
    x.append(timestamp)
    y.append(data['bpi']['INR']['rate_float'])

    plt.cla()
    plt.plot(x, y)

ani = animation.FuncAnimation(plt.gcf(), plot,interval=1000)

plt.show()