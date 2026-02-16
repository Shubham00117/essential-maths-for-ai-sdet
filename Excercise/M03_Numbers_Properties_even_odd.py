print("Print even numbers: ")
num =[1,2,3,4,5,6,7,8,9,10]

#print even numbers in list
for n in num:
    if(n% 2 ==0):
        print(n)

#print odd numbers in list
print("Print odd numbers method 1: ")
for n in num:
    if(n% 2 ==1):
        print(n)
print("Print odd numbers method 2: ")
#print odd numbers in list
for n in num:
    if(n% 2 !=0):
        print(n)
