print("School and College Student Enter 1 ")
print("University Student Enter 2")

print("Please Enter 1 or 2: ")
class1 = int(input())
if class1 == 1:
    gpa = float(input("Enter Your Mark:"))
    if gpa>=80 and gpa<=100:
        print("A+")
    elif gpa>=70 and gpa<=79:
        print("A")
    elif gpa>=60 and gpa<=69:
        print("A-")
    elif gpa>=50 and gpa<=59:
        print("B")
    elif gpa>=40 and gpa<=49:
        print("C")
    elif gpa>=33 and gpa<=39:
        print("D")
    elif gpa>=0 and gpa<=32:
        print("F")
else:
    print("System Error")

if class1 == 2:
    cgpa = float(input("Enter your Mark:"))
    if cgpa>=80 and cgpa<=100:
        print("A+")
    elif cgpa >= 75 and cgpa <= 79:
        print("A")
    elif cgpa >= 70 and cgpa <= 74:
        print("A-")
    elif cgpa >= 65 and cgpa <= 69:
        print("B+")
    elif cgpa >= 60 and cgpa <= 64:
        print("B")
    elif cgpa >= 55 and cgpa <= 59:
        print("B-")
    elif cgpa >= 50 and cgpa <= 54:
        print("C+")
    elif cgpa >= 45 and cgpa <= 49:
        print("C")
    elif cgpa >= 40 and cgpa <= 44:
        print("D")
    elif cgpa >= 00 and cgpa <= 39:
        print("F")

else:
    print("System Error")

