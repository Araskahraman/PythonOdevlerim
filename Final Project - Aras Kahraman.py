#!/usr/bin/env python
# coding: utf-8

# In[32]:


class managers:
    def __init__(self, name, lname, age):
        self.name = name
        self.lname = lname
        self.age = age
        self.language = []
    
    def print_name(self):
        print(self.name  + " " + self.lname)
        
    def showage(self):
        print(self.name  +  " " + self.lname, "is", self.age +  " years old ")
        
    def addlanguage(self, newlanguage):
        print("Adding new language:", newlanguage)
        self.language.append(newlanguage)
        
    def showinfo(self):
        print(self.name, self.lname, "is", self.age, "and", "speaks", self.language)
        


# In[31]:


class employees:
    def __init__(self, name, lname, age, language):
        self.name = name
        self.lname = lname
        self.age = age
        self.language = language
    
    def print_name(self):
        print(self.name  + " " + self.lname)
        
    def showage(self):
        print(self.name  +  " " + self.lname, "is", self.age +  " years old ")
        
    def speak_language(self):
        print(self.name, self.lname, "speaks", self.language)
        
    def showinfo(self):
        print(self.name, self.lname, "is", self.age, "and", "speaks", self.language)


# In[33]:


manager1 = managers("Mert", "Trump", "44")
manager2 = managers("Gamze", "Cakır", "43")


# In[34]:


manager1.print_name()


# In[35]:


manager1.showage()


# In[36]:


manager1.addlanguage("Spanish and English")


# In[37]:


manager1.showinfo()


# In[38]:


manager2.print_name()


# In[39]:


manager2.showage()


# In[40]:


manager2.addlanguage("English and French")


# In[41]:


manager2.showinfo()


# In[42]:


employee1 = employees("Aras", "Kahraman", "28", "English and Italian" )
employee2 = employees("Evrim", "Solhan", "27", "Turkish")
employee3 = employees("Ozlem", "İsci", "34", "Russian")


# In[43]:


employee1.showinfo()


# In[44]:


employee2.showinfo()


# In[45]:


employee3.showinfo()


# In[ ]:




