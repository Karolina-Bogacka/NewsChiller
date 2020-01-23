# NewsChiller

A final project for my Computer Science Engineering Degree.
A news aggregator designed to improve (and to enable) news reading for people with news avoidance problems, stemming from anxiety, depression and various other issues. The aggregator implements basic features like adding feed sources, disabling and enabling article filtering and a simple search bar. Any opinions or suggestions regarding the app can be expressed in the questionnaire, filling out which is highly encouraged.
The classifier used in the app is a RoBERTa based binary classifier from simpletransformers. It's been trained on a small dataset of news headlines, that I have labeled either distressing or not distressing. The news headlines used in the dataset come from the News Category Dataset on Kaggle, and from 5 different categories: POLITICS, WELLNESS, ENTERTAINMENT, PARENTING and HEALTHY LIVING. The choice of category has been determined by both the need to incorporate the most common and most distressing categories of news, and to sufficiently diversify them, in order to increase the accuracy of eventual classification.

## HOW TO:

###SET THE FILTER

![](gifs/filter.gif)

###ADD A SOURCE

![](gifs/source.gif)

###SEARCH LATEST NEWS

![](gifs/search.gif)

###FILL OUT THE QUESTIONNAIRE (PLEASE)

![](gifs/questionnaire.gif)
