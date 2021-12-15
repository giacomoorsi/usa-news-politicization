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

The following plot displays how politicized our news sources were in past years:

{% include_relative plots/stats_politicization.html %}

This plot (and all of our plots) is interactive; in particular, years on the
right can be clicked and double-clicked to display only some of them. Mousing
over the scattered points will display precise politicization at that point, as
well as the number of articles from that source in that particular year that our
dataset contains.

If we explore this plot, we see that the dataset doesn't really confirm our
intuitions. Most sources appear to have mostly the same level of politicization.
Both Fox News and Breitbart are commonly thought of as right-wing-biased.
We may expect that they are publishing more articles quoting politicians (specifically,
right-wing politicians) than other sources. However, this is not what we can see
based on our dataset. The Huffington Post is often thought of as left-wing-biased
(Breitbart News was conceived of as "The Huffington Post of the right"), yet it is
also not significantly more politicized than other news sources.

The most politicized news sources are Politico, The Hill and Washington
Examiner. Twe first two report on political news, so in hindsight it comes as no
surprise that they quotations are mostly attributed to politicians. We do not
have a clear reason for Washington Examiner being as politicized as our data
indicates. It stands out as the only news source we examine that is distrusted
by both the left and the right, but that alone does not explain the politicization.

The least politicized news sources are USA Today and New York Post. USA Today is
a middle-market newspaper catering to readers that like both entertainment as
well as coverage of important news events, while New York Post is a tabloid.

## Polarization

The following plot displays plot displays how polarized our news sourced were:

{% include_relative plots/stats_polarization_sgn.html %}

The polarization of a source is positive if it quoted more right-wing
politicians than left-wing ones, negative in the reverse case.

Again, at a glance it seems we do not find what we were looking for in this
plot. Breitbart News is as right-polarized as Business Insider, a source with
left-wing readership but trusted by both sides of the political spectrum.
Similarly, Fox News is as right-polarized as Vox, a website often cited as
left-biased and distrusted by the right. The Huffington Post is as
left-polarized as ABC News, and The Wall Street Journal, with mixed readers and
trusted by both the left and the right, is more left-polarized than either.

However, we can uncover some strange occurences in different years. In 2016, the year
that Donald Trump was elected, all news sources were left-polarized. On the other hand,
in years 2018 and 2019 all news sources were right-polarized.

TODO: how to explain this? Compare with Trumpization during those years?

For completeness, the following plot displays the absolute value of polarization:

{% include_relative plots/stats_polarization.html %}

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
