from functions import get_quotes
from functions import make_csv

year = 2020
speaker = 'Elon Musk'

# The data needs to be chunked

df = get_quotes(speaker, year)
make_csv(df, speaker, year, compression='bz2')

# This will output a single zipped csv file with only quotes from the speaker