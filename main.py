import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import cryptocompare
from datetime import datetime 

%matplotlib notebook

plt.style.use('seaborn')

x_vals = []
y_vals = []

def get_crypto_price(cryptocurrency,currency):
    return cryptocompare.get_price(cryptocurrency,currency=currency)[cryptocurrency][currency]

def get_crypto_name(cryptocurrency):
    return cryptocompare.get_coin_list()[cryptocurrency]['FullName']

def animate(i):
    timestamp = datetime.now()
    timestamp = timestamp.strftime("%H:%M:%S")
    x_vals.append(timestamp)
    y_vals.append(get_crypto_price('BTC','INR'))

    plt.cla()
    
    plt.title(get_crypto_name('BTC') + ' Price Live Plotting')
    plt.gcf().canvas.set_window_title('Live Plotting Cryptocurrency')
    
    plt.xlabel('Time')
    plt.xticks(rotation=45)
    plt.ylabel('Price($)')
    plt.plot_date(x_vals,y_vals,linestyle="solid",ms=0)
    plt.tight_layout()
    
   
ani = FuncAnimation(plt.gcf(), animate, interval=10000)

plt.show()