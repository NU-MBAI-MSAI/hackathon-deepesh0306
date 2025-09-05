import matplotlib
matplotlib.use("MacOSX")     # put this BEFORE importing pyplot

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
import random

def model_one():
    x = np.arange(0.0, 2.0, 0.01)
    y = np.sin(1 * np.pi * x)
    #x = np.arange(-2.0, 2.0, 0.01)
    #y = x ** 2 - 1
    plt.plot(x, y)
    #plt.plot(x, y, '-b')
    plt.xlabel('time (s)')
    plt.ylabel('volts (mV)')
    plt.title('Sine Wave')
    plt.show()

def model_two(npts):
    numbers = []
    for _ in range(npts):
        numbers.append(random.random())
    plt.hist(numbers,50)
    plt.show()

if __name__ == "__main__":
    print("running…")
    model_one()
    print("running2…")
    model_two(1000)
    print("finished…")
