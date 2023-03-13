#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

df = pd.read_csv("/Users/devangpatel/Desktop/python-challenge copy/python-challenge/PyPoll/Resources/election_data.csv")

df.head()

len(df)

df["Candidate"].value_counts().rename_axis("Each Candidate").reset_index(name="Votes")

D = df["Candidate"].value_counts().rename_axis("Each Candidate").reset_index(name="Votes")

D[D["Votes"]==D["Votes"].max()]

df_C = df["Candidate"].value_counts().rename_axis("Each Candidate").reset_index(name="Votes")

df_C["Votes"].sum()

df_C.iat[1, 1] / (df_C["Votes"].sum())*(100)

A = df_C.iat[1, 1] / (df_C["Votes"].sum())*(100)

df_C.iat[0, 1] / (df_C["Votes"].sum())*(100)

B = df_C.iat[0, 1] / (df_C["Votes"].sum())*(100)

df_C.iat[2, 1] / (df_C["Votes"].sum())*(100)

C = df_C.iat[2, 1] / (df_C["Votes"].sum())*(100)

df_C["Votes"].div(df_C["Votes"].sum())*(100)

df_C["Percentage"] = df_C["Votes"].div(df_C["Votes"].sum())*(100)

Votes_Each = df["Candidate"].value_counts()

df["Votes"]=df["Candidate"].value_counts()

print("Total Votes: ",len(df) )
print("")
print("------------------------")
print("")
print("Charles Casper Stockham: ", f"{A:.3f}%", f"({df_C.iat[1, 1]})")
print("")
print("Diana DeGette: ", f"{B:.3f}%", f"({df_C.iat[0, 1]})")
print("")
print("Raymon Anthony Doane: ", f"{C:.3f}%", f"({df_C.iat[2, 1]})")
print("")
print("------------------------")
print("")
print("Winner: ", D.iloc[0, 0])
print("")
print("------------------------")


import sys
file = open('output.txt', 'a')
sys.stdout = file

print("Total Votes: ",len(df) )
print("")
print("------------------------")
print("")
print("Charles Casper Stockham: ", f"{A:.3f}%", f"({df_C.iat[1, 1]})")
print("")
print("Diana DeGette: ", f"{B:.3f}%", f"({df_C.iat[0, 1]})")
print("")
print("Raymon Anthony Doane: ", f"{C:.3f}%", f"({df_C.iat[2, 1]})")
print("")
print("------------------------")
print("")
print("Winner: ", D.iloc[0, 0])
print("")
print("------------------------")

file.close()


# In[ ]:




