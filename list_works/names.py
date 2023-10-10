# all_users=["mohanlal","fahad","unny","mammotty","nivin"]

# nivin_friends=["mohanlal","fahad","unny"]
 
# for u in all_users:
#     if u not in nivin_friends:
#         print(u)


#or

# all_users=["mohanlal","fahad","unny","mammotty","nivin"]
#             #    0         1       2      3          4   
# nivin_friends=["mohanlal","fahad","unny"]
# #suggessions for nivin
# suggession_list=[]
# for e in all_users:
#     if e not in nivin_friends:
#         suggession_list.append(e)
# suggession_list.pop(suggession_list.index("nivin"))                
# print(suggession_list)
        


#find mutual frnds
nivin_friends=["mohanlal","fahad","unny"]
fahad_friends=["mohanlal","mammooty","unny"]
equalist=[]
for e in nivin_friends:
    if e in fahad_friends:
        equalist.append(e)
print(equalist)
