# NewsChiller

A final project for my Computer Science Engineering Degree.
A news aggregator designed to improve (and to enable) news reading for people with news avoidance problems, stemming from anxiety, depression and various other issues. The aggregator implements basic features like adding feed sources, disabling and enabling article filtering and a simple search bar. Any opinions or suggestions regarding the app can be expressed in the questionnaire, filling out which is highly encouraged.
The classifier used in the app is a RoBERTa based binary classifier from simpletransformers. It's been trained on a small dataset of news headlines, that I have labeled either distressing or not distressing. The news headlines used in the dataset come from the News Category Dataset on Kaggle, and from 5 different categories: POLITICS, WELLNESS, ENTERTAINMENT, PARENTING and HEALTHY LIVING. The choice of category has been determined by both the need to incorporate the most common and most distressing categories of news, and to sufficiently diversify them, in order to increase the accuracy of eventual classification.
The application can presently be accessed after previous notice on http://1410076d.ngrok.io.

## HOW TO:

## SET THE FILTER

![](gifs/filter.gif)

## ADD A SOURCE

![](gifs/source.gif)

## SEARCH LATEST NEWS

![](gifs/search.gif)

## FILL OUT THE QUESTIONNAIRE (PLEASE)

![](gifs/questionnaire.gif)

## Backstory:

The idea for this project came to me last summer, during my first programming internship.
I had a huge case of impostor syndrome - and a bunch of other issues going on in my life.
Still, I wanted to stay on top of what's going on in the world - I mean, I'd been an aspiring
journalist myself, and so I perceived it as my personal responsibility.
So every day, I would leave my house an hour before the standup and use my commute to check on the news.
But every day, the general chaos of 2019 would turn out to be too much, and I would enter the meeting
with sweaty hands and a general sense of hopelessness.
Finally, I decided to skip the news in the morning - which implicitly also meant skipping the news in
the evening, since there was just too much going on - which quickly morphed into skipping the news
altogether.
It made much more relaxed, and happy, and ready to do my job. But also much more ignorant and isolated
from the world.

This website is not meant to be used as a way to tune out reality. It's a tool for people like me,
who may not be able to engage with it directly for some time, and who would probably have to resort
to news avoidance as a result.
