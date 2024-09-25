import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("results.csv")
fig, ax = plt.subplots()

for a,c in zip(df['Algorithm'].unique(), ["green","blue"]):
    af = df.copy().loc[df['Algorithm'] == a].groupby(['Algorithm','Input']).median().reset_index()
    ax.plot(af['Input'],af['Time'],color=c)

ax.set(xlabel='input', ylabel='time',
#        title=''
)
ax.grid()

fig.savefig("test.pdf")
fig.savefig("test.png")
# plt.show()


