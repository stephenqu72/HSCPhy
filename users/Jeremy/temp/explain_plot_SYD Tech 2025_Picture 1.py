```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# Define the function for mass as a function of velocity
m = lambda v: 0.5 * v**2  # Example function for mass increasing with velocity

# Generate the plot
fig, ax = plt.subplots()

# Generate data points
v = np.linspace(0, 10, 100)
m = m(v)

# Plot the function
ax.plot(v, m, label=r'$m(v) = rac{1}{2}v^2$')

# Add labels and legend
ax.set_xlabel(r'$v$')
ax.set_ylabel(r'$m$')
ax.legend()

# Show the plot
plt.show()
```