import plotly.express as px
df = px.data.medals_long()

for i in range(0, len(df)):
    # Add some column that pretends to be a name of the point
    df.at[i, 'name'] = f'Point#{i}'

fig = px.bar(df, x="nation", y="count", color="medal", hover_name="name", title="Long-Form Input")
fig.write_html("./bar_demo.html", include_plotlyjs="cdn", full_html=False)
