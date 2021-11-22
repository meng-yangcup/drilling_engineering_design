#!/usr/bin/env python
# coding: utf-8


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd



df = pd.DataFrame({"FP": range(10000),"h": range(10000),"GH": range(10000),"0.052": range(10000),"MW": range(10000),"HSPG": range(10000),(SIDPP)})
df


h = float(input("Enter depth"))
MW = float(input("Enter mud weight(ppg)"))
Pwf = float(input("Enter  kick(ppg)"))
Vi = float(input("Enter kick volume(bbls)"))
ID = float(input("Enter casing ID(inch)"))
Dod = float(input("Enter drill string OD(inch)"))


HSP=0.052*MW*h
print("HydroStatic Pressure", HSP,"psi")

FP=0.052*Pwf*h
print("Formation Pressure",FP,"psi")



SIDPP=FP-HSP
print("shut in drill pipe pressure",SIDPP,"psi")



AC=(ID**2-Dod**2)/1029.4
print("Annalus Capacity",AC)



GH=Vi/AC
print("Gas Influsx Height",GH,"ft")



HSPG=0.12*GH
print("Hydrostatic Pressure of gas",HSPG,"psi")



SICPP=(FP)-((h-GH)*0.052*MW+HSPG)
print("Shut in casing pressure",SICPP,"psi")



PAB=(FP)-(GH*0.12)
print("Pressure at bubble",PAB,"psi")





