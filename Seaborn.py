#!/usr/bin/env python
# coding: utf-8

# ## Seaborn 

# ### Scatter Plot 

# In[1]:


import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


tips = sns.load_dataset('tips')


# In[3]:


tips.head()


# In[ ]:


# Relplot & Catplot - > ????


# In[4]:


sns.relplot(x = 'total_bill', y = 'tip', data = tips)


# ### Hue,  Style and Size

# In[5]:


# hue
sns.relplot(x = 'total_bill', y = 'tip', data = tips,hue='smoker')


# In[12]:


# + style
sns.relplot(x = 'total_bill', y = 'tip', data = tips,style='time',hue='smoker')


# In[13]:


# + size
sns.relplot(x = 'total_bill', y = 'tip', data = tips,size='size',style='time')


# In[7]:


tips.columns


# In[11]:


# hue = 'smoker' & style = 'time' & size= 'size'
sns.relplot(x = 'total_bill', y = 'tip', data = tips,hue='smoker',size='size',style = 'time')


# In[19]:


# just style = size
sns.relplot(x = 'total_bill', y = 'tip', data = tips,style='size')


# In[14]:


tips['size'].value_counts()


# In[20]:


# style = 'smoker'
sns.relplot(x = 'total_bill', y = 'tip', data = tips,style='smoker')


# In[21]:


tips['smoker'].value_counts()


# In[84]:


# sizes = (15, 200) 
sns.relplot(x = 'total_bill', y = 'tip', data = tips,sizes=(15,200))


# In[22]:


tips['time'].value_counts()


# ### Line Plot 

# In[23]:


from seaborn import relplot


# In[98]:


# generate random numbers in a dataFrame (500) , take cumsum(), colums can be time and value.
# plot relplot time on x axis and value on y axis
# line ploting 
df=pd.DataFrame(np.random.randn(500),columns=['time'])
df['value']=np.cumsum(df['time'])
sns.lineplot(data=df,x='time',y='value')


# In[24]:


fmri = sns.load_dataset('fmri')
fmri.head()


# In[25]:


fig, ax = plt.subplots()
sns.relplot(x = 'timepoint', y = 'signal', kind = 'line', data = fmri, label = 'Sine')


# In[27]:


relplot(x = 'timepoint', y = 'signal', kind = 'line', data = fmri, label = 'Signal', height = 4, aspect = 2)
plt.legend(loc='right')


# In[29]:


# estimator = none
relplot(x = 'timepoint', y = 'signal', kind = 'line', data = fmri, label = 'Signal', height = 4, aspect = 2,estimator = None)
plt.legend(loc='right')


# In[31]:


# add hue = event
relplot(x = 'timepoint', y = 'signal', kind = 'line', data = fmri, label = 'Signal', height = 4, aspect = 2,hue = 'event')
plt.legend(loc='right')


# In[32]:


# style = 'region'
relplot(x = 'timepoint', y = 'signal', kind = 'line', data = fmri, label = 'Signal', height = 4, aspect = 2,style = 'region')
plt.legend(loc='right')


# In[33]:


# marker = True, dashes = False
relplot(x = 'timepoint', y = 'signal', kind = 'line', data = fmri, label = 'Signal', height = 4, aspect = 2,marker = True, dashes = False)
plt.legend(loc='right')


# In[34]:


dots = sns.load_dataset('dots')


# In[35]:


dots.head()


# In[36]:


relplot(x = 'time', y = 'firing_rate', data = dots, kind = 'line')


# In[37]:


# hue = 'coherence', style = 'choice'
relplot(x = 'time', y = 'firing_rate', data = dots, kind = 'line',hue = 'coherence', style = 'choice')


# In[80]:


pallette = sns.cubehelix_palette(light = 0.9, n_colors = 6)
# palette = pallette
relplot(x = 'time', y = 'firing_rate', data = dots, kind = 'line',palette = pallette)


# In[81]:


#  size = 'choice'
relplot(x = 'time', y = 'firing_rate', data = dots, kind = 'line',size = 'choice')


# ### Subplots 

# In[38]:


tips.head()


# In[39]:


relplot(x = 'total_bill', y = 'tip', hue = 'smoker', col = 'smoker', data = tips)


# In[97]:


# col = 'size'
relplot(x = 'total_bill', y = 'tip', hue = 'smoker', col = 'size', data = tips)


# In[85]:


# row = 'size'
relplot(x = 'total_bill', y = 'tip', hue = 'smoker', col = 'smoker', data = tips, row = 'size')


# In[86]:


# col_wrap=3
relplot(x = 'total_bill', y = 'tip', hue = 'smoker', col = 'smoker', data = tips, col_wrap=3)


# ### Using sns.lineplot() and sns.scatterplot()

# In[87]:


fmri.head()


# In[88]:


sns.lineplot(x = 'timepoint', y = 'signal', style = 'event', hue = 'region', data = fmri, markers = True, ci = 68, err_style = 'bars')


# In[89]:


sns.lineplot(x = 'timepoint', y = 'signal',  hue = 'event', data = fmri.query("region == 'frontal'"), estimator = None, lw = 1)


# In[90]:


sns.scatterplot(x = 'total_bill', y = 'tip', data = tips, hue = 'smoker', size = 'size', style = 'time')


# ## Categorical Data Ploting 

# ### Cat Plot 

# In[91]:


tips.head()


# In[92]:


sns.catplot(x = 'day', y = 'total_bill', data = tips)


# In[93]:


sns.catplot(x = 'total_bill', y = 'day', data = tips)


# In[94]:


sns.catplot(x = 'day', y = 'total_bill', data = tips, jitter = False)


# In[95]:


sns.catplot(x = 'day', y = 'total_bill', data = tips, kind = 'swarm', hue = 'size')


# In[96]:


sns.catplot(x = 'smoker', y = 'tip', data = tips, order = ['No', 'Yes'])


# ### Box Plot 

# In[46]:


sns.catplot(x = 'day', y = 'total_bill', kind = 'box', data = tips, hue = 'sex')


# In[47]:


# dodge = False 
sns.catplot(x = 'day', y = 'total_bill', kind = 'box', data = tips, hue = 'sex',dodge = False )


# ### Boxen Plot 

# In[76]:


diamonds = sns.load_dataset('diamonds')


# In[77]:


diamonds.head()


# In[78]:


sns.catplot(x = 'color', y = 'price', kind = 'boxen', data = diamonds)


# In[79]:


sns.catplot(x = 'color', y = 'price', kind = 'boxen', data = diamonds, hue = 'cut')


# ### Violin Plot 

# In[72]:


sns.catplot(x = 'total_bill', y = 'day', data = tips, kind = 'violin', hue = 'sex', split = True)


# In[73]:


g = sns.catplot(x = 'day', y = 'total_bill', data = tips, kind = 'swarm')
sns.catplot(x = 'day', y = 'total_bill', data = tips, kind = 'violin', ax = g.ax, color = 'k')


# ### Bar Plot 

# In[74]:


titanic = sns.load_dataset('titanic')


# In[75]:


titanic.head()


# In[50]:


sns.catplot(x = 'sex', y = 'survived', kind = 'bar', data = titanic, hue = 'class')


# In[52]:


# palette='ch:0.65')
sns.catplot(x = 'sex', y = 'survived', kind = 'bar', data = titanic, hue = 'class',palette='ch:0.65')


# ### Point Plot 

# In[99]:


sns.catplot(x = 'sex', y = 'survived', hue = 'class', kind = 'point', data = titanic)


# In[ ]:





# ### Joint Plot 

# In[53]:


tips.head()


# In[54]:


x = tips['total_bill']
y = tips['tip']


# In[55]:


sns.jointplot(x, y)


# In[56]:


# kind = 'hex')
sns.jointplot(x, y,kind = 'hex')


# In[57]:


# kind = 'kde')
sns.jointplot(x, y,kind = 'kde')


# ### Pair Plot 

# In[58]:


sns.pairplot(tips)


# In[59]:


g = sns.PairGrid(tips)
g.map_diag(sns.kdeplot)
g.map_offdiag(sns.kdeplot)


# In[60]:


g = sns.PairGrid(tips)
g.map_diag(sns.kdeplot)
g.map_offdiag(sns.scatterplot)


# ### Regression Plot 

# In[61]:


tips.head()


# In[62]:


sns.regplot(x = 'total_bill', y = 'tip', data = tips)


# In[63]:


sns.lmplot(x = 'size', y = 'tip', data = tips)


# ### Controlling Ploted Figure Aesthetics
# - figure styling
# - axes styling
# - color palettes
# - etc..

# In[64]:


def sinplot(flip = 1):
    x = np.linspace(0, 14, 100)
    for i in range(1, 7):
        plt.plot(x, np.sin(x + i*0.5)*(7-i)*flip)


# In[65]:


sinplot()


# In[66]:


sinplot(-1)


# In[67]:


sns.set_style('ticks', {'axes.grid': True, 'xticks.direction': 'in'})
sinplot()


# In[68]:


sns.set_style('ticks', {'axes.grid': True, 'xticks.direction': 'in'})
sinplot()
sns.despine()


# In[69]:


sns.axes_style()


# In[70]:


sns.set_style('darkgrid')


# In[71]:


sinplot()

