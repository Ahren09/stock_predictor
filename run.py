from lib.utils import preproc_pipeline
import pandas as pd
import os
import numpy as np

def main():

    os.chdir('data/Stocks/')
    filenames = np.sort(os.listdir('.'))

if __name__ == "__main__":
    main()
    '''
    data = pd.read_csv("<path/to/data>")
    train_set, validation_set, test_set = preproc_pipeline(data)
    '''


