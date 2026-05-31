#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df = pd.read_csv("traffic.csv")
df.head()
df.info()


# In[3]:


df['date'] = pd.to_datetime(df['date'])

df = df.dropna()

df = df.sort_values(by='date')


# In[4]:


df['session_id'] = df['linkid']

df['user_id'] = df['city'] + "_" + df['country']


# In[5]:


sessions = df['session_id'].nunique()


# In[6]:


users = df['user_id'].nunique()


# In[7]:


session_counts = df.groupby('session_id').size()
bounce_sessions = session_counts[session_counts == 1].count()

bounce_rate = (bounce_sessions / sessions) * 100


# In[8]:


session_time = df.groupby('session_id')['date'].agg(['min','max'])
session_time['duration'] = (session_time['max'] - session_time['min']).dt.seconds

avg_session_duration = session_time['duration'].mean()


# In[9]:


top_tracks = df['track'].value_counts().head(10)

top_tracks.plot(kind='bar', title="Top Landing Pages")
plt.show()


# In[10]:


df['country'].value_counts().head(10).plot(kind='bar')
plt.title("Top Countries")
plt.show()


# In[11]:


journey = df.groupby('session_id')['track'].apply(list)
journey.head()


# In[12]:


entry_pages = df.groupby('session_id').first()['track']
exit_pages = df.groupby('session_id').last()['track']

entry_pages.value_counts().head(10).plot(kind='bar', title="Entry Pages")
plt.show()

exit_pages.value_counts().head(10).plot(kind='bar', title="Exit Pages")
plt.show()


# In[14]:


df['event'].value_counts().plot(kind='bar')
plt.title("Event Distribution")
plt.show()


# In[16]:


top_countries = df['country'].value_counts().head(10)

top_countries.plot(kind='bar')
plt.xticks(rotation=45)
plt.title("Top 10 Countries")
plt.show()


# In[19]:


df.groupby(df['date'].dt.date).size().plot()
plt.title("Traffic Over Time")
plt.show()

