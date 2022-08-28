


"""
edf file info:
file length: 1
signals sampled: 256 samples/second with 16 bit resolution
EEG signals: 23 in most cases
Dummy Signals: named "-" to obtain easier to read display format: ignore them
Summary.txt contains elapsed time (seconds) for each seizure contained therein

"""

# def load_pandas_data(filename):
#     # When exporting data as a NumPy array or Pandas DataFrame, be sure to properly account for the unit of representation in your subsequent analyses.
#     # with preload=True, contents are read into RAM
#     patient = mne.io.read_raw(filename,preload=True)
#     return patient.to_data_frame()


#
# # seizure occurs from 2996 < time < 3036, isolate and change 'seizure = 1' values to 1
# start = np.where(p1_seizure_set['time'] == 2996)
# end = np.where(p1_seizure_set['time'] == 3036)
# p1_seizure_set.loc[start[0][0]:end[0][0], 'seizure = 1'] = 1
#
# # concate the dfs, set index and id locations where the seizure occurs
# p1_seizure_set['time'] = p1_seizure_set['time'] + 3600.000001
# p1 = pd.concat([p1_preseizure, p1_seizure_set], axis=0, ignore_index=True)
# p1.set_index('time', inplace=True)
#
# # left hemisphere location totals
# p1['outer_left_hemi_sum'] = p1[['FP1-F7', 'F7-T7', 'T7-P7', 'P7-O1']].sum(axis=1)
# p1['inner_left_hemi_sum'] = p1[['FP1-F3', 'F3-C3', 'C3-P3', 'P3-O1']].sum(axis=1)
#
# # right hemisphere location totals
# p1['outter_right_hemi_sum'] = p1[['FP2-F8', 'F8-T8', 'T8-P8-0', 'P8-O2']].sum(axis=1)
# p1['inner_right_hemi_sum'] = p1[['FP2-F4', 'F4-C4', 'C4-P4', 'P4-O2']].sum(axis=1)
#
# # center totals
# p1['center_line'] = p1[['FZ-CZ', 'CZ-PZ']].sum(axis=1)
#
# # left temple to rear totals
# p1['left_temple_to_left_rear'] = p1[['FZ-CZ', 'CZ-PZ']].sum(axis=1)
#
# # temple to temple totals
# p1['temple_to_temple'] = p1[['FT9-FT10']].sum(axis=1)
#
# # left temple to rear totals
# p1['right_temple_to_right_rear'] = p1[['FT10-T8', 'T8-P8-1']].sum(axis=1)
#
# # reorder columns for better visual early analysis
# new_cols = ['seizure = 1',
# 			'FP2-F4','FP1-F7', 'F7-T7', 'T7-P7', 'P7-O1','outer_left_hemi_sum',
#             'FP1-F3', 'F3-C3', 'C3-P3', 'P3-O1','inner_left_hemi_sum',
#             'FP2-F8', 'F8-T8', 'T8-P8-0', 'P8-O2','outter_right_hemi_sum',
#             'FP2-F4', 'F4-C4', 'C4-P4', 'P4-O2','inner_right_hemi_sum',
#             'FZ-CZ', 'CZ-PZ','center_line',
#             'P7-T7', 'T7-FT9','left_temple_to_left_rear',
#             'FT9-FT10','temple_to_temple',
#             'FT10-T8', 'T8-P8-1','right_temple_to_right_rear']
#
# p1 = p1.reindex(columns=new_cols)
# is_na = p1.count().all().tolist()
# infinite = np.isinf(p1).sum().to_list()


