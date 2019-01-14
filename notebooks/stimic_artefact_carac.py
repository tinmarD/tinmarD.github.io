
# coding: utf-8

# # Caracterization of the stimulation artefact

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
import mne
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
import seaborn as sns
sys.path.append('../stimic_main/')
import utils_stimic
import utils_eeg_cleaning
from stim_analysis_fun import *
sns.set()
sns.set_context('paper')
plt.rcParams['figure.figsize'] = (14, 14)


# ### Set the path of the epoch and stim event list :

# In[2]:


stim_epoch_path = r'C:\\Users\\deudon\\Desktop\\Stimic\\_Data\\STIMS\\P53_CD25\\P53_CD25_stim_mne_epoch-resync-epo.fif'
stim_spreadsheet_path = r'C:\Users\deudon\Desktop\Stimic\_Data\STIMS\P53_CD25\p53_CD25_stimulations_all.xlsx'


# Read mne epoch structure : 

# In[3]:


stim_epoch = mne.read_epochs(stim_epoch_path)
print(stim_epoch)


# Load stim spreadsheet : 

# In[4]:


df = pd.read_excel(stim_spreadsheet_path)
df.head()


# ### Plot the mean artefact for 1Hz stimulation : 
# We will use the `plot_mean_artefact` function. 
# 
# The first two arguments are respectively the MNE epoch structure containing the stimulation data and the pandas DataFrame `df` listing all the stimulations.
# 
# The 3rd argument is optional, if specified it must be a column name (key) of the `df` dataframe. It will separate the different conditions, and plot each one of them is a different color.
# 
# The function can be called with optionnal selection arguments which must be column names of the stimulation data frame `df`.
# For instance : 
#  * `plot_mean_artefact(stim_epoch, df, 1freq=1)` will select only the 1Hz stimulations
#  * `plot_mean_artefact(stim_epoch, df, 1, freq=1, intensity=1.5)` will select only the 1Hz stimulations at 1.5 mA intensity
#  * `plot_artefact_ev_with_electrode_distance(stim_epoch, df, 1, freq=50, channelname='EEG A3')` will select the 50Hz stimulation located in EEG A3

# In[5]:


plot_mean_artefact(stim_epoch, df, color_by='intensity', freq=1)


# ### See the effect of intensity on the shape of the 50Hz stimulation artifact : 

# In[9]:


plot_mean_artefact(stim_epoch, df, plot_traces=0, freq=50, color_by='intensity')

