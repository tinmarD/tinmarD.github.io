
# coding: utf-8

# In[2]:


import altair as alt
from vega_datasets import data


# In[2]:


# Uncomment/run this line to enable Altair in the classic notebook (not JupyterLab)
alt.renderers.enable('notebook')


# In[6]:


iris = data.iris()
iris.head()


# In[7]:


alt.Chart(iris).mark_square().encode(
    x='petalLength',
    y='petalWidth',
    color='species'
)


# First we’ll create an interval selection using the selection_interval() function:

# In[8]:


brush = alt.selection_interval()  # selection of type "interval"


# In[11]:


alt.Chart(iris).mark_square().encode(
    x='petalLength',
    y='petalWidth',
    color=alt.condition(brush, 'species:N', alt.value('lightgray'))
).properties(
    selection=brush
)


# In[17]:


brush = alt.selection_interval(encodings=['x'])  # selection of type "interval"
chart = alt.Chart(iris).mark_square().encode(
    y='petalWidth',
    color=alt.condition(brush, 'species:N', alt.value('lightgray'))
).properties(
    selection=brush
)


# In[18]:


chart.encode(x='petalLength')  | chart.encode(x='sepalLength')

