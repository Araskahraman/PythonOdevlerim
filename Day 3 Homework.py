#!/usr/bin/env python
# coding: utf-8

# In[ ]:


user_name = "Aras"
password ="Kahraman"

user_name1 =input("Please enter your user name")

password1= input("Please enter your password")

if (user_name != user_name1 and password == password1):
    print("Invalid User Name")
elif (user_name==user_name1 and password != password1):
    print("Invalid Password")
elif (user_name != user_name1 and password!= password1):
    print("Invalid user name and password")
else:
    print("Congrats, you are logged in")


# In[ ]:




