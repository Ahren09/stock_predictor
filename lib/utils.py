def preprocess(data):
    """
    This class takes in a pandas dataframe and cleans it
    """
    raise NotImplementedError

def shape_for_keras(data):
    """
    This class takes in a pre_processed pandas dataframe and cleans it
    """
    raise NotImplementedError

def train_val_test_split(data, train_size=0.6, test_size=0.2):
    """
    Returns three arrays. 3/4 data (train_set), 1/8 (validation_set),
    1/8 (test_set)
    """
    data_size = len(data)
    end_train = int(data_size*train_size)
    end_val = int(data_size*(train_size+test_size))
    train = data.iloc[:end_train]
    val = data.iloc[end_train:end_val]
    test = data.iloc[end_val:]
    return train, val, test

def generate_ta(data):
    """
    Runs ta on a dataset
    """
    raise NotImplementedError

def preproc_pipeline(data):
    """
    Preprocesses a dataset to be used for training. 
    """
    # Preprocess
    data = preprocess(data)

    # Optional --> run a technical analysis on it and add more features
    data = generate_ta(data)
    
    # Split
    train_set, validation_set, test_set = train_val_test_split(data)
    
    # Set up for Keras
    train_set = shape_for_keras(train_set)
    validation_set = shape_for_keras(validation_set)
    test_set = shape_for_keras(test_set)

    # We could save this to csv.
    return train_set, validation_set, test_set
