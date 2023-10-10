
# from re import*

# text="aababcaabdaaa"

# pattern="a+"  # minimum one number or one or more occurance

# matcher=finditer(pattern,text)

# for m in matcher:
#     print(m.group(),m.start())


from re import*

phone=input("enter the phone number")

rule="\d{11}"

matcher=fullmatch(rule,phone)

if (matcher==None):
    print("invalid number")
else:
    print("valid number")


