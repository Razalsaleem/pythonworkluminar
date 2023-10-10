text="ABBCDAE"
wc={}                   #empty dictionary
dup_list=[]             #empty list

for ch in text:
    if ch in wc:
        dup_list.append(ch)
    else:
        wc[ch]=1
print(dup_list[1])