import math
a=int(input("Enter a: "))
b=int(input("Enter b: "))
c=int(input("Enter c: "))
discriminant = b**2-4*a*c
if discriminant>0:
    root1=(-b + math.sqrt(discriminant))/(2*a)
    root2=(-b - math.sqrt(discriminant))/(2*a)
    print("The equation has two real roots: ",root1, "and",root2)
elif discriminant == 0:
    
    root=-b/(2*a)
    print("The equation has one real root: ",root)
else:
    print("does not have a real root")