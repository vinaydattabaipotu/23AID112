grades = [85, 92, 78, 65, 88, 91, 73, 89, 55, 94]

A = B = C = below_70 = 0

for grade in grades:
    if grade >= 90:
        A += 1
    elif grade >= 80:
        B += 1
    elif grade >= 70:
        C += 1
    else:
        below_70 += 1

print("Students with A (≥90):", A)
print("Students with B (80–89):", B)
print("Students with C (70–79):", C)
print("Students below 70:", below_70)
