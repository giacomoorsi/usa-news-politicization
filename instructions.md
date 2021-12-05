---
layout: default
title: Instructions
---

# Instructions

Hello, and welcome! 

This is a website generate using `Jekyll` and GitHub Pages. 

`Jekyll` is a tool to build (static) websites in a simple way and it's perfectly integrated with GitHub that hosts the website without asking for money.

This page will be used to save some useful stuff to quickly understand how this stuff works. 

### Getting started
Once you clone the repository, you should work locally and test locally. Once you're stuff works, you should commit it and upload it. 

Committed stuff is live on this website (https://giacomoorsi.github.io/usa-news-politicization/)[https://giacomoorsi.github.io/usa-news-politicization/]

To test locally, install Jekyll. 
(read on the website on how to do it, it is pretty simple). 

Once you have done that, open this repository and type in the terminal

```bash
$ bundle install
```
It will install all the dependencies.  Now run the Jekyll server. 

```bash
$ jekyll serve
```
It will print the (local) URL that you can type on the browser to see live changes on the website. 


### Content
I am still exploring it. Everything is customizable. Therefore we can work parallely on the content (data story) and layout (CSS/HTML stuff). 

The main page is `index.md` and there you can only write in Markdown, which is automatically converted to `HTML`. 

To keep the code clear and simple and avoid shitty merges we will use several files even if we have a one-page website. 

To render the content included in another file: 
```bash
% include_relative path/to/file.md %
```
**You have to put `{` at the beginning of the command and `}` at the end** (If I wrote it in the code snippet it would have crashed, sorry)

Note that if you import a `.md` file, it will render it automatically BUT you can import also an `.html` file!


C'est ça, have fun. 

[Go back to home](/)