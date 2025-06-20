# python fundamentals
print("Hello, World!")

#conditional statements
#greater than

n = int(input("Enter first number: "))
m = int(input("Enter second number: "))

if n>m:
    print(n, " is greterthan" ,m)
else:
    print(n, " is lessthan" ,m)

    #chek number is prime or not

















# grade and percentage calculation
# Input the total marks and obtained marks
total_marks = 500
obtained_marks = int(input("Enter the obtained marks: "))


# Calculate the percentage
percentage = (obtained_marks / total_marks) * 100
if percentage >= 90:
    print(f"Your percentage is {percentage}%. You have an A+ grade.")   

elif percentage >= 80:
    print(f"Your percentage is {percentage}%. You have an A grade.")
elif percentage >= 70:
    print(f"Your percentage is {percentage}%. You have a B grade.")
elif percentage >= 60:
    print(f"Your percentage is {percentage}%. You have a C grade.")
elif percentage >= 50:
    print(f"Your percentage is {percentage}%. You have a D grade.")
else:
    print(f"Your percentage is {percentage}%. You have an F grade. Please try again.")


