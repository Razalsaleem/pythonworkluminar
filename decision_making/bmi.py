height_incm=165
weight_inkg=99

height_inmeter=height_incm/100
bmi=weight_inkg//height_inmeter**2
print(bmi)

if(bmi<19):
    print("underweight")
elif(bmi<25):
    print("normal weight")
elif(bmi<=30):
    print("over weight")
elif(bmi>30):
    print("obesity")