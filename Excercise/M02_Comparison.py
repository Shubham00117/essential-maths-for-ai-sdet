#Simple Comparison 
age = 25

if age>=18:
    print("Adult can vote!")
else:
    print("minor cannot vote!")


#multi Comparison
score=45

if score>=90:
    print("Distinction")
elif score>=80:
    print("First Class")
elif score>=70:
    print("Second Class")
elif score>=60:
    print("avg class")
elif score>=50:
    print("Below avg")
elif score>=40:
    print("below avg plus")
elif score<40:
    print("Faild")

#find largest number
a=10
b=20
c=156

if a > b and a > c:
    print("A is greater")
elif b > a and b > c:
    print("B is greater")
elif c > a and c > b:
    print("C is greater")
else:
    print("Input is wrong")

print(10%3==1)