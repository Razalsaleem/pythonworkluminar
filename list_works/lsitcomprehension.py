# lst=[2,3,4,6,7,8]

# squares=[]
# for n in lst:
#     sq=n**2
#     squares.append(sq)
# print(squares)



# cubes=[n**3 for n in lst]
# print(cubes)

# squares=[n**2 for n in lst]
# print(squares)

# add=[n+2 for n in lst]
# print(add)

# evens=[n for n in lst if n%2==0]
# print(evens)

# odd=[n for n in lst if n%2!=0]
# print(odd)

years=[y for y in range(1800,2026)]

# century_years=[y for y in years if y%100==0]
# print(century_years)

not_century_years=[y for y in years if y%100!=0]
print(not_century_years)
# print(years)
