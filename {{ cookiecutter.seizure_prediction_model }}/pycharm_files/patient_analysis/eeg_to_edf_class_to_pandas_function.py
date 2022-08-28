""" a function designed to be called when an EEG dataset needs to be cleaned """

import mne
import warnings  # Hide all warnings here
import pandas as pd
import numpy as np


def load_pandas_data(filename):
    # When exporting data as a NumPy array or Pandas DataFrame, be sure to properly account for the unit of representation in your subsequent analyses.
    # with preload=True, contents are read into RAM

    mne.set_log_level('WARNING')
    warnings.simplefilter("ignore")

    patient = mne.io.read_raw(filename,preload=True)
    return patient.to_data_frame()


def get_seizure(seizure_set_df, start, end):
    """ return index locations for a given seizure set """

    start = np.where(seizure_set_df['time'] == start)
    end = np.where(seizure_set_df['time'] == end)
    seizure_set_df.loc[start[0][0]:end[0][0],'seizure = 1'] = 1
    return seizure_set_df


def prepare_df_for_analysis(preseizure_set, seizure_set):
    """ prepare the dataframe for the analysis """

    # seizure_set['time'] = seizure_set['time'] + 3600.000001
    p1 = pd.concat([preseizure_set, seizure_set],axis=0,ignore_index=True)
    p1.set_index('time',inplace=True)

    # left hemisphere location totals
    p1['outer_left_hemi_sum'] = p1[['FP1-F7','F7-T7','T7-P7','P7-O1']].sum(axis=1)
    p1['inner_left_hemi_sum'] = p1[['FP1-F3','F3-C3','C3-P3','P3-O1']].sum(axis=1)

    # right hemisphere location totals
    p1['outter_right_hemi_sum'] = p1[['FP2-F8','F8-T8','T8-P8-0','P8-O2']].sum(axis=1)
    p1['inner_right_hemi_sum'] = p1[['FP2-F4','F4-C4','C4-P4','P4-O2']].sum(axis=1)

    # center totals
    p1['center_line'] = p1[['FZ-CZ','CZ-PZ']].sum(axis=1)

    # left temple to rear totals
    p1['left_temple_to_left_rear'] = p1[['FZ-CZ','CZ-PZ']].sum(axis=1)

    # temple to temple totals
    p1['temple_to_temple'] = p1[['FT9-FT10']].sum(axis=1)

    # left temple to rear totals
    p1['right_temple_to_right_rear'] = p1[['FT10-T8','T8-P8-1']].sum(axis=1)

    # reorder columns for better visual early analysis
    new_cols = ['seizure = 1',
                'FP2-F4','FP1-F7','F7-T7','T7-P7','P7-O1','outer_left_hemi_sum',
                'FP1-F3','F3-C3','C3-P3','P3-O1','inner_left_hemi_sum',
                'FP2-F8','F8-T8','T8-P8-0','P8-O2','outter_right_hemi_sum',
                'FP2-F4','F4-C4','C4-P4','P4-O2','inner_right_hemi_sum',
                'FZ-CZ','CZ-PZ','center_line',
                'P7-T7','T7-FT9','left_temple_to_left_rear',
                'FT9-FT10','temple_to_temple',
                'FT10-T8','T8-P8-1','right_temple_to_right_rear']

    p1 = p1.reindex(columns=new_cols)
    return p1


def is_df_clean(df):
    """ Check if a dataframe is clean. """
    # is_na = df.count()
    for i in range(df.count().all().tolist()):
        if not i:
            return f"There are null values in {df.columns[i]}: Note: this is expected if column is 'seizures = 1' as most of the values are zero, but 1 where the seizure exist."
    # infinite = np.isinf(df).sum()
    for j in  np.isinf(df).sum().any().to_list():
        if not j:
            return f'There are infinite values in {df.columns[j]}'

