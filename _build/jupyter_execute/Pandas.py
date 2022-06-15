#!/usr/bin/env python
# coding: utf-8

# ## Introduction to Pandas
# Pandas is a library that is useful for working with different types of datasets. A dataframe is a pandas object that has a variety of function to analyze and visualize data.

# In[1]:


import pandas as pd


# In[42]:


print(pd.__version__)


# Creating a dataframe from a dictionary where keys become headers and values (list) are entries in the dataframe. The orientation of the dataframe by default is `columns` ie keys are considered as column header and values are rows. This behaviour can be changed using the `orient` argument. When orientation is index, an addtional argument `columns` can be used to specify column headers.

# In[1]:


from IPython.display import display_html 
from IPython.display import display, Latex


# In[44]:


input_dict = {'Column1': ['A','B','C','D','E'], 'Column2':[1,2,3,4,5]}
df1 = pd.DataFrame.from_dict(input_dict)
df2 = pd.DataFrame.from_dict(input_dict, orient='index', columns=['Val1','Val2','Val3','Val4','Val5',])
print(input_dict)


# ### Getting basic information about the dataframe
# Pandas offers set of commands to get some basic information about the content of dataframes. Below are some of these command along with their corresponding output. 

# In[45]:


display(df1) 
print("**Different commands to get some basic information about this dataframe**")
display(Latex(f'df1.shape $\Longrightarrow$ {df1.shape}'))
display(Latex(f'df1.size $\Longrightarrow$ {df1.size}'))
display(Latex(f'df1.ndim $\Longrightarrow$ {df1.ndim}'))
display(Latex(f'df1.axes $\Longrightarrow$ {df1.axes}'))
display(Latex(f'df1.values $\Longrightarrow$ {df1.values}'))


# In[46]:


df1_styler = df1.style.set_table_attributes("style='display:inline;margin-right:10em'").set_caption('df1').set_table_styles([{
    'selector': 'caption',
    'props': [
        ('text-align', 'center'),
        ('font-size', '14pt')
    ]
}])
df2_styler = df2.style.set_table_attributes("style='display:inline'").set_caption('df2').set_table_styles([{
    'selector': 'caption',
    'props': [
        ('text-align', 'center'),
        ('font-size', '14pt')
    ]
}])

display_html(df1_styler._repr_html_()+df2_styler._repr_html_(), raw=True)


# ### Read data from a csv file

# The `read_csv()` function can be used to create a dataframe from a csv file. To use one of the columns as indices for the dataframe add the `index_col` keyword attribute. 

# In[ ]:


# %load test.csv
Name,Age,Country
Sohan,22,India
Sam,21,USA


# In[50]:


df3 = pd.read_csv("test.csv")
df4 = pd.read_csv("test.csv", index_col="Country")


# In[51]:


df3_styler = df3.style.set_table_attributes("style='display:inline;margin-right:10em'").set_caption('df3').set_table_styles([{
    'selector': 'caption',
    'props': [
        ('text-align', 'center'),
        ('font-size', '14pt')
    ]
}])
df4_styler = df4.style.set_table_attributes("style='display:inline'").set_caption('df4').set_table_styles([{
    'selector': 'caption',
    'props': [
        ('text-align', 'center'),
        ('font-size', '14pt')
    ]
}])

display_html(df3_styler._repr_html_()+df4_styler._repr_html_(), raw=True)


# ### Combining dataframes - join, merge, and concat

# Concat is used to combine dataframes across rows or columns. Merge is used to combine dataframes on common columns or indices. Join is used to combine based on a key column or index. 

# In[52]:


import numpy as np


# In[53]:


df_1 = pd.DataFrame(np.random.uniform(1,2,size=(5, 4)), columns=list('ABCD'))
df_2 = pd.DataFrame(np.random.uniform(2,3,size=(5, 4)), columns=list('ABCD'))


# In[54]:


df_1_styler = df_1.style.set_table_attributes("style='display:inline;margin-right:10em'").set_caption('df_1').set_table_styles([{
    'selector': 'caption',
    'props': [
        ('text-align', 'center'),
        ('font-size', '14pt')
    ]
}])
df_2_styler = df_2.style.set_table_attributes("style='display:inline'").set_caption('df_2').set_table_styles([{
    'selector': 'caption',
    'props': [
        ('text-align', 'center'),
        ('font-size', '14pt')
    ]
}])

display_html(df_1_styler._repr_html_()+df_2_styler._repr_html_(), raw=True)


# In[55]:


df_new = pd.concat([df_1,df_2])#,ignore_index=True)
df_new


# In[56]:


df_new = pd.concat([df_1,df_2],axis=1)
df_new


# In[57]:


df_new = pd.concat([df_1,df_2],keys=["df_1","df_2"])
df_new


# In[58]:


df_new.loc["df_2"]


# **Merge** is used combine dataframe on one or more columns

# In[59]:


df3 = pd.read_csv("test.csv")
display(df3)
df4 = df3.copy(deep=True)
df4.loc[2]=["Peter", 20, "UK"] 
df4.loc[len(df4.index)] = ["Mohan", 25, "India"]
display(df4)

df_merged1 = pd.merge(df3,df4)
display(df_merged1)

df_merged2 = pd.merge(df3,df4,on=["Country","Name"],suffixes=('_df3', '_df4'))
display(df_merged2)


# **Join** is used to combine dataframes along a specific column. 

# In[60]:


df3.join(df4,lsuffix='_df3', rsuffix='_df4')


# In[61]:


df3


# In[62]:


df3.join(df4.set_index("Country"),on="Country", lsuffix='_df3', rsuffix='_df4')


# In[63]:


df3.join(df4.set_index("Country"),on="Country", lsuffix='_df3', rsuffix='_df4', how="outer")


# ### Groupby
# We can create groups for same values in a column to apply a function to all rows having a particular value.

# In[64]:


students = [["Sam","Peter","Mohan", "Mike"], ["UG","PG","UG","PG"], [70,80,90,70]]
df_students = pd.DataFrame(students).T
df_students.columns=["Name","Program","Marks"]
df_students


# In[65]:


df_students.set_index("Program", inplace=True)
display(df_students)


# In[66]:


df_students.groupby(level="Program")["Marks"].mean()


# ### Ploting
# Dataframe has a `plot()` function to do basic visualization. The `kind` attribute for this function can be used to change the plot type.

# In[67]:


df_col1 = pd.DataFrame(np.array(range(1,6))**2)
df_col2 = pd.DataFrame(np.array(range(1,6))**3)

df_comb = pd.concat([df_col1,df_col2], axis=1, ignore_index=True)
df_comb.columns = ["Squares", "Cubes"]
df_comb.index = range(1,6)
df_comb


# In[68]:


df_comb.plot()
df_comb.plot(kind="bar")


# ### The iris dataset

# In[69]:


csv_url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
# using the attribute information as the column names
col_names = ['Sepal_Length','Sepal_Width','Petal_Length','Petal_Width','Class']
iris =  pd.read_csv(csv_url, names = col_names)


# In[70]:


iris


# In[71]:


print("Shape", iris.shape)
print(iris.dtypes)


# In[72]:


iris.describe()


# In[73]:


iris.set_index("Class").groupby(level="Class").describe()


# In[74]:


iris.plot.scatter(x="Sepal_Length",y="Sepal_Width")


# In[75]:


import matplotlib.pyplot as plt
import seaborn as sns


# In[76]:



iris.set_index("Class").groupby(level="Class").plot.scatter(x="Sepal_Length",y="Petal_Length")


# In[77]:


sns.jointplot(data=iris,x="Sepal_Length",y="Petal_Length",hue="Class")

