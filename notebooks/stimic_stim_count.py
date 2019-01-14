
# coding: utf-8

# ## Count Stim
# This notebook show how to count the number of stimulations in function of the different stimulation paremeters from the Stimulation Event File

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_context('paper')
sns.set()
import re


# In[2]:


stim_spreadsheet_path = r'..\data\p42_KR01_stimulations_all.xlsx'
patient_id = 'KR01'


# ### Read the Excel sheet with pandas

# In[3]:


pd.set_option('display.width', 500)
df = pd.read_excel(stim_spreadsheet_path)
df.style.set_properties(**{'font-size':'5'})
df.head()


# #### Plot the  number of stimulation in function of the frequency, intensity and channel : 

# In[4]:


f = plt.figure(figsize=(16, 12))
ax1 = f.add_subplot(131)
sns.countplot(df['freq'], ax=ax1)
ax2 = f.add_subplot(132)
sns.countplot(df['intensity'], ax=ax2)
ax2.set(title=patient_id)
ax3 = f.add_subplot(133)
sns.countplot(y='channelname', data=df, orient='h', ax=ax3)


# #### Another way to count the stimulations, in function of the channel and frequency : 

# In[5]:


f = plt.figure(figsize=(13, 13))
ax = f.add_subplot(111)
ax.set(title=patient_id)
sns.countplot(y='channelname_bipolar', hue='freq', data=df, orient='h', ax=ax)

