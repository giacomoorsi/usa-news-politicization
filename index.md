---
layout: default
title: Our beautiful data story
---

{% include_relative home/scroller-uikit.html %}

# Introduction
***
Democrats and Republicans: light and darkness for some, yin and yang for others.

The bipolarity that opposes Americans is not just a "ballot box thing", but rather an attitude ingrained in their day-to-day lives.
Even the channel they pick when switching on the TV, first thing in the morning, is part of this bigger picture.
Does landing on Fox News, CNN, or any other news source, have something to do with all of this?

With the help of data, *A LOT OF DATA*, we hope to highlight that indeed it does and wish to provide quantitative figures to support this hypothesis.

{% include_relative home/introduction/metrics.html %}

## Motivations

Why did we decide to do this project?

Over the recent years, we've been hearing a lot that there's an increasing
amount of politicization and polarization of news sources in the USA, meaning
that news feature politicians more often (one well-known politician in
particular) and that the articles often favour one side of the debate. During
and after the 2016 election, there were many articles about how people backing
Trump tended to read different news sources from people on the other side of the
political spectrum, news sources that reportendly tended to publish news pieces
containing hoaxes and conspiracy theories - for instance, [this article
](https://www.washingtonpost.com/news/the-fix/wp/2017/08/22/trump-backers-disturbing-reliance-on-hoax-and-conspiracy-theory-websites-in-1-chart/).
We can still read that some news sources (like [the Gateway
Pundit](https://www.reuters.com/investigates/special-report/usa-election-threats-gatewaypundit/))
are gaining a huge number of readers by helping Trump spread his claims about
the last election being "stolen". Donald Trump himself has been claiming that
many news sources are spreading "fake news" about him, with a disturbing
similarity to the "lügenpresse" accusations used by the Third Reich against
foreign press. It would appear that Mr. Trump's popularity mostly relies
on specific news sources.

Intuitively, we would expect news sources aligned with Trump to publish articles
that cite him and people from his political circle - Republicans, that is - more
than people that oppose him, i.e. Democrats.

So which sources are with Trump, and which ones are against him?

{% include_relative home/news-sources.html %}


# Background

_Briefly_ introduce our data sources (or should we do that at the end?):
- Pew research
- Similarweb
- Twitter

# Neat plots

We do neat plots in this section.

All our plots are interactive - points on the plot can be moused over to display
precise information and sometimes, even additional information not shown
otherwise (like the number of articles from a source in a particular year). You
can also explore the plots and filter what is shown by clicking on the labels on
the right-hand side of the plot.

We probably want to discuss methodology somewhere over here?
I.e. what it is we exactly calculated.

Our analysis is based on counting articles in which a quote from a given speaker
occurs.

## News sources

Previously we introduced some of our news sources and we said that we have some
intutions about the bias of those sources. It turns out that we're not the only
people with intuitions like that. Pew Research did a study of American public
asking what opinions did people have about various news sources, and this
research shows that our intuitions are actually reflected by what people think.

In the plot below we can see how popular the websites of our news sources are.
We can also see what people use the source for their political information, as
well as if the source is distrusted by people on the left or on the right.

{% include_relative plots/pew_similarweb.html %}

The following plot is similar, but it displays Twitter followers instead of
(non-unique) website views:

{% include_relative plots/pew_twitter.html %}

Based on this plot, we can already tell that people on the right read different
sources than the people on the left. We see that the right-wingers distrust more
news sources than the left-wingers; in fact, they distrust most of the sources with
mixed readers! 

Fun fact: there's actually one news source which is distrusted by people on the
left as well as people on the right. One needs to wonder who exactly reads the
Washington Examiner.

## Focus on specific politicians

We expected biased news sources to give more space to quotations from Trump.
Does our data confirm our suspicions?

{% include_relative plots/stats_trumpization.html %}

We cannot really see a pattern in which news sources quote Trump more. For
instance, both Fox News and Breitbart news quoted Trump around 10% of the time
in 2018 (which is still a lot, if you think about it!), but various news sources
(like The Hill, Politico, ABC News, The Washington Examiner) quoted him up to
twice as often.

Interestingly, we do see that many news sources started quoting Trump much more
often from 2017 onwards. USA Today is an exception to the this trend - they did
quote Trump more, but the increase was much smaller than for the other news
sources.

Out of curiosity, we also inspected how often Hillary Clinton, Trump's opponent
from the 2016 presidential election, was quoted by our sources:

{% include_relative plots/stats_hillarization.html %}

Interestingly, a reverse tend appears in this plot. Clinton was quoted about as
often as Trump in 2015 and 2016, but after the election year it would appear that
our sources lost the interest in her.

## Politicization

The following plot displays how politicized our news sources were in past years:

{% include_relative plots/stats_politicization.html %}

This plot (and all of our plots) is interactive; in particular, years on the
right can be clicked and double-clicked to display only some of them. Mousing
over the scattered points will display precise politicization at that point, as
well as the number of articles from that source in that particular year that our
dataset contains.

If we explore this plot, we see that the dataset doesn't really confirm our
intuitions. We expected right-biased sources to be more politicized than others,
but most sources appear to have about the same level of politicization.
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

However, we have uncovered some strange occurences in different years. In 2016,
the year that Donald Trump was elected, all news sources were left-polarized,
which wasn't the case in 2015. On the other hand, in years 2017 and 2018 (but
not 2017!) all news sources were right-polarized.

For completeness, the following plot displays the absolute value of polarization:

{% include_relative plots/stats_polarization.html %}

## Correlations

Show the correlation matrices.

Discuss how we found out that probably the Internet is left-wing-biased.


<!--
<div style="height:500px"></div>
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

<!--{% include_relative plotly/scatter_demo.html %}-->


<!--{% include_relative plotly/bar_demo.html %}-->
