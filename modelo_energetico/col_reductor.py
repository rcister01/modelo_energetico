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

def reduce_columns_period_sum(dataframe, columns, period_days):
    if 672 % (period_days*24) == 0:
        divition_length = period_days*24
        new_dataframe = pd.DataFrame()

        for column in columns:
            for i in range(int(672/divition_length)):
                new_dataframe[f'{column}_{i}'] = np.zeros(dataframe.shape[0])
                div_start = int(i * divition_length)
                for j in range(div_start, div_start + divition_length):
                    new_dataframe[f'{column}_{i}'] = new_dataframe[f'{column}_{i}'] + dataframe[f'{column}_{j}']

        return new_dataframe

    else:
        raise ValueError('28 días debe ser divisible por el período')


def reduce_columns_period_avg(dataframe, columns, period_days):
    if 672 % (period_days * 24) == 0:
        divition_length = period_days * 24
        new_dataframe = pd.DataFrame()

        for column in columns:
            for i in range(int(672 / divition_length)):
                new_dataframe[f'{column}_{i}'] = np.zeros(dataframe.shape[0])
                div_start = int(i * divition_length)
                for j in range(div_start, div_start + divition_length):
                    new_dataframe[f'{column}_{i}'] = new_dataframe[
                        f'{column}_{i}'] + dataframe[f'{column}_{j}'] / (672 / divition_length)

        return new_dataframe

    else:
        raise ValueError('28 días debe ser divisible por el período')

def total_q_hour(dataframe):
    new_dataframe = pd.DataFrame()
    for i in range(672):
        new_dataframe[f'Q_{i}'] = np.zeros(dataframe.shape[0])
        for j in range(i, dataframe.shape[1], 672):
            new_dataframe[f'Q_{i}'] = new_dataframe[f'Q_{i}'] + dataframe.iloc[:, j]

    return new_dataframe
