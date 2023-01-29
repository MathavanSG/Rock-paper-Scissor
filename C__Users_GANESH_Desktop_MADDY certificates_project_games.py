#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random


# In[2]:


user_wins=0


# In[3]:


computer_wins=0


# In[4]:


options=["Rock","Paper","Scissor"]


# In[ ]:


user_wins=0
computer_wins=0
options=["Rock","Paper","Scissor"]
while True:
    user_input=input("Type Rock/Paper/Scissor or Q to quit: ").lower()
    if user_input=="q":
        break
    if user_input in options:
        continue
    random_number=random.randint(0,2)
    #rock-0,paper-1,scissor-2
    computer_pick=options[random_number]
    print("computer picked",computer_pick+".")
    
    if user_input=="Rock" and computer_pick=="Scissor":
        print("you won")
        user_wins+=1
        continue

    elif user_input=="Paper" and computer_pick=="Rock":
        print("user won")
        user_wins+=1
        continue
    elif user_input=="Scissor" and computer_pick=="Paper":
        print("user won")
        user_wins+=1
        break
    if user_input==computer_pick:
        print("draw")
        user_wins==computer_wins==0
        continue
    else:
        print("computer won")
        computer_wins+=1
print(computer_wins)
print(user_wins)

print("Good bye")

        
    
        


# In[ ]:




