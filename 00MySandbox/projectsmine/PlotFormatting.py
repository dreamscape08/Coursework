#PlotFormatting

# %%
# Dependencies
import matplotlib.pyplot as plt
import numpy as np


# %%
# Generate the x values from 0 to 10 using a step of 0.1
x_axis = np.arange(0, 10, 0.1)
sin = np.sin(x_axis)
cos = np.cos(x_axis)


# %%
# Add a semi-transparent horizontal line at y = 0
plt.hlines(0, 0, 10, alpha=0.25)


# %%
# Use dots or other markers for your plots, and change their colors

plt.plot(x_axis, sin, linewidth=0, marker="o", color="blue")
plt.plot(x_axis, cos, linewidth=0, marker="^", color="red")


# %%
# Add labels to the x and y axes
plt.title("Juxtaposed Sine and Cosine Curves")
plt.xlabel("Input (Sampled Real Numbers from 0 to 10)")
plt.ylabel("Value of Sine (blue) and Cosine (red)")


# %%
# Set your x and y limits
plt.xlim(0, 10)
plt.ylim(-1, 1)


# %%
# Set a grid on the plot
plt.grid()


# %%
# Save the plot and display it
plt.savefig("sin_cos_with_markers.png")
plt.show()


# %%
plt.show()


# %%



