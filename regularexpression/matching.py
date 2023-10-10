# word finding

from re import *

# text="abababcdab"

# matcher=finditer("abc",text)
# count=0

# for m in matcher:
#     print(m.start())
#     print(m.group())
#     count+=1
# print(count)

# digit finding,place

# from re import *

# text="abcdA&B*CD!7e9fk_"

# matcher=finditer("[aeiouAEIOU]",text)
# count=0

# for m in matcher:
#     print(f"location={m.start()}")
#     print(m.group())
#     count+=1
# print(count)


text="hellothere@12"

matcher=finditer("[^aeiou]",text)


for m in matcher:
    print(f"location={m.start()}")
    print(m.group())

