import plotly.express as px
import plotly.data as pldata
import pandas as pd

df = pldata.wind()
print(df.head(10))
print(df.tail(10))


df['strength'] = df['strength'].str.extract('(\d+)').astype(float)
fig = px.scatter(df, x='frequency', y='strength', color='direction')
fig.write_html("wind.html")
fig.show()