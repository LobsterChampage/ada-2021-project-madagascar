# The Elon effect - How Elon Musk’s quotes impact the world and financial markets

## Abstract

There is no doubt that Elon Musk has had an impact on the financial market, and we find his impact rather interesting. In this project, we will look at how quotes or comments about businesses and companies, made by important people, impact the companies' stock price and popularity. For this milestone, we will limit the scope to only investigate the quotes made by Musk, but we may change this for milestone 3. As an example, quite recently Musk made a tweet stating that Tesla will stop accepting Bitcoin as a payment method. Shortly after the bitcoin price dropped dramatically. We think it would be interesting to extract, filter and tell a story about how Musk’s quotes such as this one and similar ones, affect the companies/products' stock price and popularity. The idea of the project is to evaluate the impact Musk has on the financial market and see whether his words influence the financial world or not.

## Research Questions

As mentioned, the goal for this project is to see and quantify how Musk impacts both the financial market as well as whether he has an impact on the popularity of these companies. The research questions are therefore linked with these subjects.

-   How does Musk impact the financial markets? (Yahoo finance)
    -   Does Musk’s quotes impact the stock price?
    -   Is his negative quotes more hurtful than the gain from his positive ones?
    -   Does the company size play a role in the amount of change in the stock price?
-   Does Musk’s quotes affect the popularity of companies? (pytrends)
    -   Does the company size play a role?
-   Has his impact changed in any way?
    -   Does his quotes have a bigger impact now than what they had in prior years?
    -   How has Elon’s own popularity changed? (pytrends)

## Additional datasets

-   Google search (gsearch)
-   Yahoo finance (yfinance)
-   Google trends (pytrends)

After installing and importing gsearch and yfinance, you are able to find the company’s ticker by combining the company’s name and a Google search. The ticker is like a stock-Id. One could then use the ticker combined with methods from yfinance to find information and historical market data about the company. The related code is in the script; “financials.py”. By combining this code with the quotes, one is able to see how a particular stock developed before and after being mentioned.

By using pytrends, a Google trends API, you can find out how the popularity of a company changes after Elon has mentioned it. Google trends gives relative information regarding the popularity of Google searches, and we will use this to look at how this has changed for a specific company after Elon mentions it.

## Methods

#### Data extraction and processing [Finished in Milestone 2]

We first extracted Elon quotes from quotebank and combined them in a single folder for all years (lLoad Project notebook). We then used spacy, natural language processing, to extract the names of organizations from the quotes (and dropped quotes that don’t mention any organizations). The full pipeline for this step is summarized in figure 1.

#### Choose 5-10 public listed companies to analyze [Milestone 3]

Here we will choose 5-10 companies to analyze, our selection criteria are based on the most mentioned publicly listed companies (according to Elon). This list is in the Main notebook. The list could change if the quotes for a certain company turn out to be irrelevant (neutral quotes).

#### Natural Language Processing sentiment analysis [Milestone 3]

We will carry out a Sentiment Analysis in order to identify and extract opinions within Elon’s quotes. The role of this step is to label the quotes to either positive or negative.

#### Check if Musk has an influence (yfinance, pytrends) [Milestone 3]

In this part, we want to see if there is a causality between Elon quotes and the stock price and popularity of a company. In order to do so, we are going to carry out an observational study of the stock price. For each company that we select, we will match it with others with the same covariates (for instance here, the notoriety, the field of application…) but with no link with Musk (meaning we need that Elon hasn’t talked about these organizations). Therefore, we compare the change of the stock price of the company that is mentioned in the quotes with others over a time interval. It would be interesting to look at different time intervals as well. Then we can plot this and show a trend figure to compare the stock with the other companies. For instance, we can compare Apple to Microsoft as well as the other FAANG-companies. We can then model a normal distribution with the evolution of the stock price for the selected organizations, and then see if the company (Apple, in our example) follows the same distribution. This will be our null hypothesis and we will compute the p-value to find out if whether to reject it or not. If our null hypothesis is rejected this means that Musk has an effect on the stock price. The same can be applied to look at the popularity.

#### Amount of influence. [Milestone 3]

For each company, we compute a random variable Y that describes the stock price evolution each day for a given time lapse. Thanks to the Sentiment analysis of the quotes, we apply a regression model to Y as a function of the sentiment analysis X. X will be a random variable that for 2 days before,1 after and the same day of the quotes will correspond to the sentiment analysis (1 if it’s positive, -1 if it’s negative) and for the other days will be equal to 0. We will apply a linear model to Y as a function of X. The problem here is that the number of parameters are not sufficient for our model to be fully trusted. So we are going to add variables that correspond to the evolution of indexes of similar companies. Now that we have our linear model. We are going to make hypothesis tests on the value of the parameters of X say Bx. The null hypothesis will be that Bx = 0 to determine if the results of part 4 confirms our model fitting. And then we will estimate our variable to see how much the quote of Elon influenced the stock price.

## Proposed timeline

27.11 Start working on Milestone 3 and decide the companies that will be analyzed

28.11 Label the data Natural Language Processing sentiment analysis

28.11 - 05.12 Carry out steps 4 and 5

05.12 - 15.12 Start drafting the data story

15.12 - 17.12 Finishing touches

## Organization within the team

Step 4 - Fredrik and Adham
Step 5 - Selima and Ferdinand
Data story - Whole team
