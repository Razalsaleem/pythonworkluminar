text="pneumonoultramicroscopicsilicovolcanoconiosis"

v_count=0
c_count=0

for ch in text:
    if ch in["a","e","i","o","u"]:
        v_count+=1
    else:
        c_count+=1
print("vowel count",v_count)
print("consenant count",c_count)