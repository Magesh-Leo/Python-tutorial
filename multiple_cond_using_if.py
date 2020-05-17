# multiple conditions check using if condition 

count=0
print('That condition getting infinite Answers')
for x in range(1,100000):
    if ((x%6 == 1) and (x%5 == 1) and
        (x%4 == 1) and (x%3 == 1) and
        (x%2 == 1) and (x%7 == 0)):
        count+=1
        
        print(f"{count} )The ans is :{x}")
