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

## Dairy 2

After dairy 1 is done we can now move all the quotebank dataset into a separate folder (outside Git or in what we called /backup in /Data). Then we can push all the Elon Musk quote datasets to git (because they are now small enough to be shared).

This makes it easier for everyone to download without going through all the hassle above.

We still have to be careful not to make unforseen changes to the dataset, but we also have the option to handle the data and filter it.
