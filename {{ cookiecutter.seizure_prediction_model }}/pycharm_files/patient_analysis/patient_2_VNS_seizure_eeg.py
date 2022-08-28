import numpy as np
import pandas as pd
import sklearn as sk
import matplotlib.pyplot as plt
import mne
import warnings  # Hide all warnings here
from eeg_to_edf_class_to_pandas_function import load_pandas_data,get_seizure,prepare_df_for_analysis,is_df_clean

data_set_site = 'https://physionet.org/content/chbmit/1.0.0/ '
view_data_set ="https://physionet.org/lightwave/?db=chbmit/1.0.0"
quick_access_mne_raw ="https://mne.tools/dev/generated/mne.io.Raw.html"

mne.set_log_level('WARNING')
warnings.simplefilter("ignore")
warnings.filterwarnings("ignore",category=DeprecationWarning)

raw_p1_02_nonseizure = '/Users/jshensley/Desktop/springboard/DS_Method_and_Capstones/capstone_2_2/capstone_2/a_cookiecutter_for_capstone_2/{{ cookiecutter.seizure_prediction_model }}/pycharm_files/Capstone2_dataset/VNS_patient/chb09_18_nonseizure_set_just_before_seizure_set.edf'

raw_p1_02_seizure_set = '/Users/jshensley/Desktop/springboard/DS_Method_and_Capstones/capstone_2_2/capstone_2/a_cookiecutter_for_capstone_2/{{ cookiecutter.seizure_prediction_model }}/pycharm_files/Capstone2_dataset/VNS_patient/chb09_19_aa_seizure_set.edf'

p2_VNS_preseizure_set = load_pandas_data(raw_p1_02_nonseizure)
p2_VNS_preseizure_set['seizure = 1'] = 0

p2_VNS_seizure_set = load_pandas_data(raw_p1_02_seizure_set)
p2_VNS_seizure_set['seizure = 1'] = 0

p2_VNS__seizures = get_seizure(p2_VNS_seizure_set, 5299, 5361)
p2_VNS_df = prepare_df_for_analysis(p2_VNS_preseizure_set, p2_VNS_seizure_set)
p1_plus_18_df_is_clean = is_df_clean(p2_VNS_df)
print(p1_plus_18_df_is_clean)

p2_VNS_df.info()
print(f'\n\n\n')
p2_VNS_describe = p2_VNS_df.describe()
print(p2_VNS_describe)