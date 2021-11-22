#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[3]:


q = 250 #stb/d

tp = 460 #hrs

Pi = 4412 #psia

h = 69 #ft

phi = 3.9/100

ct = 17E-6 #psi-1

B = 1.136 #rb/stb

mu = 0.8 #cp

rw = 0.198 #ft


# In[11]:


df = pd.read_excel('C:\\Users\\Akshay M\\Desktop\\pbt.xlsx')


# In[12]:


df.head()


# In[14]:


df['delP'] = Pi - df['Pwf']
df


# In[25]:


t = np.array(df['t'])

dt = []
for i in range(len(t)):

  if i==0:
    dt.append(t[i])
  else:
    dt.append(t[i] - t[i-1])

dt = np.array(dt)
df['dt'] = dt
df


# In[20]:


p = np.array(df['delP'])

dp = []
for j in range(len(p)):

  if j==0:
    dp.append(p[j])
  else:
    dp.append(p[j] - p[j-1])

dp = np.array(dp)
df['dP'] = dp
dp


# In[21]:


P_dash = (df['t'][1:])*(df['dP'][1:])/df['dt'][1:]
P_dash


# In[26]:


P_del = df['delP'][1:]
P_del


# In[27]:


plt.style.use('default')

plt.figure(figsize=(20,12))

plt.loglog(df['t'][1:], P_dash,linestyle='--', marker='o', color='b',label='Derivative Plot')

plt.loglog(df['t'][1:], P_del,linestyle='--', marker='o', color='r',label='Drawdown')

plt.title('Log-Log Plot (diagnostic Plot)')

plt.xlabel('Time, hrs')
plt.ylabel("delP and (delP)'")

plt.legend(loc='best')
plt.grid()


# In[28]:


df_IARF = df[(df['t']>=10) & (df['t']<=100)]
df_IARF


# In[29]:


df_IARF['logt'] = np.log10(df_IARF['t'])
df_IARF


# In[33]:


plt.plot(df_IARF['logt'],df_IARF['Pwf'],label='Almost Straight line')

plt.title('Semi-Log (Conventional Plot) for IARF')

plt.xlabel('Time, hrs')
plt.ylabel("Pwf, Psia")

plt.legend(loc='best')
plt.grid()


# In[34]:


coeffs = np.polyfit(df_IARF['logt'],df_IARF['Pwf'],1)
coeffs


# In[37]:


m = coeffs[0]
k = abs(162.6*q*mu*B/m/h)
k


# In[ ]:


#Hence the Natural Absolute Permeability of the reservoir is : 6.138060324686079 md

#AKSHAY MANJRAMKAR

