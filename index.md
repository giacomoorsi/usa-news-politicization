---
layout: default
title: Our beautiful data story
---

# Intro

As is well known, the political system of the United States of America is marked by a system of bipolarity that opposes Democrats to Republicans. The bipolarity that opposes Americans at the ballot box and in the polls is reflected in several aspects of Americans' lifestyles, including the newspapers and news sources they rely on. This has led some news sources to lean toward a particular political area. It is well known, for example, that Democrats tend to follow TV news reported by CNN while Republicans by Fox News. 

In the journey illustrated by this data story, we have the ambition to report factual data that supports the thesis that some news sources are biased, analyzing 5 years of quotes reported by 19 online newspapers that we selected. 

{% include_relative home/introduction/metrics.html %}

## Motivations

Why did we decide to do this project?

We hear about politicization, polarization being a problem.

There was that thing where Trump was elected, and apparently online media helped
him.

Can we use the Quotebank dataset to confirm our intuitions?

# Background

Introduce the data we're going to use.

## Pew research

## Similarweb

## Twitter

# Neat plots

We probably want to discuss methodology somewhere over here?
I.e. what it is we exactly calculated.

Our analysis is based on counting articles in which a quote from a given speaker
occurs.

## Politicization

Show plots for politicization.

Describe the findings and how they aren't entirely what we expected.

Most politicized sources -- ones that report primarily political news (shocker!).

## Polarization

Show plots for polarization.

Discuss weirdnesses for years '16, '17, '18.

Maybe calculate and show plots for Trumpization as well? (% of quotes from Trump).

## Correlations

Show the correlation matrices.

Discuss how we found out that probably the Internet is left-wing-biased.



<div style="height:500px"></div><!-- Let's put some margin -->
---

# Instructions
In [this page](instructions) you can find some simple info on how to write that stuff. 

---

# This is a test page

This is an index page in markdown.

Here you can simply write in **markdown**. 
What happens if I import `HTML`?

{% include_relative home/snippet.html %}

Cool, it works. 

Now we can go back to work!!!

But also... we can import `Mardown` files!

{% include_relative home/chapter-01.md %}

## This is a test plotly demo

With plotly, we can generate interactive plots and save them to HTML.
Doing so is as simple as:

```python
import plotly.express as px
df = px.data.medals_long()

for i in range(0, len(df)):
    # Add some column that pretends to be a name of the point
    df.at[i, 'name'] = f'Point#{i}'

fig = px.scatter(df, y="count", x="nation", color="medal", symbol="medal", hover_name='name')
fig.update_traces(marker_size=10)
fig.write_html("./scatter_demo.html", include_plotlyjs="cdn", full_html=False)
```

And if we include the result, it looks like follows:

{% include_relative plotly/scatter_demo.html %}

Here's another demo chart:

{% include_relative plotly/bar_demo.html %}
