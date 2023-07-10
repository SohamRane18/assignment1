# Break

for i in range(1,20):
     if i==6:  
           break
else:
         print(i)

#  Pass

s="Soham"
for i in s:
        if i=="a":
           pass
else:
         print(i)
print("Pass.")

# Continue

for i in range(1,20):
    if i==6: 
        continue
    else:
        print(i)


# for with else

for i in range(1,20):
    print(i)
else:
    print("FOR WITH ELSE")


# While with else

i=1
while i<=101:
     if i %2==0:
         print("Even Number",i)
     else:
         print("Odd Number",i)
     i+=1
