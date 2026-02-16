# Problem 1: Easy 🟢
# Scenario: You need to print numbers from 1 to 10.
# Challenge: Write a loop that prints: 1 2 3 4 5 6 7 8 9 10
# Hint: Remember, range(1, 11) goes from 1 to 10!

for i in range(1,11):
    print(i)

# Problem 2: Medium 🟡
# Scenario: You're validating a PIN code. You need to count how many digits are in a number.
# Challenge: Write a function count digits(n) that returns how many digits are in a positive integer.
# Examples: count digits(5847) → 4, count digits(100) → 3

def count_number(pincode):
        count = 0
        for i in str(pincode):
            count=count+1
        return count
    
# pincode_count=count_number(431503)
# print(pincode_count)

# Problem 3: Application 🔴
# Scenario: As an SDET, you need to generate test data with IDs counting backward.
# Challenge: Create a f
# unction that generates test IDs from 100 down to 1, formatted as "CLEANUP099" , etc.
# Bonus: The IDs should be zero-padded to 3 digits.

def clean_userstory():
      for i in range(100,0,-1):
            print(f"CLEANUP_{i}")

clean_userstory()


#Enumerate iterate with index
def iterate_with_index(pincode):
    count1=0
    for i ,val in enumerate(pincode):
        count1=i+1
    return count1
total_num=iterate_with_index([4,3,1,5,0,3])
print(total_num)

#print even numbers

for i in range(0,11,2):
    print(i)

# extract rightmost digit
num=14535
elastdigit=num%10
print("Lastmost digit is: ",elastdigit)

#remove lastmost digit
num1=58375
rlastdigit=num1//10
print("remove lastmost digit: ",rlastdigit)

            


    


            
            
