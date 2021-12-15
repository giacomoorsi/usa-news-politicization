---
layout: default
title: Our beautiful data story
---

As is well known, the political system of the United States of America is marked
by a system of bipolarity that opposes Democrats to Republicans. The bipolarity
that opposes Americans at the ballot box and in the polls is reflected in
several aspects of Americans' lifestyles, including the newspapers and news
sources they rely on. This has led some news sources to lean toward a particular
political area. It is well known, for example, that Democrats tend to follow TV
news reported by CNN while Republicans by Fox News.

In the journey illustrated by this data story, we have the ambition to report
factual data that supports the thesis that some news sources are biased,
analyzing 5 years of quotes reported by 19 online newspapers that we selected.

{% include_relative home/introduction/metrics.html %}

## Motivations

Why did we decide to do this project?

Over the recent years, we've been hearing more and more from our peers, as well
as reading on the internet, that there's an increasing amount of politicization
and polarization of news sources in the USA. During and after the 2016 election,
one could find numerous articles discussing that people backing Trump tended to
read different news sources from people on the left of the political spectrum,
news sources that reportendly tended to publish news pieces containing hoaxes
and conspiracy theories -
[this](https://www.washingtonpost.com/news/the-fix/wp/2017/08/22/trump-backers-disturbing-reliance-on-hoax-and-conspiracy-theory-websites-in-1-chart/).
is an example of such an article. We can still read that specific news sources
are gaining a huge number of readers by helping Trump spread his claims about
the last election being "stolen"; the news source in question being [the Gateway
Pundit](https://www.reuters.com/investigates/special-report/usa-election-threats-gatewaypundit/).
With a disturbing similarity to the "lügenpresse" accusations used by the Third
Reich against foreign press, Donald Trump himself has been claiming that many
traditional news sources are spreading "fake news" about him. Apparently, he
himself is basing his popularity on specific online news sources.

TODO: introduce Quotebank over here.

Intuitively, we would expect news sources aligned with Trump to publish articles
that cite him and people from his political circle - Republicans, that is - more
than people that oppose him, i.e. Democrats.

Can we use the Quotebank dataset to confirm our intuitions?

# Background

Introduce the data we're going to use.

## Similarweb

## Twitter

## Pew research

{% include_relative plots/pew_similarweb.html %}
{% include_relative plots/pew_twitter.html %}

# Neat plots

We probably want to discuss methodology somewhere over here?
I.e. what it is we exactly calculated.

Our analysis is based on counting articles in which a quote from a given speaker
occurs.

## Politicization

{% include_relative plots/stats_politicization.html %}

Describe the findings and how they aren't entirely what we expected.

Most politicized sources -- ones that report primarily political news (shocker!).

## Polarization

{% include_relative plots/stats_polarization_sgn.html %}

{% include_relative plots/stats_polarization.html %}

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
