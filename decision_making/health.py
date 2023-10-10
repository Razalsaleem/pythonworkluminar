tummy_size=int(input("enter the tummy size :"))
buttock_size=int(input("enter the buttock size :"))
gender=input("enter gender male or female :")
measurement=tummy_size/buttock_size

val=round(measurement,2)
print(val)

if gender=="female":
    if(measurement<=0.80):
       print("health risk is low body shape is pear") 
    elif(measurement<=0.85):
       print("health risk is moderate body shape is avacado") 
    else:
       print("health risk is high body shape is apple") 
elif gender=="male":
    if(measurement<=0.95):
        print("health risk is low body shape is pear") 
    elif(val<0.96):
       print("health risk is moderate body shape is avacado")
    else:
       print("health risk is high body shape is apple") 
else:
    print("enter a valid gender")








