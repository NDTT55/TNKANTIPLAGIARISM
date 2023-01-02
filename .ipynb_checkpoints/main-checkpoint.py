import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from tqdm import tqdm
import seaborn as sns
import random
import plotly.express as px
import plotly.figure_factory as ff

df = pd.read_csv(r'C:\Users\nikit\ml-fall22\01. Python\ml_hw01\data.csv')
df.info()
print('\n--------------------\n')
b=np.zeros(len(df['Age']))
for i in range(len(df['Age'])):
    b[i]=df.loc[i,'Age']

print('\n--------------------\n')

plt.xlabel('Возраст')
plt.ylabel('Количество игроков')
plt.title('Количество игроков по возрасту')
plt.grid(True)
plt.hist(b)
plt.show()
b=np.array(df['Preferred Foot'])
print(b)


plt.ylabel('count')
plt.xlabel('prefered legs')
plt.hist((b[b=='Right']),label='Right')
plt.hist((b[b=='Left']),label='Left')
plt.show()



