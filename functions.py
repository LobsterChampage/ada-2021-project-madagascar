import pandas as pd
import bz2
import os

def chunkify(filepath, chunk_size, outputname):
    """
    takes in the filepath as input
    takes in int as chunk_size
    outputname is what every output chunk starts their name as
    """
    batch_no=1
    for chunk in pd.read_json(filepath, chunksize=chunk_size, lines=True, compression='bz2'):
        output = 'Data/' + outputname+str(batch_no) + '.csv'

        chunk.to_csv(output, index=False)

        compressionLevel = 9
        source_file = output
        destination_file = output+ '.bz2'

        with open(source_file, 'rb') as data:
            compressed = bz2.compress(data.read(), compressionLevel)
        fh = open(destination_file, "wb")
        fh.write(compressed)
        fh.close()

        os.remove(output)

        batch_no += 1
        
        
        
def find_csv_filenames( path_to_dir, suffix=".csv" ):
    filenames = listdir(path_to_dir)
    return [ filename for filename in filenames if filename.endswith( suffix ) ]    



def get_elon_quotes():

    cd = 'Data\\' # Set working directory
    filenames = find_csv_filenames(cd) #Get filenames ending wih csv
    file_arr = np.array(filenames) # change list to numpy array
    N =len(filenames) #Number of chunks
    df1 = pd.read_csv("Data/" + file_arr[0]) # load first chunk
    df_all = df1[df1["speaker"]=='Elon Musk'] # Extract elon musk quotes from first chunk file
    # For loop through all chunks and concat data frames to have one data frame with all elon musk quotes
    for ii in range(1,N):
        name_2load = "Data/" + file_arr[ii]
        current_df = pd.read_csv(name_2load)
        df_elo_current = current_df[current_df["speaker"]=='Elon Musk']
        df_all = pd.concat([df_all, df_elo_current], axis=0)
    return df_all
    