from re import*


text="abcd12kABC@#"

# pattern="\d"  # only to take digits

# pattern="\D"    # without digits

# pattern="\w"    # without characters

pattern="\W"     # only characters

matcher=finditer(pattern,text)

for m in matcher:
    print(m.group(),m.start())