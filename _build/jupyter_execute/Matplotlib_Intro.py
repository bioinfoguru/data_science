#!/usr/bin/env python
# coding: utf-8

# ## Introduction to Matplotlib
# A Python library for data visualization. It offers variety of functions to plot different types of graphs which can be customised to create publication quality figures. The `pyplot` function in this library is used for instantiating a matplotlib graph object.

# In[1]:


import matplotlib.pyplot as plt


# In[4]:


x = range(1,11)
y = [a**2 for a in x]

plt.plot(x,y) #line plot

plt.scatter(x,y) #scatter plot
plt.xlabel("Number")
plt.ylabel("Square")

plt.show()


# In[9]:


x = range(1,11)
y = [a**2 for a in x]
plt.scatter(x,y)
plt.xlabel("Number", fontsize=12)
plt.ylabel("Square of the Number", fontsize=12)
plt.show()


# In[5]:


x = range(1,11)
y = [a**2 for a in x]
z = [a**3 for a in x]
plt.scatter(x,y,marker="^", color="red")
plt.scatter(x,z,marker="*", color="purple")
plt.xlabel("Number", fontsize=12)
plt.ylabel("Value", fontsize=12)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
plt.legend(["Squares","Cubes"])
plt.show()


# ### Subplots
# The `pyplot` class has `subplot()` function that return a figure and and axes object. These can be used to access and manipulated different elements of the graph. In addition, subplots can take number of plots as argument to create a figure with multiple plots. This function has a keyword argument `figsize` to specify the size of the plot.

# In[6]:


x = range(1,11)
y = [a**2 for a in x]
z = [a**3 for a in x]

fig, ax = plt.subplots()

ax.scatter(x,y,marker="^", color="red")
ax.scatter(x,z,marker="*", color="purple")

plt.show()


# In[15]:


x = range(1,11)
y = [a**2 for a in x]
z = [a**3 for a in x]

fig, ax = plt.subplots(2,1,sharex=True) #create subplots with two rows and one column



ax[0].scatter(x,y,marker="^", color="red")
ax[1].scatter(x,z,marker="*", color="purple")

#ax[0].set_xlabel("Number")
ax[1].set_xlabel("Number")

ax[0].set_ylabel("Squares")
ax[1].set_ylabel("Cubes")

#plt.subplots_adjust(hspace = 0.5)#sharex argument for subplots
plt.show()


# In[69]:


x = range(1,11)
y = [a**2 for a in x]
z = [a**3 for a in x]

fig, ax = plt.subplots(2,2) #create subplots with two rows and two columns
ax[0,0].scatter(x,y,marker="^", color="red")
ax[1,0].scatter(x,z,marker="*", color="purple")
ax[1,0].bar(x,z,color="purple",alpha=0.1)

ax[0,1].bar(x,y,color="red")
ax[1,1].bar(x,z,color="purple")


fig.savefig("subplot.png", dpi=300)
plt.show()


# ### plt.subplot (without 's')
# The `subplot()` function is similar to subplots with a difference that it take an additional argument - index. This can be used to make axes span multiple columns within the subplot. 

# In[96]:


x = range(1,11)
y = [a**2 for a in x]
z = [a**3 for a in x]

ax1 = plt.subplot(2,1,1) 
ax2 = plt.subplot(2,2,3)
ax3 = plt.subplot(2,2,4)

ax1.scatter(x,y,marker="^", color="red")
ax1.bar(x,y, color="red",alpha=0.1)
ax2.scatter(x,z,marker="*", color="purple")
ax3.bar(x,z,color="purple")

plt.savefig("subplots2.png",dpi=300)
plt.show()

