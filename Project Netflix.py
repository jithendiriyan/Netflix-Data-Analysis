#!/usr/bin/env python
# coding: utf-8

# In[19]:


# importing the dataset and library
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Set Seaborn style
sns.set(style="whitegrid")


# In[20]:


#dataset = pd.read_csv("E:/Netflix Project/netflix_titles.csv")
#fectching the data set from data source
dataset = pd.read_csv(r"E:\Netflix Project\netflix_titles.csv")


# In[21]:


dataset


# In[22]:


# To show the count of rows and columns
dataset.shape


# In[23]:


#shows first five rows
dataset.head()


# In[24]:


#shows last rows
dataset.tail()


# In[25]:


#count of the elements
dataset.size


# In[26]:


#to show column names
dataset.columns


# In[27]:


# TO show the data types
dataset.dtypes


# In[28]:


# to find any null is present
dataset.isnull()


# In[29]:


#collecting information from the dataset
dataset.info()


# In[30]:


#check any duplicate value are present in the data set
dataset.duplicated()


# In[31]:


#check the data whether duplicate value is present in it
dataset[dataset.duplicated()]


# In[32]:


#checking sum of the non values 
dataset.isnull().sum()


# In[33]:


#Using heat map to check the null values
sns.heatmap(dataset.isnull())


# In[34]:


# Count the number of Movies and TV Shows
plt.figure(figsize=(10,6))
sns.countplot(x='type', data=dataset, palette='viridis')
plt.title('Count of Movies and TV Shows on Netflix')
plt.show()


# In[40]:


# Count the number of content by Genre
plt.figure(figsize=(12,8))
dataset['listed_in'].str.split(', ').explode().value_counts().head(10).plot(kind='barh', color='gold')
plt.title('Top 10 Genres on Netflix')
plt.xlabel('Number of Titles')
plt.ylabel('Genre')
plt.show()


# In[42]:


# Top 10 countries by number of titles
plt.figure(figsize=(12,8))
dataset['country'].str.split(', ').explode().value_counts().head(10).plot(kind='barh', color='lightcoral')
plt.title('Top 10 Countries by Number of Titles')
plt.xlabel('Number of Titles')
plt.ylabel('Country')
plt.show()


# In[54]:


# Count the number of titles released each year
plt.figure(figsize=(14,8))
dataset['release_year'].value_counts().sort_index().plot(kind='bar', color='red')
plt.title('Number of Netflix Titles Released Each Year')
plt.xlabel('Year')
plt.ylabel('Number of Titles')
plt.show()


# In[ ]:





# In[ ]:




