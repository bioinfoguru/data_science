#!/usr/bin/env python
# coding: utf-8

# ## Covid19 data analysis
# Using the data avaiable from Our World in Data, here we'll apply some of the data science concepts to analyze Covid19 data.

# In[34]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys


# In[35]:


df1 = pd.read_csv("owid-covid-data.csv")


# In[36]:


df1.shape


# In[40]:


df1


# In[143]:


#Countries with maximum number of cases per continent
df_cont_location = df1.groupby(["continent","location"],as_index=False)["total_cases"].max()
df_cont_location


# In[148]:


idx = df1.groupby(['continent'])['total_cases'].transform(max) == df1['total_cases']
df1[idx]


# ### Exercise
# Find top 10 countries having highest number of total Covid cases till date.

# In[69]:


top_10 = df1.groupby(["location"], as_index=False)["new_cases"].sum().sort_values(by="new_cases", ascending=False)[8:18]


# In[96]:


top_10


# Using `nlargest()` function

# In[50]:


df_2 = df1.groupby(["location"],as_index=False)["new_cases"].sum()


# In[53]:


df_2.nlargest(15,"new_cases")


# Selecting data for a particular date.

# In[54]:


df_date_filter = df1[df1["date"]=="2022-06-13"]


# In[97]:


df_date_filter.nlargest(10,"total_cases")[["total_cases"]]


# In[98]:


top_10


# In[104]:


fig, ax = plt.subplots()
ax.barh(top_10["location"],top_10["new_cases"], color="lightblue")
ax.spines[["top","right","left"]].set_visible(False)
ax.yaxis.set_ticks_position('none')
a=ax.get_yticklabels()
ax.grid('on',which='major',axis='x')
ax.invert_yaxis()
plt.show()


# ### Changing axis scale
# 

# In[145]:


import numpy as np


# In[242]:


#Exponential 
N=1
x = range(1,11)
y = []
for a in x:
    N = N*2
    y.append(N)

fig, (ax1,ax2) = plt.subplots(nrows=1, ncols=2,figsize=(9,3))
plt.rcParams.update({'font.size': 14})

ax1.plot(x,y)
ax2.plot(x,y)
ax2.set_yscale('log')

ax1.set_title("Linear Scale")
ax2.set_title("Log Scale")


plt.show()


# In[71]:


fig, ax = plt.subplots(2,1)
plt(ax=ax[0])
plt(ax=ax[1])


# In[77]:


fig,some_axes=plt.subplots(figsize=(8,3))

df1[df1["location"]=="India"].plot(x="date", y="total_cases",ax=some_axes)
df1[df1["location"]=="United States"].plot(x="date", y="total_cases",ax=some_axes)
df1[df1["location"]=="France"].plot(x="date", y="total_cases",ax=some_axes)
plt.legend(["India","United States", "France"])
plt.ylabel("Total Cases")
#plt.yscale("log")
plt.show()


# ### Function to plot total cases

# In[79]:


def plot_country(*args):
    fig,ax=plt.subplots(figsize=(8,3))
    for c in args:
        df1[df1["location"]==c].plot(x="date", y="total_cases",ax=ax)
    plt.legend(args)
    plt.show()

plot_country("India","United States","France")


# In[436]:


fig,ax=plt.subplots(figsize=(8,3))
df1[df1["location"]=="India"].plot(x="date", y="new_cases",ax=ax)
#df1[df1["location"]=="United States"].plot(x="date", y="new_cases",ax=ax)
plt.show()


# In[6]:


df_India = df1[df1["location"]=="India"]


# In[81]:


df_India[(df_India["date"] >= '2022-01-01') & (df_India["date"] <= '2022-01-31')]


# In[82]:


df_India.dtypes


# In[83]:


df_India["date"] = pd.to_datetime(df_India['date'])


# In[84]:


df_India_2022 = df_India[(df_India["date"] >= '2022-01-01')]


# In[86]:


df_India_2022.dtypes


# In[87]:


df_months = df_India_2022.groupby(df_India_2022['date'].dt.strftime('%B'))["new_cases"].sum().to_frame().reset_index()#.plot(kind="bar")


# In[88]:


df_months


# In[89]:


print(df_months.dtypes)
df_months.sort_values(by="date",inplace=True, ignore_index=True)
df_months


# In[90]:


months = ["January", "February", "March", "April", "May", "June", 
          "July", "August", "September", "October", "November", "December"]
df_months['date'] = pd.Categorical(df_months['date'], categories=months, ordered=True)
df_months.sort_values(by="date",inplace=True, ignore_index=True)
print(df_months.dtypes)
df_months


# In[91]:


fig,ax=plt.subplots()
df_months.plot(kind="bar",xlabel="date", ax=ax)
plt.show()


# In[407]:


df_India_2022["date"] = df_India_2022["date"].dt.strftime('%B')


# In[431]:


months = ["January", "February", "March", "April", "May", "June"]
df_India_2022['date'] = pd.Categorical(df_India_2022['date'], categories=months, ordered=True)
df_India_2022.sort_values(by="date",inplace=True, ignore_index=True)
df_India_2022.dtypes


# In[434]:


ax = df_India_2022.boxplot(column="new_cases",by="date")
plt.title("")
plt.show()


# In[92]:


import seaborn as sns


# In[7]:


df_India.columns


# In[15]:


df1.loc[df1['location'].isin(["India","United States"])]


# In[18]:


sns.jointplot(data=df1.loc[df1['location'].isin(["India","United States"])],              x="new_cases",y="new_deaths", hue="location")


# In[93]:


new_df = df1.loc[df1['location'].isin(["India","United States"])]


# In[94]:


new_df


# In[95]:


sns.jointplot(data=new_df,              x="total_cases",y="total_vaccinations", hue="location")


# In[24]:


df1.loc[df1['location'].isin(["India","United States"])]


# In[29]:


sns.pairplot(df1.loc[df1['location'].isin(["India","United States"])]
             [["location","total_cases","total_deaths","total_vaccinations"]],hue="location")


# In[ ]:




