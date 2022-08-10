#!/usr/bin/env python
# coding: utf-8

# # `Time Series` Plot 

# In[2]:



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


#rcParams - figsize and dpi
plt.rcParams['figure.figsize']=[8,4]
plt.rcParams['figure.dpi']=160


# In[4]:


df = pd.read_csv('daily-temperature.csv')
df


# In[5]:


df.info()


# In[7]:


# to_datetime
#change datatype of 
df['Date']=pd.to_datetime(df['Date'])
df.info()


# In[10]:


df.info()


# In[11]:


df.set_index('Date', inplace=True)


# In[23]:


df.head()


# # Line and Scatter Plot 

# In[31]:



# Plot the Date and temperature dataset 
# change color and set xlabel & ylabel
# Give the title as well
df.plot(color='g')
plt.xlabel('Date')
plt.ylabel('Temp')
plt.title('Date V Temp')


# In[32]:



# Change the plot style with dots
# Again change th colors
df.plot(color='r',marker='o')


# In[33]:


# Write down which plot is better ? and why !!
print('The second plot is better as the markers help to better identify centain peak values')


# ## Subplots 

# In[12]:


groups = df.groupby(pd.Grouper(freq = 'A'))
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Grouper.html


# In[13]:


keys = groups.groups.keys()


# In[14]:


keys


# In[15]:


groups.get_group('1981-12-31')


# In[16]:


for key in keys:
    print(key)


# In[17]:


key


# In[18]:


groups.get_group(key)['Temp'].values


# In[19]:


years = pd.DataFrame()
for key in keys:
    years[key] = groups.get_group(key)['Temp'].values


# In[20]:


years


# In[68]:


plt.show()
#plot subplots (with temperature on y-axis and day on x-axis)
# tight the layout so that you cannot have same x-axis label on every plot.
# change the figure size such that width(x-axis) is 3 times as of length(y-axis)

years.plot(subplots=True,figsize=(30,10))
plt.xlabel('Days')
plt.tight_layout()
plt.show()


# # Heatmap 

# In[21]:


plt.matshow(years.T, aspect = 'auto') # marshow display the data points/values with difference of colors
# lower values darker colors and high temp. values are brighter values


# # Histogram and KDE Plot 

# In[60]:



# plot histogram
# change the bins & grids and change the colors as well
# xlabel and ylabel
df.plot(kind='hist',bins=30,color='b',grid=True)
plt.xlabel('Temp')
plt.ylabel('Frequency 10 years')
plt.show()


# In[63]:



# change the above histogram into KDE plot (as discussed in last class)
# give the xy-labels as well
df.plot(kind='kde',grid=True,color='y')
plt.xlabel('Temp')
plt.ylabel('Frequency 10 years')
plt.show()


# In[67]:


# Write which plot is better to show the temperature (a time series data) with in a year
print('As temperature data is continuous in nature the kde representation is better for its representation' )

