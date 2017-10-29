import plotly 
plotly.tools.set_credentials_file(username='Urno', api_key='GNGdfn3ST0XuO0w5Pyxm')

import plotly.plotly as py
import plotly.graph_objs as go

stream_id = 'rgpmrezgd0'
stream_1 = dict(token=stream_id, maxpoints=60)

trace1 = go.Scatter(
    x=[],
    y=[],
    mode='lines+markers',
    stream=stream_1
)

data = go.Data([trace1])

layout = go.Layout(title='Grade')
fig = go.Figure(data=data, layout=layout)
py.plot(fig, filename='python-streaming')

s = py.Stream(stream_id)
s.open()

import time
import random

time.sleep(5)
X=[0.0, 0.7, 1.0, 1.3, 1.7, 2.0, 2.3, 2.7, 3.0, 3.3, 3.7, 4.0, 4.3]
n=0;y=0

while True:
    n+=1
    x =random.choice(X)+0.2
    y =((y*(n-1)+x*(100/4.5))/n)
    print(x, y)

    s.write(dict(x=x, y=y))

    time.sleep(1)

s.close()
