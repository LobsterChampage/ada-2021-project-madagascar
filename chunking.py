from functions import chunkify

year = 2020
chunk_size = 200000

# Have the compressed quotebank file in /Data and name it: quotes-YEAR.json.bz2
# This can be parallellarized for different years

chunkify('Data/quotes-' + str(year) + '.json.bz2', chunk_size,'quotes-' + str(year) + '-')

# This will output a bunch of chunks files for the given year in the same /Data folder