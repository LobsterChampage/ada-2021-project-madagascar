import pandas as pd

def chunkify(filename, chunk_size, outputname):
    batch_no=1
    for chunk in pd.read_json(filename, chunksize=chunk_size, lines=True):
        chunk.to_csv('Data/' + outputname+str(batch_no) + '.csv', index=False)
        batch_no += 1

def writeToGitignore(files, amount):
    f = open('.gitignore', 'a')

    for i in range(1, amount):
        f.write(files+ str(i) +'.csv\n')
    f.close()