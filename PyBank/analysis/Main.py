#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

# csv path
df = pd.read_csv("/Users/devangpatel/Desktop/python-challenge copy/python-challenge/PyBank/Resources/budget_data.csv")

df.head()
# count the months
df["Date"].value_counts()

counts = df["Date"].value_counts()
# net P/L
df["Profit/Losses"].sum()

A = df["Profit/Losses"].sum() 
# change of P/L month to month
df["Profit/Losses"].diff()

df["Profit/Losses"].diff().mean()
# average change of P/L month to month
result = df["Profit/Losses"].diff().mean()
# largest increase of change for P/L
df["Profit/Losses"].diff().max()

df["change"] = df["Profit/Losses"].diff()

df["change"].max()

max = df[df["change"]==df["change"].max()]
# largest decrease of change for P/L
df["change"].min()

B = (int(df["change"].max()))

C = int(df["change"].min())

print("Financial Analysis")

print("")

print("-------------------------")

print("")

print("Total Months: ", len(counts))

print("")

print("Total: ", f"${A}") 

print("")

print("Average Change: ", f"${result:.2f}")

print("")

print("Greatest Increase in Profits: ", df.iloc[79, 0], f"(${B})")

print("")

print("Greatest Decrease in Profits: ", df.iloc[49, 0], f"(${C})")

# exports results to text file
import sys
file = open('output.txt', 'a')
sys.stdout = file

print("Financial Analysis")

print("")

print("-------------------------")

print("")

print("Total Months: ", len(counts))

print("")

print("Total: ", f"${A}") 

print("")

print("Average Change: ", f"${result:.2f}")

print("")

print("Greatest Increase in Profits: ", df.iloc[79, 0], f"(${B})")

print("")

print("Greatest Decrease in Profits: ", df.iloc[49, 0], f"(${C})")

file.close()


# In[ ]:




