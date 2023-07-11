# Perform below operations:

ls=[]
i=1
print("Enter numbers:-")
while i<=5:
    n=int(input())
    ls.append(n)
    i+=1; 
print(ls)

# 1) Calculate the sum of all the elements in the list
print(sum(ls))

# 2) Find the smallest number
print(min(ls))

# 3) Find the largest number
print(max(ls))

# 4) Display list in ascending order
ls.sort()
print(ls)

#5) Display list in descending order
ls.sort(reverse=True)
print(ls)

#6) Convert list into tuple
print(tuple(ls))

#7) Delete the list
del ls
print(ls)