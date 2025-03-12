import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("results.csv")

fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(16, 10))

axes[0, 0].bar(df['Distance'], df['Q2(x)'], color='lightskyblue')
axes[0, 0].set_xlabel('Distance')
axes[0, 0].set_ylabel('Q2(x)')
axes[0, 0].set_title('Bar Chart - Distance vs Q2(x)')

axes[0, 1].bar(df['Distance'], df['Q2(x)zz'], color='lightskyblue')
axes[0, 1].set_xlabel('Distance')
axes[0, 1].set_ylabel('Q2(x)zz')
axes[0, 1].set_title('Bar Chart - Distance vs Q2(x)zz')

axes[1, 0].scatter(df['Distance'], df['Q2(x)'], color='blue')
axes[1, 0].plot(df['Distance'], df['Q2(x)'], linestyle='dotted', color='blue')
axes[1, 0].set_xlabel('Distance')
axes[1, 0].set_ylabel('Q2(x)')
axes[1, 0].set_title('Scatter Plot - Distance vs Q2(x)')

axes[1, 1].scatter(df['Distance'], df['Q2(x)zz'], color='blue')
axes[1, 1].plot(df['Distance'], df['Q2(x)zz'], linestyle='dotted', color='blue')
axes[1, 1].set_xlabel('Distance')
axes[1, 1].set_ylabel('Q2(x)zz')
axes[1, 1].set_title('Scatter Plot - Distance vs Q2(x)zz')

plt.tight_layout()

plt.savefig("bar_and_scatter_charts.png")

plt.show()
