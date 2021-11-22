#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[14]:


L_dp = float(input("Enter length of drill pipe(ft)"))
W_dp = float(input("Enter weight of drill pipe(lbm/ft)"))
L_dc = float(input("Enter length of drill collar(ft)"))
W_dc = float(input("Enter  weight of drill collar(lbm/ft)"))
mud_w = float(input("Enter mud weight(ppg)"))


# In[15]:


BF = 1 - (15/65.5)

W_air = L_dp*w_dp + L_dc*w_dc

W_buoyed = W_air*BF


# In[16]:


print(W_buoyed)


# In[24]:


p1 = 0.052*mud_w*L_dp
print("The value of Hydrostatic Pressure at the TOp of Drill collars is",p1,"psi")
depth = np.arange(12000,-1,-2000)
stress = np.arange(-500,501,100) 


# In[25]:


p2 = 0.052*mud_w*(L_dp+L_dc)
print("The value of hydrostatic at the bottom of the drill collars is",p2,"psi")


# In[26]:


A_dp = (w_dp/490)*144  
print("The value of Cross Sectional Area of drillpipe is",A_dp,"sq. in")


# In[27]:


A_dc = (w_dc/490)*144 
print("The value of Cross Sectional Area of drillcollar is",A_dc,"sq. in")


# In[35]:


d_dp = np.arange(10001,-1,-100)

d_dc = np.arange (12001,10001,-100)

F_dp = 178870.2290076336 - 19.5*d_dp

F_dc = 1201000 - 147*d_dc

print("The value of weight at drillpipe is",F_dp)
print("The value of weight at drillcollar is",F_dc)


# In[36]:


d_0 = [10000,10000,10000]

F_0 = [F_dp[0], 0 , F_dc[-1]]


# In[39]:


plt.style.use('default')

plt.figure(figsize=(16,8))

plt.title('Axial Tensions in a Drill String as a Function of Depth')

plt.plot(F_dp,d_dp, label = 'Tension')

plt.plot(F_0,d_0, label = 'Neutral')

plt.plot(F_dc,d_dc, label = 'Compression')

plt.xlabel('Axial Stress, lbf')

plt.ylabel('Depth, ft')

plt.legend()

plt.ylim(15000,0)

plt.grid()


# In[ ]:




