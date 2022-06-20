#!/usr/bin/env python
# coding: utf-8

# ## Interactive data visualization
# **Ipython widgets**

# In[2]:


import matplotlib.pyplot as plt
import numpy as np
from IPython.display import Markdown, display, HTML
from ipywidgets import widgets, interact, Dropdown


# In[3]:


def plot1(Numbers):
    x = range(1,Numbers+1)
    y = [a**2 for a in x]
    plt.bar(x,y)
    plt.xlabel("Number")
    plt.ylabel("Square")


# In[4]:


interact(plot1, Numbers=widgets.IntSlider(min=5, max=20, step=1, value=10));


# Toogle widget

# In[5]:


def plot2(calc):
    with out:
        x = range(1,5+1)
        y = [a**2 for a in x]
        z = [a**3 for a in x]
        if(calc=="Squares"):
            plt.bar(x,y, width=0.4, label="Squares")
            plt.xlabel("Number")
            plt.ylabel("Square")
        if(calc=="Cubes"):
            plt.bar(x,z, width=0.4, label="Cubes")
            plt.xlabel("Number")
            plt.ylabel("Cube")
        if(calc=="both"):
            X_axis = np.arange(len(x))
            plt.bar(X_axis-0.1,y, width=0.2, label="Squares")
            plt.bar(X_axis+0.1,z, width=0.2, label="Cubes")
            plt.xlabel("Number")
            plt.ylabel("Square/Cube")
            plt.legend()
            

toggle = widgets.ToggleButtons(
    options=['Squares', 'Cubes','both'],
    description='Y-axis:',
    disabled=False,
    button_style='', 
    tooltips=['Calculate squares', 'Calculate cubes', 'Calculate both'],
)
out = widgets.Output()


# In[6]:


@interact
def clicked(a=toggle):
    plot2(a)


# ### Converting notebooks to html
# 
# The interactive visualization with the notebooks can be converted to static webpages in the html format. The [nbconvert](https://nbconvert.readthedocs.io/en/latest/) package facilitates converting Jupyter notebooks to html. It can be installed vi `pip install nbconvert`. Once installed, the following command can be used to convert a notebook `test.ipynb` to the html format.
# 
# `jupyter nbconvert --to html test.ipynb`
# 
# The resulting html file can be uploaded on any of the web hosting services such as Google Sites.
# 

# ### Bokeh library
# Installation - `pip install bokeh`

# In[7]:


import pandas as pd
from bokeh.plotting import figure, show


# In[11]:


## for showing graphs inside Jupyter notebook 
from bokeh.resources import INLINE
import bokeh.io
bokeh.io.output_notebook(INLINE)


# In[12]:


x = range(1,6)
y = [a**2 for a in x]
z = [b**3 for b in x]


# In[13]:


p = figure(title="Line plot", x_axis_label='Number', y_axis_label='Square')


# In[14]:


p.line(x, y, legend_label="Test") #line_width=2
show(p)


# In[15]:


p = figure(title="Line plot", x_axis_label='Number', y_axis_label='Value',          width=500, height=250)
p.line(x, y, legend_label="Square", color="teal", line_width=2)
p.line(x, z, legend_label="Cube", color="orange", line_width=2) 
show(p)


# In[16]:


#Changing graph theme
#from bokeh.io import curdoc
#curdoc().theme = "caliber"


# In[17]:


df1 = pd.read_csv("owid-covid-data.csv")


# In[20]:


df1['date'] = pd.to_datetime(df1['date'])


# In[21]:


p = figure(width=750, height=250,x_axis_type='datetime')
p.line(source=df1[df1["location"]=="India"], x="date", y="total_cases", color="indigo", line_width=2)
p.line(source=df1[df1["location"]=="United States"], x="date", y="total_cases", color="magenta", line_width=2)

show(p)

