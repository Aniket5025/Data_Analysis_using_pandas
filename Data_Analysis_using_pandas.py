#!/usr/bin/env python
# coding: utf-8

# # Hitters Dataset

# In[1]:


import pandas as pd


# In[4]:


df=pd.read_csv("E:\ds\Assignments\Pandas\hitters.csv")
df.head()


# Q1: Find out no of missing values in each column

# In[5]:


df.isna().sum()


# Q2: Find of people who have batted for more than 400 matches
# 

# In[6]:


df[df['AtBat']>400]['Name']


# Q3: Find out the name of the player who has hit max home runs

# In[7]:


df.loc[df['HmRun'].idxmax(),'Name']


# In[8]:


df['HmRun'].max()


# In[9]:


df['HmRun'].idxmax()


# Q4: Find out league wise total number of players

# In[10]:


df.value_counts('NewLeague')


# Q5: Find out division wise total amount of salary invested

# In[11]:


df['Division'].unique()


# In[12]:


df.groupby('Division')['Salary'].sum()


# Q6: Find out five most senior players. 

# In[11]:


df.sort_values('Years',ascending=False)[['Name','Years']].head()


# In[ ]:





# # Cars Dataset

# In[12]:


df1=pd.read_csv("E:\ds\Class_material\Cars93.csv")
df1.head()


# Q1 Find out car having highest Mileage in city

# In[13]:


df1['MPG.city'].max()


# Q2 Find out Models of cars which are having Price between 17 and 25

# In[14]:


df1[(df1.Price>17) & (df1.Price<25)][['Model','Price']]


# Q3. Find out top 7 most fuel economic cars for highway

# In[15]:


df1.sort_values('MPG.highway',ascending=False).head(7)[['Manufacturer','Model','MPG.highway']]


# Q4. Find out Models of cars having no AirBags and which are of compact type whose price is below 20.

# In[16]:


df1[(df1.AirBags=='None') & (df1.Type=='Compact') & (df1.Price<20)][['Manufacturer','Model','Type','Price','AirBags']]


# Q5. Find out top 7 most fuel economic cars for city, show results in sorted manner based on Horsepower.

# In[17]:


df1.sort_values('MPG.city',ascending=False).head(7)[['Manufacturer','Model','MPG.city']]


# Q6. Find out Cars having mileage of more than 15 miles in city

# In[18]:


df1[df1['MPG.city']>15][['Manufacturer','Model','MPG.city']]


# Q7. Find out Cars with US based origin

# In[19]:


df1[df1['Origin']=='USA'][['Manufacturer','Model','Origin']]


# Q8. Find out Cars with no airbags and which are compact in type, from the output retrieve only Model, Mileage in city, Type,
#     Airbags

# In[20]:


df1[(df1.AirBags=='None') & (df1.Type=='Compact') & (df1.Price<20)][['Model','MPG.city','Type','AirBags']]


# Q9. Find out cars with Mileage in city more than 15 which are compact in type.

# In[21]:


df1[(df1['MPG.city']>15) & (df1.Type=='Compact') ][['Manufacturer','Model','Type']]


# In[ ]:





# In[ ]:




