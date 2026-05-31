#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df = pd.read_csv("ecommerce_customer_data_custom_ratios.csv")


# In[3]:


df.head()


# In[4]:


df.columns


# In[5]:


df = df.drop(['Customer Age'], axis=1)
df['Purchase Date'] = pd.to_datetime(df['Purchase Date'])
df.isnull().sum()


# In[6]:


df['Total Purchase Amount'].sum()


# In[7]:


df['Total Purchase Amount'].mean()


# In[8]:


df['Product Category'].value_counts()


# In[9]:


sns.countplot(data=df, x='Product Category')
plt.xticks(rotation=45)
plt.show()


# In[10]:


sns.countplot(data=df, x='Churn')
plt.show()


# In[11]:


snapshot_date = df['Purchase Date'].max() + pd.Timedelta(days=1)


# In[12]:


rfm = df.groupby('Customer ID').agg({
    'Purchase Date': lambda x: (snapshot_date - x.max()).days,
    'Customer ID': 'count',
    'Total Purchase Amount': 'sum'
})
rfm.rename(columns={
    'Purchase Date': 'Recency',
    'Customer ID': 'Frequency',
    'Total Purchase Amount': 'Monetary'
}, inplace=True)

rfm.head()


# In[13]:


rfm['R_score'] = pd.qcut(rfm['Recency'], 4, labels=[4,3,2,1])
rfm['F_score'] = pd.qcut(rfm['Frequency'], 4, labels=[1,2,3,4])
rfm['M_score'] = pd.qcut(rfm['Monetary'], 4, labels=[1,2,3,4])


# In[14]:


rfm['RFM_Score'] = rfm['R_score'].astype(str) + rfm['F_score'].astype(str) + rfm['M_score'].astype(str)


# In[15]:


def segment(row):
    if row['RFM_Score'] == '444':
        return 'Best Customers'
    elif row['R_score'] == 4:
        return 'Recent Customers'
    elif row['F_score'] == 4:
        return 'Loyal Customers'
    elif row['M_score'] == 4:
        return 'Big Spenders'
    else:
        return 'At Risk'

rfm['Segment'] = rfm.apply(segment, axis=1)


# In[16]:


rfm['Segment'].value_counts()


# In[17]:


rfm['Segment'].value_counts().plot(kind='bar')
plt.title("Customer Segments")
plt.show()


# In[18]:


df['Month'] = df['Purchase Date'].dt.to_period('M')

monthly_sales = df.groupby('Month')['Total Purchase Amount'].sum()

monthly_sales.plot()
plt.title("Monthly Sales Trend")
plt.xticks(rotation=45)
plt.show()


# In[19]:


category_sales = df.groupby('Product Category')['Total Purchase Amount'].sum()

category_sales.sort_values(ascending=False).plot(kind='bar')
plt.title("Revenue by Category")
plt.show()


# In[23]:


sns.countplot(data=df, x='Payment Method')
plt.title("Payment Method Usage")
plt.xticks(rotation=45)
plt.show()


# In[24]:


sns.countplot(data=df, x='Churn')
plt.title("Churn Distribution")
plt.show()


# In[25]:


sns.boxplot(data=df, x='Churn', y='Age')
plt.title("Churn vs Age")
plt.show()


# In[26]:


sns.boxplot(data=df, x='Churn', y='Total Purchase Amount')
plt.title("Churn vs Spending")
plt.show()


# In[27]:


churn_rate = df['Churn'].value_counts(normalize=True) * 100
churn_rate


# In[ ]:




