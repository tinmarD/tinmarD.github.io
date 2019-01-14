
# coding: utf-8

# ## Shape evolution of the stimulation artefact along the electrode
# In this notebook, we analyse how the shape of the artefact changes when the distrance from the recording site to the stimulation site increases.

# In[3]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import mne
from stim_analysis_fun import *
sns.set_context('paper')
sns.set()
import re


# ### Set the path of the epoch and stim event list :

# In[4]:


stim_epoch_path = r'C:\\Users\\deudon\\Desktop\\Stimic\\_Data\\STIMS\\P53_CD25\\P53_CD25_stim_mne_epoch-resync-epo.fif'
stim_spreadsheet_path = r'C:\Users\deudon\Desktop\Stimic\_Data\STIMS\P53_CD25\p53_CD25_stimulations_all.xlsx'


# Read mne epoch structure : 

# In[5]:


stim_epoch = mne.read_epochs(stim_epoch_path)
print(stim_epoch)


# Load stim spreadsheet : 

# In[6]:


df = pd.read_excel(stim_spreadsheet_path)


# Let's call the `plot_artefact_ev_with_electrode_distance` function. 
# 
# The two arguments are respectively the MNE epoch structure containing the stimulation data and the pandas DataFrame listing all the stimulations.
# The 3rd argument is the channel maximal offset, i.e. how far from the stimulation site we look at the shape of the stimulation artefact.
# 
# The function can be called with optionnal selection arguments which must be column names of the stimulation data frame `df`.
# For instance : 
#  * `plot_artefact_ev_with_electrode_distance(stim_epoch, df, 1, freq=1)` will select only the 1Hz stimulations
#  * `plot_artefact_ev_with_electrode_distance(stim_epoch, df, 1, freq=1, intensity=1.5)` will select only the 1Hz stimulations at 1.5 mA intensity
#  * `plot_artefact_ev_with_electrode_distance(stim_epoch, df, 1, freq=50, channelname='EEG A3')` will select the 50Hz stimulation located in EEG A3

# In[7]:


plot_artefact_ev_with_electrode_distance(stim_epoch, df, 1, freq=50)

