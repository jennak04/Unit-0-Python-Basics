# LESSON 5: USER INPUT & PROCESSING
print("LESSON 5: USER INPUT & PROCESSING (Advanced Track)")
print("=" * 50)

# PART 1: Input Comparison (JS vs Python)
print("\n--- PART 1: Input Comparison ---")
# Compare to JS: let name = prompt("Name:");
#name = input("Name:")
#print(f"Hello, {name}")

# Compare to JS: let age = parseInt(prompt("Age:"));
#age = int(input("Age:"))
#print(f"You are {age} years old")

# PART 2: Type Conversion - Python Style  
#print("\n--- PART 2: Type Conversion ---")
# Like JS parseInt(), parseFloat() but Python syntax
#num_str = "42"
#num_int = int(num_str)
#num_float = int(num_str)

#print(f"You are {int(num_str)} years old")

# Try the bool() function - different from JS truthy/falsy
#print(f"bool(''): {bool('')}") #false
#print(f"bool('0'): {bool('0')}") #false
#print(f"bool('-10'): {bool('-10')}") #true
#print(f"bool(' '): {bool(' ')}") #true (space is a charatcer)

# PART 3: Math Operators (Focus on differences from JS)
print("\n--- PART 3: Math Operators ---")
# Test regular division / (always returns float in Python)
print(f"6 / 2 = {6/2} (type: {type(6/2)})") #Yields to a float

# Test floor division // (doesn't exist in JS)


# Test with same numbers - see the difference


# PART 4: Complex Expressions & Precedence
print("\n--- PART 4: Complex Expressions ---")
# Test: 9 + 6 / 3 * 2 - 1 (same rules as JS?)
result = 9 + 6 / 3 * 2 - 1
print(f"9 + 6 / 3 * 2 - 1 = {result}")
print("Step by step comparison")
print("9 + 6 / 3 * 2 - 1") #division first
print("9 + 2.0 * 2 - 1")  #multiplication
print("9 + 4.0 - 1") #addition
print("13.0 - 1") #subtraction

# Test: 6 / 2 (what type is the result?)


#code along
print("CODE ALONG")
user_name = input("Name: ")
user_number = input("Favorite number: ")
number_int = int(user_number)
doubled = {number_int} * 2


print(f"{user_name}'s favorite number * 2 is {doubled}")