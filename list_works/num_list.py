numbers=[1,4,10,11,12]

even_list=[]

odd_list=[]

for n in numbers:
    even_list.append(n) if n%2==0 else odd_list.append(n)
print(even_list)

print(odd_list)