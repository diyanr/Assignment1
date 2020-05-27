import numpy as np
import matplotlib.pyplot as plt
import math

x = np.linspace(0,2*math.pi,100)
plt.plot(x,np.sin(x),label="Sine")
plt.plot(x,np.cos(x),label="Cosine")
plt.legend()
plt.show()
