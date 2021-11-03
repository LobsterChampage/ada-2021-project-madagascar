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