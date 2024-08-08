"""
a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
c=int(input("enter the third number:"))
r1=(-b+((b*2)-(4*a*c))*0.5)/(2*a)
r2=(-b-((b*2)-(4*a*c))*0.5)/(2*a)
print("the first root is:",r1,r2) 
"""
import math

a = int(input('Enter A value: '))
b = int(input('Enter B value: '))
c = int(input('Enter C value: '))

discriminant = b**2 - 4*a*c

if discriminant >= 0:
    r1 = (-b + math.sqrt(discriminant)) / (2*a)
    r2 = (-b - math.sqrt(discriminant)) / (2*a)
    
    print("The solutions for the quadratic equation are:", r1, "and", r2)
else:
    print("No real solutions exist.")