start=10
even_sum=0
odd_sum=0

while(start<=20):
    if(start%2==0):
       even_sum=even_sum+start
    else:
     odd_sum=odd_sum+start
    start+=1
print("evensum",even_sum)
print("oddsum",odd_sum)