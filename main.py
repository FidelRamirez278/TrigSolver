import math

# Law of Sines to calculate a side length
def law_of_sines_side(a, A, B):
    return (a * math.sin(math.radians(B))) / math.sin(math.radians(A))

# Law of Sines to calculate an angle in degrees
def law_of_sines_angle(A, a, b):
    return math.degrees(math.asin((b * math.sin(math.radians(A))) / a))

# Law of Cosines to calculate a side length
def law_of_cosines_side(a, b, C):
    return math.sqrt(a**2 + b**2 - 2*a*b*math.cos(math.radians(C)))

# Law of Cosines to calculate an angle in degrees
def law_of_cosines_angle(a, b, c):
    return math.degrees(math.acos((b**2 + c**2 - a**2) / (2*b*c)))

# SSS case to solve a triangle
def sss_case(a, b, c):
    A = law_of_cosines_angle(a, b, c)
    B = law_of_cosines_angle(b, a, c)
    C = 180 - A - B
    return A, B, C, a, b, c

# SAS case to solve a triangle
def sas_case(a, b, C):
    c = law_of_cosines_side(a, b, C)
    A = law_of_cosines_angle(a, b, c)
    B = 180 - A - C
    return A, B, C, a, b, c

# ASA case to solve a triangle
def asa_case(A, B, c):
    C = 180 - A - B
    a = law_of_sines_side(c, C, A)
    b = law_of_sines_side(c, C, B)
    return A, B, C, a, b, c

# AAS case to solve a triangle
def aas_case(A, B, a):
    C = 180 - A - B
    b = law_of_sines_side(a, A, B)
    c = law_of_sines_side(a, A, C)
    return A, B, C, a, b, c

# SSA case to solve a triangle
def ssa_case(A, a, c):
    C = law_of_sines_angle(A, a, c)
    B = 180 - A - C
    b = law_of_sines_side(a, A, B)
    return A, B, C, a, b, c

# Area of an oblique triangle
def triangle_area(triangle_info):
    a, b, c = triangle_info[-3:]
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

# Collects and calculates triangle information based on the specified triangular case
def collect_triangle_info(triangle_type):
    if triangle_type not in ["sss", "sas", "asa", "aas", "ssa"]:
        print(f"Invalid triangle type: {triangle_type}")
        return

    input_prompts = {
        "sss": ("Enter the length of side a: ", "Enter the length of side b: ", "Enter the length of side c: "),
        "sas": ("Enter the length of side a: ", "Enter the length of side b: ", "Enter the measure of angle C: "),
        "asa": ("Enter the measure of angle A: ", "Enter the measure of angle B: ", "Enter the length of side c: "),
        "aas": ("Enter the measure of angle A: ", "Enter the measure of angle B: ", "Enter the length of side a: "),
        "ssa": ("Enter the measure of angle A: ", "Enter the length of side a: ", "Enter the length of side c: ")
    }

    # Get input values
    inputs = []
    for prompt in input_prompts[triangle_type]:
        value = float(input(prompt))
        inputs.append(value)

    # Calculate triangle information
    if triangle_type == "sss":
        A, B, C, a, b, c = sss_case(*inputs)
        triangle_info = sss_case(*inputs)
    elif triangle_type == "sas":
        A, B, C, a, b, c = sas_case(*inputs)
        triangle_info = sas_case(*inputs)
    elif triangle_type == "asa":
        A, B, C, a, b, c = asa_case(*inputs)
        triangle_info = asa_case(*inputs)
    elif triangle_type == "aas":
        A, B, C, a, b, c = aas_case(*inputs)
        triangle_info = aas_case(*inputs)
    elif triangle_type == "ssa":
        triangle_info = ssa_case(*inputs)
        A, B, C, a, b, c = triangle_info

    # Print triangle information and area
    print(f"\nThe triangle has the following side-lengths:\na = {a} \nb = {b} \nc = {c}")
    print(f"\nThe triangle has the following angle measurement:\nA = {A} \nB = {B} \nC = {C}")
    print(f"\nThe area of the triangle is {triangle_area([A, B, C, a, b, c])} units squared.")

print("Welcome to TrigSolver!")
triangle_type = input("Enter your triangular case (sss, sas, asa, aas, ssa): ")

# Call collect_triangle_info() with the user input as the argument
triangle_info = collect_triangle_info(triangle_type)
