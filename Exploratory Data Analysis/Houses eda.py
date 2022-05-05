#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib .pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[2]:


houses=pd.read_csv('C:/hotel_bookings.csv')


# In[3]:


# Number of independent variables
X = houses.iloc[:,1:4]
print(X)


# In[4]:


# Name of the independent variable having minimum average value
houses['lead_time'].mean()


# In[5]:


# Name of the independent variable having minimum average value
houses['arrival_date_year'].mean()


# In[6]:


# Name of the independent variable having minimum average value
houses['is_canceled'].mean()


# In[7]:


# Name of the independent variable having high standard deviation
houses.describe()


# In[8]:


# What is the dependent variable in the selected dataset
Y = houses.iloc[:,4]
print(Y)


# In[9]:


# Display top 5 rows from the selected dataset
houses.head()


# In[10]:


# Find the total count of missing values in each column(independent variables). 
houses.isnull().sum()


# In[11]:


# Visualize all missing values, and identify the independent variable having maximum number of missing values?
sns.heatmap(houses.isnull(),cbar=False,cmap='viridis')


# In[12]:


#  Choose one numeric independent variable having missing values and replace the missing values with the average value of the column. 
num_col = ['lead_time', 'arrival_date_year', 'is_canceled']
for col in num_col:
    houses[col]=pd.to_numeric(houses[col])
    houses[col].fillna(houses[col].mean(), inplace=True)
houses.head()


# In[13]:


# Choose one independent variable and show frequency distribution using histogram
sns.histplot(houses.lead_time,bins=10)


# In[33]:


# Name of the independent variable having outliers? Use Box-plot to visualize.
plt.figure(figsize = (15, 8))
plt.subplot(1,1,1)
sns.boxplot(x = 'is_canceled', y = 'lead_time', data = houses)


# In[46]:


# Display Correlation Matrix and find two pairs of independent variables, one having strong positive correlation and the other pair having strong negative correlation
f, ax = plt.subplots(figsize=(10, 8))
corr = houses.corr()
sns.heatmap(corr,
            xticklabels=corr.columns.values,
            yticklabels=corr.columns.values)


# In[49]:


# Use scatter plots to visualize the correlation between independent and dependent variables (use same two pairs identified in previous question)
x = "lead_time"
y = "stays_in_week_nights"
sns.scatterplot(houses[x], houses[y])


# In[ ]:




