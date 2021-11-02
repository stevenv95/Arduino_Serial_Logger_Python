import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# plt.style.use('fivethirtyeight')

x_vals = []
y_vals = []


def animate(i):
    data = pd.read_csv('data.csv')
    x = data['x_value']
    y = data['y_value']

    plt.cla()

    plt.plot(x, y, label='Vibration(G)')

    plt.legend(loc='upper left')
    plt.tight_layout()


ani = FuncAnimation(plt.gcf(), animate, interval=10)

plt.tight_layout()
plt.show()
