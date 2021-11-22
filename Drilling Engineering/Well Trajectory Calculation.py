#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Well Trajectory Calculation
#Referance H. Rabia


# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math


# In[2]:


TVD1 = float(input("Enter True Vertical Depth @ seaction1 (ft)"))
del_N1 = float(input("Enter northing co-ordinate @ Seaction1 (ft)"))
del_E1 = float(input("Enter easting co-ordinate @ Seaction1 (ft)"))
TB = float(input("Enter Target Bearing(Degree)"))
MD = float(input("Enter Total Measured Depth(ft)"))
I1 = float(input("Enter Inclination @seaction1(degree)"))
I2 = float(input("Enter Inclination @seaction2(degree)"))
A1 = float(input("Enter corrected azimuth @ seaction1(degree)"))
A2 = float(input("Enter corrected azimuth @ seaction2(degree)"))
P = print(math.pi)
VS = float(input("Enter Vertical Seaction(ft)"))


# In[3]:


TVD = 360*200*((math.sin(math.radians(I2)))-(math.sin(math.radians(I1))))/(2*(math.pi)*((I2)-(I1)))
print("The value of True vertical depth is",TVD,"ft")


# In[4]:


#TVD at seaction 2
TVD2 = TVD1+TVD
print("The value of True vertical depth @ seaction 2 is",TVD2,"ft")


# In[5]:


del_N = 360**2*MD*((math.cos(math.radians(15)))-(math.cos(math.radians(19))))*((math.sin(math.radians(55)))-(math.sin(math.radians(45))))/(4*(math.pi**2)*(A2-A1)*(I2-I1))
print("the value of northing co-ordinate",del_N,"ft sq.")
                                                                                                                                       


# In[6]:


# Increment of northing co-ordinate at seaction 2
del_N2 = del_N1+del_N
print("The vlaue of Increment of northing co-ordinate at seaction 2 ",del_N2,"ft sq.")


# In[7]:


del_E = 360**2*MD*((math.cos(math.radians(15)))-(math.cos(math.radians(19))))*((math.cos(math.radians(45)))-(math.cos(math.radians(55))))/(4*(math.pi**2)*(A2-A1)*(I2-I1))
print("the value of easting co-ordinate",del_E,"ft sq.")


# In[8]:


# Increment of easting co-ordinate at seaction 2
del_E2 = del_E1+del_E
print("the value of easting co-ordinate",del_E2,"ft sq.")


# In[11]:


#thita
T=65-math.degrees(math.atan((44.73)/(37.53)))
T


# In[12]:


VS1 = math.sqrt((del_E**2)+(del_N**2))*(math.cos(math.radians(T)))
print("The value of vertical seaction is",VS1,"ft")


# In[13]:


#vertical seaction at seaction 2
VS2 = VS+VS1
print("The value of vertical seaction is",VS2,"ft")


# In[30]:


Y = [0,500,1000,1500,2000]
X = [0,5,10,15,20]
plt.plot(X,Y)
plt.show()


# In[15]:


#Cos DL is dog leg severity

dl = (math.cos(math.radians(19-15)))-((math.sin(math.radians(15)))*(math.sin(math.radians(19))))*(1-(math.cos(math.radians(55-45))))
print("The value of dog-leg is",dl,"degree")


# In[17]:


#to find cos inverce 
DL=(math.degrees(math.acos(dl)))
DL


# In[20]:


#dog -leg severity 
DLS= ((DL)/(MD)*(100))
print("The value of dog-leg severity is",DLS,"deg/100ft")


# In[ ]:


#AKSHAY MANJRAMKAR

