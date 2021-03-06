import pandas as pd
import numpy as np
from sklearn import preprocessing as prep


def feature_selection (df, features):
        
    dataset_fs = pd.DataFrame(columns = df.columns)    
    droplist = [i for i in df.columns if i not in features]
    dataset_fs = df.drop(droplist, axis = 1, inplace = False) 
    dataset_fs['Inverter avg.'] = df[[
            'CS101 : Sys 1 inverter 1 cabinet temp.',
            'CS101 : Sys 1 inverter 2 cabinet temp.', 
            'CS101 : Sys 1 inverter 3 cabinet temp.', 
            'CS101 : Sys 1 inverter 4 cabinet temp.', 
            'CS101 : Sys 1 inverter 5 cabinet temp.', 
            'CS101 : Sys 1 inverter 6 cabinet temp.', 
            'CS101 : Sys 1 inverter 7 cabinet temp.',
            'CS101 : Sys 2 inverter 1 cabinet temp.', 
            'CS101 : Sys 2 inverter 2 cabinet temp.',  
            'CS101 : Sys 2 inverter 3 cabinet temp.',
            'CS101 : Sys 2 inverter 4 cabinet temp.']].mean(axis=1)
    dataset_fs['Inverter std'] = df[[
            'CS101 : Sys 1 inverter 1 cabinet temp.',
            'CS101 : Sys 1 inverter 2 cabinet temp.', 
            'CS101 : Sys 1 inverter 3 cabinet temp.', 
            'CS101 : Sys 1 inverter 4 cabinet temp.', 
            'CS101 : Sys 1 inverter 5 cabinet temp.', 
            'CS101 : Sys 1 inverter 6 cabinet temp.', 
            'CS101 : Sys 1 inverter 7 cabinet temp.',
            'CS101 : Sys 2 inverter 1 cabinet temp.', 
            'CS101 : Sys 2 inverter 2 cabinet temp.',  
            'CS101 : Sys 2 inverter 3 cabinet temp.',
            'CS101 : Sys 2 inverter 4 cabinet temp.']].std(axis=1)
    
    # Normalize the data
    temp = dataset_fs.values
    x_scaled = prep.normalize(temp)
    normalized_dataset_fs = pd.DataFrame(x_scaled, columns = dataset_fs.columns)
    
    return normalized_dataset_fs