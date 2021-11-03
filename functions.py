import pandas as pd
import bz2
import os
import numpy as np

def chunkify(filepath, chunk_size, outputname):
    """
    takes in the filepath as input
    takes in int as chunk_size
    outputname is what every output chunk starts their name as
    """
    batch_no = 1
    for chunk in pd.read_json(filepath, chunksize=chunk_size, lines=True, compression='bz2'):
        output = 'Data/' + outputname + str(batch_no) + '.csv'

        chunk.to_csv(output, index=False)

        compressionLevel = 9
        # Source file for bz2 comrpession
        source_file = output
        destination_file = output + '.bz2'

        with open(source_file, 'rb') as data:
            # Reads the content of the file and makes a compressed copy
            compressed = bz2.compress(data.read(), compressionLevel)
        fh = open(destination_file, "wb")
        # Make a new compressed file with compressed content
        fh.write(compressed)
        fh.close()

        # Removes the .csv file to save space
        os.remove(output)

        batch_no += 1

def find_csv_filenames(path_to_dir, year):
    filenames = os.listdir(path_to_dir)
    return [filename for filename in filenames if filename.startswith("quotes-" + str(year) + "-")]    

def get_elon_quotes(year):
    cd = 'Data/' # Set working directory
    filenames = find_csv_filenames(cd, year) #Get chunks from a given year
    file_arr = np.array(filenames) # change list to numpy array
    N = len(filenames) #Number of chunks
    df1 = pd.read_csv(cd + file_arr[0]) # load first chunk
    df_all = df1[df1["speaker"]=='Elon Musk'] # Extract elon musk quotes from first chunk file
    # For loop through all chunks and concat data frames to have one data frame with all elon musk quotes
    for i in range(1,N):
        name_2load = cd + file_arr[i]
        current_df = pd.read_csv(name_2load)
        df_elo_current = current_df[current_df["speaker"]=='Elon Musk']
        df_all = pd.concat([df_all, df_elo_current], axis=0)
    return df_all