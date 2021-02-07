#!/usr/bin/env python
# coding: utf-8

# In[82]:


class Animals:
    def __init__(self, name, age, legs):
        self.name = name
        self.age = age
        self.legs = legs
    
    def print_name(self):
        print(self.name) 
        
    def showage(self):
        print(self.name  +  " is", self.age +  " years old ")
        
    def number_legs(self):
        print(self.name, "has", self.legs, "legs")
        
    def showinfo(self):
        print(self.name, "is", self.age, "years old and", "has", self.legs, "legs" )
        
    


# In[83]:


class Dogs(Animals):
    pass

dogs = Animals("Fluffy", "3", "4")
dogs.print_name()


# In[84]:


dogs.showage()


# In[85]:


dogs.number_legs()


# In[86]:


dogs.showinfo()


# In[87]:


class Cats(Animals):
    pass

cats = Animals("Luna", "5", "4")
cats.print_name()


# In[88]:


cats.showage()


# In[89]:


cats.number_legs()


# In[90]:


cats.showinfo()


# In[ ]:




