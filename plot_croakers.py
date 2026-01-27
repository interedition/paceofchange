#!/usr/bin/env python3
"""
Generate a high-resolution scatter plot matching the notebook exactly,
with an arrow pointing to "The Croakers" by Joseph Rodman Drake.
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Set the style to match the notebook (gray background with white grid)
plt.style.use('seaborn-v0_8-darkgrid')

# Load the data
data_path = "mainmodelpredictions.csv"
df = pd.read_csv(data_path)

# Extract x (publication date) and y (logistic score)
x = df['pubdate'].values
y = df['logistic'].values
classvector = df['realclass'].values

# Separate reviewed and random volumes for plotting
reviewedx = []
reviewedy = []
randomx = []
randomy = []

for idx, reviewcode in enumerate(classvector):
    if reviewcode == 1:
        reviewedx.append(x[idx])
        reviewedy.append(y[idx])
    else:
        randomx.append(x[idx])
        randomy.append(y[idx])

# Set axis limits (matching notebook)
plt.axis([min(x) - 2, max(x) + 2, min(y) - 0.02, max(y) + 0.02])

# Plot the data points (matching notebook exactly)
plt.plot(reviewedx, reviewedy, 'ro')
plt.plot(randomx, randomy, 'k+')

# Fit and plot the linear trend line (matching notebook)
z = np.polyfit(x, y, 1)
p = np.poly1d(z)
plt.plot(x, p(x), "b-")

# Find "The Croakers" data point
croakers_idx = df[df['title'].str.lower().str.contains('croakers', na=False)].index[0]
croakers_x = df.loc[croakers_idx, 'pubdate']
croakers_y = df.loc[croakers_idx, 'logistic']

# Add arrow pointing to "The Croakers" - label in lower left
plt.annotate('The Croakers',
             xy=(croakers_x, croakers_y),
             xytext=(min(x) + 5, min(y) + 0.01),
             arrowprops=dict(arrowstyle='->', color='red', lw=1.0),
             fontweight='bold',
             bbox=dict(boxstyle='round,pad=0.5', facecolor='white', edgecolor='black'))

# Save the high-resolution plot
output_file = "croakers_plot_highres.png"
plt.savefig(output_file, dpi=300, bbox_inches='tight')
print(f"High-resolution plot saved to: {output_file}")

# Show the plot (non-blocking to allow script to exit)
plt.show(block=False)
