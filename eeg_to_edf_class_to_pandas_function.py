"""functions  designed to be called when an EEG dataset needs to be cleaned and organized for capstone 2 project """

import mne
import warnings  # Hide all warnings here
import pandas as pd
import numpy as np


def load_pandas_data(filename):
    """ converts raw data from a .edf file to a dataframe and eliminates known warnings"""

    mne.set_log_level('WARNING')
    warnings.simplefilter("ignore")

    patient = mne.io.read_raw(filename, preload=True)
    return patient.to_data_frame()


def prepare_df_for_analysis(preseizure_set, seizure_set, start, end):
    """

    Prepares a master dataframe for the analysis.
    :param preseizure_set: a full EEG set without a seizure
    :param seizure_set: an EEG with a seizure and then truncated after the seizure
    to reduce runtime
    :param start: start time of the seizure as listed in the summary file from Children's hospital data set
    :param end: end time of the seizure as listed in the summary file from Children's hospital data set
    :return: a dataframe

    """

    preseizure_set.set_index('time', inplace=True)
    seizure_set.set_index('time',inplace=True)

    preseizure_set['seizure = 1'] = 0
    seizure_set['seizure = 1'] = 0

    seizure_set.loc[start : end, 'seizure = 1'] = 1

    patient = pd.concat([preseizure_set, seizure_set],axis=0,ignore_index=True)

    # left hemisphe®re location totals
    patient['outer_left_hemi_sum'] = patient[['FP1-F7','F7-T7','T7-P7','P7-O1']].sum(axis=1)
    patient['inner_left_hemi_sum'] = patient[['FP1-F3','F3-C3','C3-P3','P3-O1']].sum(axis=1)

    # right hemisphere location totals
    patient['outter_right_hemi_sum'] = patient[['FP2-F8','F8-T8','T8-P8-0','P8-O2']].sum(axis=1)
    patient['inner_right_hemi_sum'] = patient[['FP2-F4','F4-C4','C4-P4','P4-O2']].sum(axis=1)

    # center totals
    patient['center_line'] = patient[['FZ-CZ','CZ-PZ']].sum(axis=1)

    # left temple to rear totals
    patient['left_temple_to_left_rear'] = patient[['FZ-CZ','CZ-PZ']].sum(axis=1)

    # temple to temple totals
    patient['temple_to_temple'] = patient[['FT9-FT10']].sum(axis=1)

    # left temple to rear totals
    patient['right_temple_to_right_rear'] = patient[['FT10-T8','T8-P8-1']].sum(axis=1)

    # reorder columns for better visual early analysis
    new_cols = ['seizure = 1',
                'FP1-F7','F7-T7','T7-P7','P7-O1','outer_left_hemi_sum',
                'FP1-F3','F3-C3','C3-P3','P3-O1','inner_left_hemi_sum',
                'FP2-F8','F8-T8','T8-P8-0','P8-O2','outter_right_hemi_sum',
                'FP2-F4','F4-C4','C4-P4','P4-O2','inner_right_hemi_sum',
                'FZ-CZ','CZ-PZ','center_line',
                'P7-T7','T7-FT9','left_temple_to_left_rear',
                'FT9-FT10','temple_to_temple',
                'FT10-T8','T8-P8-1','right_temple_to_right_rear']

    patient = patient.reindex(columns=new_cols)
    patient.set_index(create_int_index(patient),inplace=True)

    locations = seizure_location(patient)
    patient = patient.iloc[: locations[1] + 1,:]

    return patient


def is_df_clean(df):
    """ Check if a dataframe is clean. """
    for i in range(df.count().all().tolist()):
        if not i:
            return f"There are null values in {df.columns[i]}: Note: this is expected if column is 'seizures = 1' as most of the values are zero, but 1 where the seizure exist."
    # infinite = np.isinf(df).sum()
    for j in  np.isinf(df).sum().any().to_list():
        if not j:
            return f'There are infinite values in {df.columns[j]}'


def create_int_index(df):
    """Create and return an index that is `int` based"""
    return np.linspace(0, len(df), len(df), dtype=int)


def seizure_location(df):
    """Return the index locations of the seizure."""

    seizure_location = df.index[df['seizure = 1'] != 0].tolist()
    # seizure_start, seizure_end = seizure_location[0], seizure_location[-1]

    return seizure_location[0], seizure_location[-1]


def model_dataframe(df):
    """Return a dataframe with the model-ready features """

    df_copy = df.copy()


    df_copy.drop(['seizure = 1', 'outer_left_hemi_sum','inner_left_hemi_sum','outter_right_hemi_sum','inner_right_hemi_sum','center_line','left_temple_to_left_rear', 'temple_to_temple', 'right_temple_to_right_rear'], axis=1, inplace=True)

    return df_copy

