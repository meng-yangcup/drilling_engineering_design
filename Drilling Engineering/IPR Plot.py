#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# In[3]:



porosity = float(input("Enter Porosity"))
K = float(input("Enter Perm.(md)"))
h = float(input("Enter pay zone thicknes(Feet)"))
P = float(input("Enter  Reservoir Pressure(psi)"))
Pb = float(input("Enter Bubble Point Pressure(psi)"))
Bo = float(input("Enter Formation Volume Factor"))
Viscosity  = float(input("Enter fluid viscosity(cp)"))
ct = float(input("Enter Total Compressibility(psi-1)"))
A = float(input("Enter Drainage Area(Acres)"))
re = np.sqrt(43560*A/3.14)
rw = float(input("Enter Wellbore radius(ft)"))
S = float(input("Enter Skin Factor"))


# In[4]:


J = K*h/(141.2*Bo*Viscosity*(np.log(re/rw)-0.75+S))
print("The value of productivity index is", J)


# In[5]:


qmax = J*P/1.8
print("The value of Qmax is ", qmax, "stb/day")


# In[6]:


a = np.arange(0,2500,500)
b = np.append(a,2500)
pwf = b[-1::-1]
pwf


# In[7]:


flowrate = []
for i in pwf:
    q = qmax*(1-0.2*(i/P)-0.8*((i/P)**2))
    flowrate.append(q)
flowrates = np.array(flowrate)
flowrates


# In[10]:


df = pd.DataFrame(flowrates,pwf)
df


# In[9]:


plt.figure()
plt.plot(flowrates,pwf)
plt.xlabel("Flowrate(stb/day)")
plt.ylabel("pwf(psia)")
plt.title("Vogel's IPR for Saturated Reservoir")
plt.show()


# In[ ]:


#AKSHAY MANJRAMKAR

