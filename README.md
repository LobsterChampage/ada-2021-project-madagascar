# Project

## Installations and updates

We will use pandas and spacy

Remember to update your libraries either with conda or pip.

To install spacy with pip:

```
pip install spacy
```

We will use different models for spacy which is downloaded in the terminal like this:

```
python -m spacy download en_core_web_sm
python -m spacy download en_core_web_md
python -m spacy download en_core_web_lg
```

## Setup

We are working in jupyter notebook with local data.

Every member has their own private notebook called privateNotebook.ipynb in the main folder. This file is gitignored to avoid the hassle of git conflicts if we had our notebooks public and peeked into eachothers notebooks.

Every member has to load in their own data. This can be done by downloading the compressed files from: [Drive](https://drive.google.com/drive/folders/1R-GVIdxU3jkQb5zU0uG9044Vynh9nYR1)

We have the data in a gitignored /Data folder.
The .bz2 files should be named 'quotes-YEAR.json.bz2' with YEAR as the year of the quotes.

We work with chunks of the data to make it more managable, but everyone has to name and size their chunks the same for our code to work for all.

For chunking one of the bz2 files we use our chunkify function in functions.py.

THe chunks should be called 'quotes-YEAR-NUMBER.csv.bz2' with YEAR as the year and NUMBER as the number it gets from our chunkify function.

This is the code to chunkify 2020:

```py
from functions import chunkify

chunkify('Data/quotes-2020.json.bz2',100000,'quotes-2020-')
```

Remember to set the size to 100000 and output `quotes-2020-` with the `-` at the end. And remember to output in `Data`.

## Dairy 1

We have now made a smarter pipeline.

Our functions goes into `functions.py` and we can chunk the dataset with `chunking.py` and extract the quotes we need with `extracting.py`.

#### To summarize all the user needs to do:

-   put the 6 quotebank files in /Data and name them accordingly `quotes-YEAR.json.bz2` (Downloading can take ca. 1 hour)
-   run the code in `chunking.py` (10 min - 1 hour 30 min per file, but can be parallellarized)
-   run the code in `extracting.py` (ca 3 min - 25 min, but can be parallellarized)
-   use the 6 new small `SPEAKER-quotes-YEAR.csv.bz2`

This only have to be done once and then the files can be shared within the group.

## P2: Project proposal and initial analyses

When you are done with Homework 1, you will continue to work on the next project milestone. In Milestone 2, together with your team members, you will agree on, and refine, your project proposal. Your first task is to select a project. Even though we provide the main dataset for you to use, it is your responsibility to check that what you propose is feasible given the data (including any additional data you might bring in yourself), and to perform initial analyses.

Note that we will support you in working with Quotebank data from 2015 to 2020, inclusive. You are, of course, free to use the data from other years if you wish so, but only if you are feeling adventurous! We have also prepared for you a Google Colab notebook with code to get you started with loading the dataset.

The goal of this milestone is to intimately acquaint yourself with the data, preprocess it and complete all the necessary descriptive statistics tasks. We expect you to have a pipeline in place, fully documented in a notebook, and show us that you have clear project goals.

When describing the relevant aspects of Quotebank data, and any other datasets you may intend to use, you should in particular show (non-exhaustive list):

-   That you can handle the data in its size.
-   That you understand what’s in the data (formats, distributions, missing values, correlations, etc.).
-   That you considered ways to enrich, filter, transform the data according to your needs.
-   That you have a reasonable plan and ideas for methods you’re going to use, giving their essential mathematical details in the notebook.
-   That your plan for analysis and communication is reasonable and sound, potentially discussing alternatives to your choices that you considered but dropped.
-   We will evaluate this milestone according to how well these steps have been done and documented, the quality of the code and its documentation, the feasibility and critical awareness of the project. We will also evaluate this milestone according to how clear, reasonable and well thought-through the project idea is. Please use the second milestone to really check with us that everything is in order with your project (idea, feasibility, etc.) before you advance too much with the final Milestone 3! There will be project office hours dedicated to helping you.

You will work in your project GitHub repository that will be created by using the link we provide. Follow this link to create your public repository dedicated to the project.

The repository will automatically be named ada-2021-project-<your_team_name>. By the Milestone 2 deadline, each team should have a single public GitHub repo under the epfl-ada GitHub organization, containing the project proposal and initial analysis code.

External sources for enriching Quotebank data: To help you on your Quotebank ADAventure, we would like to provide you access to additional metadata about the speakers in the Quotebank dataset. This information is available for ~9M unique Wikidata entities (identified with their QIDs) as a .parquet file named speaker_attributes.parquet via Google Drive. Note that the schema of speaker_attributes.parquet is also available within the same Google Drive folder that hosts the parquet file. You can load this file as a pandas dataframe using df = pd.read_parquet(<path_to_file>). Pandas requires pyarrow to read parquet files, which can be installed using conda install pyarrow -c conda-forge.

Additionally, we also provide you with sample code (available in the same Google Drive folder) along with instructions on how to execute it, which was used to extract the aforementioned information about speakers from the Wikidata knowledge base. You are free to extend the provided code to extract additional information about speakers than what is already provided by us. Please be advised that the Wikidata dumps (you need to use the wikidata-<timestamp>-all.json.gz file) are usually very large (~100GB) in size, so don’t leave it until the last minute to parse/extract information from this resource. For additional information about Wikidata dumps and how to download them, please see this Wiki page.

## P2 deliverable (done as a team): GitHub repository with the following:

Readme.md file containing the detailed project proposal (up to 1000 words). Your README.md should contain:

-   Title
-   Abstract: A 150 word description of the project idea and goals. What’s the motivation behind your project? What story would you like to tell, and why?
-   Research Questions: A list of research questions you would like to address during the project.
-   Proposed additional datasets (if any): List the additional dataset(s) you want to use (if any), and some ideas on how you expect to get, manage, process, and enrich it/them. Show us that you’ve read the docs and some examples, and that you have a clear idea on what to expect. Discuss data size and format if relevant. It is your responsibility to check that what you propose is feasible.
-   Methods
-   Proposed timeline
-   Organization within the team: A list of internal milestones up until project Milestone 3.
-   Questions for TAs (optional): Add here any questions you have for us related to the proposed project.
-   Notebook containing initial analyses and data handling pipelines. We will grade the correctness, quality of code, and quality of textual descriptions.

# Abstract

Quotes or comments made by important people on businesses and companies could have a major impact on the business’s stock price and even net sales. For example, not so long-ago Elon musk made a tweet that Tesla will stop accepting Bitcoin as a method of payment. Shortly after that, the bitcoin price dropped dramatically. It would be interesting to extract Elon Musk’s quotes and filter those that are related to other companies or products and see how these quotes affected the companies/products' stock price. The idea of the project is to evaluate the impact Elon musk has on the financial market and see if whether his words have so much influence on the financial world or not.
