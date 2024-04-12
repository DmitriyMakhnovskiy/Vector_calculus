#
# Sum and difference of two vectors u1 and u2
#
# Dr. Dmitriy Makhnovskiy, City College Plymouth, England
# 12.04.2024
#

import math
import matplotlib.pyplot as plt

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


def draw_vector_with_arguments(vector, magnitude, angle_degrees, title='', color='blue'):
    x, y = vector

    # Set the axis limits to be proportional to the magnitude of the vector
    max_limit = magnitude * 1.1  # Adding some padding
    plt.figure()
    ax = plt.gca()
    ax.set_xlim([-max_limit, max_limit])
    ax.set_ylim([-max_limit, max_limit])
    ax.set_aspect('equal')
    ax.axhline(0, color='black', linewidth=0.5, zorder=0)
    ax.axvline(0, color='black', linewidth=0.5, zorder=0)
    plt.grid(True, zorder=0)

    ax.quiver(0, 0, x, y, angles='xy', scale_units='xy', scale=1, color=color, zorder=1)

    table_data = [
        ["Magnitude", f'{magnitude:.2f}'],
        ["Angle (°)", f'{angle_degrees:.2f}']
    ]

    # Determine the position of the table
    if x >= 0 and y >= 0:
        table_loc = 'lower right'
    elif x < 0 and y >= 0:
        table_loc = 'lower left'
    elif x < 0 and y < 0:
        table_loc = 'upper left'
    else:
        table_loc = 'upper right'

    table = ax.table(cellText=table_data, loc=table_loc, cellLoc='center', edges='closed', zorder=2)
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.auto_set_column_width([0, 1])
    for key, cell in table._cells.items():
        cell.set_facecolor('white')
        cell.set_alpha(1)

    plt.title(title)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()

print('')
# u1 + u2
vector, magnitude, angle_rad, angle_deg = vector_sum(u1, u2)
print("u1 + u2:", vector)
print("|u1 + u2|:", magnitude)
print("arg(u1 + u2):", angle_rad, ' rad')
print("arg(u1 + u2):", angle_deg, ' deg')
draw_vector_with_arguments(vector, magnitude, angle_deg, title='u1 + u2', color='blue')

# u1 - u2
vector, magnitude, angle_rad, angle_deg = vector_difference(u1, u2)
print("\nu1 - u2:", vector)
print("|u1 - u2|:", magnitude)
print("arg(u1 - u2):", angle_rad, ' rad')
print("arg(u1 - u2):", angle_deg, ' deg')
draw_vector_with_arguments(vector, magnitude, angle_deg, title='u1 - u2', color='blue')

# u2 - u1
vector, magnitude, angle_rad, angle_deg = vector_difference(u2, u1)
print("\nu2 - u1:", vector)
print("|u2 - u1|:", magnitude)
print("arg(u2 - u1):", angle_rad, ' rad')
print("arg(u2 - u1):", angle_deg, ' deg')
draw_vector_with_arguments(vector, magnitude, angle_deg, title='u2 - u1', color='blue')