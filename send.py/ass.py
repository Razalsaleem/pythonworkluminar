#1

user_text=int(input("enter a number"))
if user_text>10 and user_text<=20:
    print("thank you")
else:
    print("incorrect answer")   



#2

user=int(input("enter a number  "))
if user<10:
    print("too low")
elif user<=20:
    print("correct")
else:
    print("too high")

#3

age=int(input("enter your age"))
if age>=18:
    print("you can vote")
elif age==17:
    print("you can learn to drive")
elif age<=16:
    print("you can go to treat")


#4

number=int(input("enter a number 1 or 2 or 3"))
if number==1:
    print("thank you")
elif number==2:
    print("well done")
elif number==3:
    print("correct")
else:
    print("error message")


#5
 
num=int(input("enter the number  "))
if num%2==0 and num%3==0:
    print(num,"is divisible by both 2 & 3")
else:
    print("not divisible")

#6

ch=input("enter a character  ")
if ch in ["a","e","i","o","u"]:
    print(ch, "is a vowel")
else:
    print("not a vowel")

#7

num=int(input("enter the num: "))
i=1
for i in range (1,11):
    print(num*i)

#8

start=int(input("enter the range: "))
end=int(input("enter the range: "))
for num in range(start, end + 1):
        if num % 2 == 0:
            print(num)

#9

username= input("enter the name : ")



x=1
while (x<=3):
    print(username)
    x=x+1


#10

name=input("enter the name: ")
num=int(input("enter the num: "))

if num<10:
    value=name*num
    print(value)
else:
    print("too high")


#11

numpep=int(input("how many people you wants to invite to the party: "))

def invitepep():

    if numpep < 10:
        for i in range(numpep):
            name = input(f"Enter the name of peoples {i + 1}: ")
            print(f"{name} has been invited.")
    else:
        print("Too many people")

invitepep()

#12

num=int(input("enter a num: "))

while num <=5:
    num=int(input("enter a number: "))
print(f"the num you entered was a{num}")

#13
user=int(input("enter the number  "))
if user<10:
    print("too low")
elif user<=20:
    print("correct")
else:
    print("too high")


#14    

for i in range(10,310,+10):
    print(i)

#15

avg=[]

for i in range (0,5):
    num=int(input("enter the number: "))
    avg.append(num)

average=((sum(avg))//5)

print(f"avg of 5 numbers is {average}")