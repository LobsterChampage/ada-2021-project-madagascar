# The Elon effect

Link to our data story: https://lobsterchampagne.github.io/project-madagascar-data-story/


# Project 3

1. Follow this to extract the relevant data
2. Data Exploring (Fredrik)
3. Sentiment analysis (Adham)
4. Regression (yfinance)
    4.1 Apple (yfinance)
    4.2 Ford (yfinance)
    4.3 Tesla (yfinance)
5. Regression (google_trends)
    4.1 Apple (google_trends)
    4.2 Ford (google_trends)
    4.3 Tesla (google_trends)
6. Observational study (Selima & Ferdinand)
7. Linear Regression (Selima)

Website (Fredrik)

## Abstract

Comments made by important people on companies could have a major impact on the business’s stock price and even net sales. For example, not so long-ago Elon musk tweeted that Tesla will stop accepting Bitcoin as a method of payment. Shortly after that, the bitcoin price dropped dramatically [[1]](https://www.cnbc.com/2021/05/13/bitcoin-btc-price-falls-after-tesla-stops-car-purchases-with-crypto.html). We think it would be interesting to extract, filter and tell a story about how Musk’s quotes such as this one and similar ones, affect companies' stock price and popularity. The idea of the project is to evaluate the impact Elon Musk has on the financial market and see whether his words have a big influence on the financial world or not.

## Research Questions

-   How does Musk impact the financial markets?
    -   Does Musk’s quotes impact the stock price?
    -   Is his negative quotes more hurtful than the gain from his positive ones?
    -   Does the company size play a role in the amount of change in the stock price?
-   Does Musk’s quotes affect the popularity of companies?
    -   Does the company size play a role?
-   Has his impact changed in any way?
    -   Do his quotes have a bigger impact now than what they had in prior years?
    -   How has Elon’s own popularity changed?

## Additional datasets

-   Google search (gsearch)
-   Yahoo finance (yfinance)
-   Google trends (pytrends)

We use gsearch [[2]](https://pypi.org/project/gsearch/) to find companies’ tickers by combining the company’s name and a Google search. The ticker is then used with the yfinance library [[3]](https://pypi.org/project/yfinance/) to find historical market data about the company. The related code is in the script; “financials.py”.

By using pytrends [[4]](https://pypi.org/project/pytrends/), a Google trends API, we can find out how the popularity of a company changes after Elon has mentioned it.

## Methods

#### Data extraction and processing [Milestone 2]

We first extracted Elon quotes from quotebank and combined them in a single folder for all years. We then used spacy [[5]](https://spacy.io/), to extract the names of organizations from the quotes. The full pipeline for this step is summarized in the figure.

![figure 1](figures/figure1.svg?raw=true)

#### Choose companies to analyze [Milestone 3]

Here we will choose 5-10 publicly listed companies to analyze. The list of the most mentioned companies is in the Main notebook.

#### Natural Language Processing sentiment analysis [Milestone 3]

We will carry out a Sentiment Analysis in order to identify and extract opinions within Elon’s quotes. We are thinking of using Vader [[6]](https://github.com/cjhutto/vaderSentiment) for this.

#### Check if Musk has an influence [Milestone 3]

In this part, we want to see if there is a causality between Elon quotes and the stock price and popularity of a company. In order to do so, we are going to carry out an posterior observational study of the stock price. For each company that we select, we will match it with other companies with the same observed covariates (the field of application etc.) but with no link to Musk. Therefore, we compare the change of the stock price of the company that is mentioned with others over a time interval. We will look into the effects of different time intervals.
For instance, we can compare Apple to an index of FAANG- or tech-companies. We will then model a normal distribution of the evolution of the stock price for the selected index, and then see if the company (Apple, in our example) follows the same distribution. This will be our null hypothesis and we will compute the p-value using a t-test (or Wilcoxon signed rank test), to find out whether to reject it or not. If our null hypothesis is rejected this means that Musk has an effect on the stock price. The same can be applied to look at the popularity.

#### Amount of influence. [Milestone 3]

For each company, we compute a variable Y that describes the stock price evolution each day for a given time lapse. With the Sentiment analysis of the quotes, we apply a regression model to Y as a function of the sentiment analysis X. X will be a variable that corresponds to the output of the sentiment analysis for the days around the quote and for other days it will be 0. We will apply a linear model to Y as a function of X. The problem here is that the number of parameters are not sufficient for our model to be fully trusted. So we are going to add variables that correspond to the evolution of stock indexes of similar companies. With our linear model we are going to make hypothesis tests on the value of the parameters of X say Bx. The null hypothesis will be that Bx = 0 to determine if the results of part 4 confirms our model fitting. And then we will estimate our variable to see how much the quote of Elon influenced the stock price.

## Proposed timeline

27.11 Decide on the companies that will be analyzed

28.11 Label the data with Natural Language Processing sentiment analysis

28.11 - 05.12 Carry out steps 4 and 5

05.12 - 15.12 Start drafting the data story

15.12 - 17.12 Finishing touches

## Organization within the team

Step 4 - Fredrik and Adham

Step 5 - Selima and Ferdinand

Data story - Whole team

## Organization of the repository

Load Project: This notebook contains all the necessary steps to extract Elon Musk’s quotes from Quotebank.

Main: This notebook contains the descriptive statistics of our data and a small demonstration of what we achieved so far.

functions.py: This file contains the helper functions we use to extract the data we need from quotebank.

financials.py: This file contains the functions used to extract the financial data of an organization.

Timings.md: The role of this markdown is to provide some indication on how much time is used on loading the data.

/Data: A folder with the data:

-   all-Elon Musk-quotes.csv.bz2 (all of Elon’s Quotes)
-   high-prob-Elon Musk-quotes.csv.bz2 (0.7+ probability)
-   org-lg-Elon Musk.csv.bz2 (dataset with organisations linked to quotes)
