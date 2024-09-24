import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("results.csv")
fig, ax = plt.subplots()

for a,c in zip(df['Algorithm'].unique(), ["green","blue"]):
    af = df.copy().loc[df['Algorithm'] == a].groupby(['Algorithm','Input']).median().reset_index()
    ax.plot(af['Input'],af['Time'],'ro',color=c)

ax.set(xlabel='input', ylabel='time',
#        title='About as simple as it gets, folks'
)
ax.grid()

fig.savefig("test.pdf")
plt.show()


