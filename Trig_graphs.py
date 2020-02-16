from matplotlib import pyplot as plt
import numpy as np
from numpy import pi

print("\n")
print("What type of graph do you want?: ")
trig_type = input("S for sine, C for cosine and T for tangent: ")

if trig_type.lower() == "s":
    x = np.linspace(0, 2*pi, 360)
    y = np.sin(x)

elif trig_type.lower() == "c":
    x = np.linspace(0, 2*pi, 360)
    y = np.cos(x)
    
elif trig_type.lower() == "t":
    x = np.linspace(0, 2*pi, 180)
    y = np.tan(x)

    




plt.plot(x, y)
plt.grid()
plt.show()

