#!/usr/bin/env python
# coding: utf-8

# In[13]:


import pandas as pd
df = pd.read_csv('/Users/daisy/Desktop/movies_metadata.csv')
df = df.set_index('title')
result = df.loc['Grumpier Old Men']
print("Details for: Grumpier Old Men")
result


# In[25]:


sorted_movies = df.sort_values('release_date')
movies =sorted_movies.loc[:, ['release_date','budget','revenue','runtime']]
movies.head()


# In[26]:


revenue =movies[(movies['revenue'] > 20000000) & (movies['budget'] < 1000000)]
revenue


# In[ ]:




