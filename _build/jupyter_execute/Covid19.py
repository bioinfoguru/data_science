#!/usr/bin/env python
# coding: utf-8

# ## Covid19 data analysis
# Using the data avaiable from Our World in Data, here we'll apply some of the data science concepts to analyze Covid19 data.

# In[10]:


import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


df1 = pd.read_csv("owid-covid-data.csv")


# In[3]:


df1.head()


# ### Exercise
# Find top 10 countries having highest number of total Covid cases till date.

# In[221]:


top_10 = df1.groupby(["location"], as_index=False)["new_cases"].sum().sort_values(by="new_cases", ascending=False)[8:18]


# In[222]:


top_10


# Using `nlargest()` function

# In[223]:


df1.groupby(["location"],as_index=False)["new_cases"].sum().nlargest(10,"new_cases")


# Selecting data for a particular date.

# In[241]:


df1[df1["date"]=="2022-06-13"].nlargest(10,"total_cases")#[["location","total_cases"]]


# In[33]:


top_10_r


# In[437]:


fig, ax = plt.subplots()
ax.barh(top_10_r.index,top_10_r.values, color="lightblue")
ax.spines[["top","right","left"]].set_visible(False)
ax.yaxis.set_ticks_position('none')
a=ax.get_yticklabels()
ax.grid('on',which='major',axis='x')

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


# In[298]:


fig,ax=plt.subplots(figsize=(8,3))
df1[df1["location"]=="India"].plot(x="date", y="total_cases",ax=ax)
df1[df1["location"]=="United States"].plot(x="date", y="total_cases",ax=ax)
df1[df1["location"]=="France"].plot(x="date", y="total_cases",ax=ax)
plt.legend(["India","United States", "France"])
plt.ylabel("Total Cases")
#plt.yscale("log")
plt.show()


# ### Function to plot total cases

# In[267]:


def plot_country(*args):
    fig,ax=plt.subplots(figsize=(8,3))
    for c in args:
        df1[df1["location"]==c].plot(x="date", y="total_cases",ax=ax)
    plt.legend(args)
    plt.show()

plot_country("India","United States")


# In[436]:


fig,ax=plt.subplots(figsize=(8,3))
df1[df1["location"]=="India"].plot(x="date", y="new_cases",ax=ax)
#df1[df1["location"]=="United States"].plot(x="date", y="new_cases",ax=ax)
plt.show()


# In[349]:


df_India = df1[df1["location"]=="India"]


# In[353]:


df_India[(df_India["date"] >= '2022-01-01') & (df_India["date"] <= '2022-01-31')].head()


# In[354]:


df_India.dtypes


# In[355]:


df_India["date"] = pd.to_datetime(df_India['date'])


# In[385]:


df_India_2022 = df_India[(df_India["date"] >= '2022-01-01')]


# In[386]:


df_months = df_India_2022.groupby(df_India_2022['date'].dt.strftime('%B'))["new_cases"].sum().to_frame().reset_index()#.plot(kind="bar")


# In[387]:


print(df_months.dtypes)
df_months.sort_values(by="date",inplace=True, ignore_index=True)
df_months


# In[388]:


months = ["January", "February", "March", "April", "May", "June", 
          "July", "August", "September", "October", "November", "December"]
df_months['date'] = pd.Categorical(df_months['date'], categories=months, ordered=True)
df_months.sort_values(by="date",inplace=True, ignore_index=True)
print(df_months.dtypes)
df_months


# In[401]:


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

