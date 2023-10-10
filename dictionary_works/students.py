student={"name":"razal","rollno":100,"course":"django"}
# print(student)

# if "total" in student:
#     print("present")
# else:
#     print("not present")


# student["grade"]="A"
# print(student)

# for k in student.keys(): # for to get keys
#     print(k)

# for v in student.values(): # for to get values
#     print(v)


for k,v in student.items(): #To get both the  keys and values.
    print(k,v)