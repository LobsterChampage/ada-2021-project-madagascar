import pandas as pd

def chunkify(filepath, chunk_size, outputname):
    """
    takes in the filepath as input
    takes in int as chunk_size
    outputname is what every output chunk starts their name as
    """
    batch_no=1
    for chunk in pd.read_json(filepath, chunksize=chunk_size, lines=True, compression='bz2'):
        chunk.to_csv('Data/' + outputname+str(batch_no) + '.csv', index=False)
        batch_no += 1

def writeToGitignore(files, amount):
    """
    This is to bulk write to gitignore for our data files
    """
    f = open('.gitignore', 'a')

    for i in range(1, amount):
        f.write(files+ str(i) +'.csv\n')
    f.close()