#
# Sum and difference of two vectors u1 and u2
#
# Dr. Dmitriy Makhnovskiy, City College Plymouth, England
# 12.04.2024
#

import math

# Number of decimal places when calculating real values
accuracy = 3

# Vector 1
phase1 = 0.0  # angle in radians (modify if you use degrees)
mag1 = 60  # magnitude
u1 = (mag1 * math.cos(phase1), mag1 * math.sin(phase1))  # vector

# Vector 2
phase2 = math.pi/6  # angle in radians (modify if you use degrees)
mag2 = 85  # magnitude
u2 = (mag2 * math.cos(phase2), mag2 * math.sin(phase2))  # vector

def vector_sum(u1, u2):
    x = round(u1[0] + u2[0], accuracy)
    y = round(u1[1] + u2[1], accuracy)
    magnitude = round(math.sqrt(x**2 + y**2), accuracy)
    angle = math.atan2(y, x)
    angle_rad = round(angle, accuracy)
    angle_deg = round(angle * 180.0 / math.pi, accuracy)
    return (x, y), magnitude, angle_rad, angle_deg

def vector_difference(u1, u2):
    x = round(u1[0] - u2[0], accuracy)
    y = round(u1[1] - u2[1], accuracy)
    magnitude = round(math.sqrt(x**2 + y**2), accuracy)
    angle = math.atan2(y, x)
    angle_rad = round(angle, accuracy)
    angle_deg = round(angle * 180.0 / math.pi, accuracy)
    return (x, y), magnitude, angle_rad, angle_deg

print('')
# u1 + u2
vector, magnitude, angle_rad, angle_deg = vector_sum(u1, u2)
print("u1 + u2:", vector)
print("|u1 + u2|:", magnitude)
print("arg(u1 + u2):", angle_rad, ' rad')
print("arg(u1 + u2):", angle_deg, ' deg')

# u1 - u2
vector, magnitude, angle_rad, angle_deg = vector_difference(u1, u2)
print("\nu1 - u2:", vector)
print("|u1 - u2|:", magnitude)
print("arg(u1 - u2):", angle_rad, ' rad')
print("arg(u1 - u2):", angle_deg, ' deg')

# u2 - u1
vector, magnitude, angle_rad, angle_deg = vector_difference(u2, u1)
print("\nu2 - u1:", vector)
print("|u2 - u1|:", magnitude)
print("arg(u2 - u1):", angle_rad, ' rad')
print("arg(u2 - u1):", angle_deg, ' deg')