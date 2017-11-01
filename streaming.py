import plotly 
plotly.tools.set_credentials_file(username='Urno', api_key='GNGdfn3ST0XuO0w5Pyxm')

import matplotlib.pyplot as plt
import random

G=[0.0, 0.7, 1.0, 1.3, 1.7, 2.0, 2.3, 2.7, 3.0, 3.3, 3.7, 4.0, 4.3]
n=0;y=0;X=[];Y=[]

while n<=7:
    n+=1
    x=random.choice(G)+0.2
    y=((y*(n-1)+x*(100/4.5))/n)
    X.append(x)
    Y.append(y)

plt.plot(X, Y, 'bs')
plt.axis([0, 4.5, 0, 100])
plt.show()
