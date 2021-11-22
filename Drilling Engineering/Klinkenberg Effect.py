#!/usr/bin/env python
# coding: utf-8

# In[3]:


#The permeability of a core plug is measured by air. Only one measurement is made at a mean pressure of 2.152 psi. 
#The air permeability is 46.6 md. Estimate the absolute permeability of the core sample. 
#Compare the result with the actual absolute permeability of 23.66 md.


# In[15]:


import numpy as np
import matplotlib.pyplot as plt
k = float(input("Enter the initial guess of absolute permeability(md):"))
pmean = float(input("Enter The mean pressure(psi):"))
kgas = float(input("Enter the gas perm.(md):"))


while abs(6.9*(k**0.64)+pmean*k-pmean*kgas) > 0.0001:
    k = k - (6.9*(k**0.64)+pmean*k - pmean*kgas)/(4.416*(k**(-0.36))+pmean)
    
print("The value of absolute permeability after iteration or gas permeability at infinite pmean is ",k)

x = [0,1/pmean]
y = [k,kgas]

coefficients = np.polyfit(x,y,1)
polynomial = np.poly1d(coefficients)
x_axis = np.linspace(0,0.2,0.01)
y_axis = polynomial(x_axis)
plt.plot(x_axis, y_axis)
plt.plot(x,y)
plt.xlabel("1/Mean_pressure (psi^-1)")
plt.ylabel("Measured Gas Permeability(md)")
plt.title("The Klinkenberg Effect")
plt.grid(True)
plt.show()


# In[ ]:


#Courtsey- Tarek Ahmed

