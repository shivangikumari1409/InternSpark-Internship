#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


sns.set()


# In[6]:


df = pd.read_csv("superstore_final_dataset (1).csv", encoding='latin1')
df.head()


# In[7]:


df.info()
df.describe()


# In[9]:


df['Order_Date'] = pd.to_datetime(df['Order_Date'], dayfirst=True)
df['Ship_Date'] = pd.to_datetime(df['Ship_Date'], dayfirst=True)


# In[10]:


df.isnull().sum()


# In[11]:


df = df.dropna()


# In[12]:


df = df.drop_duplicates()


# In[13]:


df['Year'] = df['Order_Date'].dt.year
df['Month'] = df['Order_Date'].dt.month
df['Month_Name'] = df['Order_Date'].dt.strftime('%B')


# In[14]:


month_order = ['January','February','March','April','May','June',
               'July','August','September','October','November','December']

df['Month_Name'] = pd.Categorical(df['Month_Name'], categories=month_order, ordered=True)


# In[15]:


total_revenue = df['Sales'].sum()
avg_order_value = df.groupby('Order_ID')['Sales'].sum().mean()
total_orders = df['Order_ID'].nunique()

print("Total Revenue:", total_revenue)
print("Average Order Value:", avg_order_value)
print("Total Orders:", total_orders)


# In[16]:


region_sales = df.groupby('Region')['Sales'].sum().sort_values()

region_sales.plot(kind='bar', title='Sales by Region')
plt.show()


# In[17]:


category_sales = df.groupby('Category')['Sales'].sum()

category_sales.plot(kind='pie', autopct='%1.1f%%')
plt.title("Sales by Category")
plt.show()


# In[18]:


subcat_sales = df.groupby('Sub_Category')['Sales'].sum().sort_values()

subcat_sales.plot(kind='barh', figsize=(8,6))
plt.title("Sales by Sub-Category")
plt.show()


# In[19]:


top_products = df.groupby('Product_Name')['Sales'].sum().sort_values(ascending=False).head(10)

top_products.plot(kind='barh')
plt.title("Top 10 Products")
plt.show()


# In[21]:


worst_products = df.groupby('Product_Name')['Sales'].sum().sort_values().head(10)


# In[22]:


monthly_sales = df.groupby('Month_Name')['Sales'].sum()

monthly_sales.plot(kind='line', marker='o')
plt.title("Monthly Sales Trend")
plt.show()


# In[23]:


yearly_sales = df.groupby('Year')['Sales'].sum()

yearly_sales.plot(kind='bar')
plt.title("Yearly Sales")
plt.show()


# In[24]:


segment_sales = df.groupby('Segment')['Sales'].sum()

segment_sales.plot(kind='bar')
plt.title("Sales by Segment")
plt.show()


# In[25]:


top_cities = df.groupby('City')['Sales'].sum().sort_values(ascending=False).head(10)

top_cities.plot(kind='bar')
plt.title("Top Cities by Sales")
plt.show()


# In[26]:


ship_mode_sales = df.groupby('Ship_Mode')['Sales'].sum()

ship_mode_sales.plot(kind='bar')
plt.title("Sales by Shipping Mode")
plt.show()

