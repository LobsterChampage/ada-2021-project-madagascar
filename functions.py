import pandas as pd
import bz2
import os
import numpy as np
import time
import spacy
import glob

def chunkify(filepath, chunk_size, outputname, timing=False):
    """
    takes in the filepath as input
    takes in int as chunk_size
    outputname is what every output chunk starts their name as
    timing is per chunk for benchmarks
    """
    batch_no = 1
    for chunk in pd.read_json(filepath, chunksize=chunk_size, lines=True, compression='bz2'):
        # Taking the time of loading each chunk
        if timing:
            before = time.time()

        output = 'Data/' + outputname + str(batch_no) + '.csv'

        chunk.to_csv(output, index=False)

        compression_level = 9
        # Source file for bz2 comrpession
        source_file = output
        destination_file = output + '.bz2'

        with open(source_file, 'rb') as data:
            # Reads the content of the file and makes a compressed copy
            compressed = bz2.compress(data.read(), compression_level)
        fh = open(destination_file, "wb")
        # Make a new compressed file with compressed content
        fh.write(compressed)
        fh.close()

        # Removes the .csv file to save space
        os.remove(output)

        if timing:
            after = time.time()
            print(after - before, 's')

        batch_no += 1

def find_csv_filenames(path_to_dir, year):
    """
    finds all chunkfiles that belongs to a given year and is in a given directory
    """
    filenames = os.listdir(path_to_dir)
    return [filename for filename in filenames if filename.startswith("quotes-" + str(year) + "-")]    

def get_quotes(speaker, year, timing=False):
    """
    returns the dataset with only quotes from the given speaker from the files of a given year
    timing for the whole function for benchmarks
    """
    if timing:
        before = time.time()

    cd = 'Data/' # Set working directory
    filenames = find_csv_filenames(cd, year) #Get chunks from a given year
    file_arr = np.array(filenames) # change list to numpy array
    N = len(filenames) #Number of chunks
    df1 = pd.read_csv(cd + file_arr[0]) # load first chunk
    df_all = df1[df1["speaker"]==speaker] # Extract elon musk quotes from first chunk file
    # For loop through all chunks and concat data frames to have one data frame with all elon musk quotes
    for i in range(1,N):
        name_2load = cd + file_arr[i]
        current_df = pd.read_csv(name_2load)
        df_elo_current = current_df[current_df["speaker"]==speaker]
        df_all = pd.concat([df_all, df_elo_current], axis=0)

    if timing:
        after = time.time()
        print(after - before, 's')

    return df_all

def make_csv(dataFrame, speaker, year, compression='bz2'):
    """
    create a compressed csv of a dataframe of quotes for a speaker and a year
    """
    dataFrame.to_csv('Data/' + speaker + '-quotes-' + str(year) + '.csv.' + compression)

def create_org_df(spacy_model, df, timing=False):
    """
    create a dataframe with the organizations from the quotes in a dataframe
    timing for the whole function including loading spacy_model
    """
    if timing:
        before = time.time()

    spacy_nlp = spacy.load(spacy_model)

    #gets filled with dictionaries for rows
    quote_list = []

    for i in range(0, df.shape[0]):
        quote = df.iloc[i]['quotation']
        # Extracts the quote and looks at it with nlp
        doc = spacy_nlp(quote)

        for element in doc.ents:
            # If a token gets categorized as ORG then it makes a dictionary for quote_list
            if element.label_ == 'ORG':
                quote_list.append({
                    'ORG' : element,
                    'date' : df.iloc[i]['date'],
                    'numOccurrences' : df.iloc[i]['numOccurrences'],
                    'quotation' : df.iloc[i]['quotation'],
                    'quoteID' : df.iloc[i]['quoteID'],
                    'probas' : df.iloc[i]['probas']})

    # Turns quote_list into a DataFrame with keys as columns
    org_df = pd.DataFrame.from_dict(quote_list)

    if timing:
        after = time.time()
        print(after - before, 's')

    return org_df

def combining_yearly_quotes(speaker):
    # Load all of the speakers quotes of all years
    path = 'Data/'
    # The speakers data in Data/ should be 'SPEAKER-quotes-YEAR.csv.bz2'
    # This will only grab files starting with the speaker's name
    all_files = glob.glob(path + speaker +"*.bz2")

    # Combine all speakers quotes from all the years 
    li = []
    for filename in all_files:
        df = pd.read_csv(filename)
        li.append(df)

    frame = pd.concat(li, axis=0, ignore_index=True) 

    # Save the extra column with original indicies before droping it
    indices_pd = frame['Unnamed: 0']
    numpy_array_indices_pd = indices_pd.to_numpy()
    numpy_array_indices_pd

    # Drop the extra column with original indicies
    frame = frame.drop(columns="Unnamed: 0")
    # Chnage new indicies with original indicies
    frame.index = numpy_array_indices_pd

    frame.to_csv(path + 'all-' + speaker + '-quotes.csv.bz2', compression='bz2')