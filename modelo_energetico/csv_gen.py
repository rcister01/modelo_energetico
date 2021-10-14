import pandas as pd
import numpy as np

def reduce_columns_sum(dataframe, columns, div_factor):
    if 24%div_factor==0:
        divition_length = int(24/div_factor)
        new_dataframe = pd.DataFrame()

        for column in columns:
            for i in range(div_factor):
                new_dataframe[f'{column}_{i}'] = np.zeros(dataframe.shape[0])
                div_start = int(i*divition_length)
                for j in range(div_start,div_start+divition_length):
                    for k in range(j, 672, 24):
                        new_dataframe[f'{column}_{i}'] = new_dataframe[f'{column}_{i}'] + dataframe[f'{column}_{k}']

        return new_dataframe

    else:
        raise ValueError('24 debe ser divisible por el factor de división')

def reduce_columns_avg(dataframe, columns, div_factor):

    if 24%div_factor==0:
        divition_length = int(24/div_factor)
        new_dataframe = pd.DataFrame()

        for column in columns:

            for i in range(div_factor):
                new_dataframe[f'{column}_{i}'] = np.zeros(dataframe.shape[0])
                div_start = int(i*divition_length)
                for j in range(div_start,div_start+divition_length):
                    for k in range(j, 672, 24):
                        new_dataframe[f'{column}_{i}'] = new_dataframe[f'{column}_{i}'] + dataframe[f'{column}_{k}']/(672/div_factor)

        return new_dataframe

    else:
        raise ValueError('24 debe ser divisible por el factor de división')
