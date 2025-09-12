# LESSON 4 STARTER CODE: VARIABLES AND DATA TYPES

# ========================================
# PART 1: Creating Variables Practice
# ========================================
name = "Jenna"
age = 15
gpa = 3.7
grade = 10

print("Student Name: " + name)
# print("Student Age:" + age) str+int wont work
print("Student Age:", + age) 

# variables can change
age = 17
# multiple assignment
subject, period = "CS100", 1

# ========================================
# PART 2: Data Types Practice
# ========================================
# four main (primitive) data types
name = "Jenna" # str(string)
age = 15       # int(integer)
gpa = 3.7      # float(decimal)
is_present = True #bool(Boolean)

#check data types via type() function
print(f"Name:{name} Type:{type(name)}")
print(f"Age:{age} Type:{type(age)}")
print(f"GPA:{gpa} Type:{type(gpa)}")
print(f"Present:{is_present} Type:{type(is_present)}")

# ========================================
# PART 3: Type Conversion Practice
# ========================================
#convert between types
grade_text = "95"
#grade_text2 = '"95"'
print(f"Original:{grade_text} {type(grade_text)}")
grade_number = int(grade_text)
print(f"As number: {grade_number} {type(grade_number)}")

gpa_number = float(gpa)
print(f"GPA: {gpa_number} {type(gpa_number)}")
gpa_text = str(gpa_number)

#pratice with bool() function
print(f"bool(0) - {bool(0)}") #false, doesnt have a value
print(f"bool(1) - {bool(1)}") #true
print(f"bool(10) - {bool(10)}") #true
print(f"bool('') - {bool('')}") #true
print(f"bool('hi') - {bool('hi')}") #true


# ========================================
# PART 4: Variable Operations Practice  
# ========================================
#swapping variables
color1 = "red"
color2 = "blue"
color1, color2 = color2, color1
print(f"Color2: {color2}")




