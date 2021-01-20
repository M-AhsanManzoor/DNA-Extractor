#!/usr/bin/env python
# coding: utf-8
# Contribute by Muhammad Ahsan Manzoor
# In[21]:


import os
listdir = os.listdir(".")
slis = [item for item in listdir if item.lower().__contains__('.sq') == True]


# In[22]:


print(slis)


# In[ ]:


for fname in slis:
    with open(fname, "r") as fin: 
        data = fin.readlines()[0]
    with open(fname[:-3] + ".fasta", "w") as fout:
        fout.write(">"+fname[:-3] +"\t" + str(len(data)) + "\n")
        i = 0
        for ch in data:
            if i == 70:
                i = 0
                fout.write("\n")
            fout.write(ch)
            i= i+1
            

