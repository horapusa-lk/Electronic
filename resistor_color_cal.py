
def resistor_color_cal(resistance):
    resistor_colors_1and2 = [
        "Black",
        "Brown",
        "Red",
        "Orange",
        "Yellow",
        "Green",
        "Blue",
        "Purple",
        "Gray",
        "White",
    ]

    resistor_colors_3 = [
        "Black",
        "Brown",
        "Red",
        "Orange",
        "Yellow",
        "Green",
        "Blue",
        "Gold",
        "Silver"
    ]

    resistor_colors_4 = [
        "Brown",
        "Red",
        "Orange",
        "Yellow",
        "Green",
        "Blue",
        "Purple",
        "Gray",
        "Gold",
        "Silver",
        "No Color"
    ]

    resistance_str = str(resistance)

    color_1 = resistor_colors_1and2[int(resistance_str[0])]
    color_2 = resistor_colors_1and2[int(resistance_str[1])]
    color_3 = ""

    if resistance < 100:
        color_3 = resistor_colors_3[0]
    elif resistance < 1000:
        color_3 = resistor_colors_3[1]
    elif resistance < 10000:
        color_3 = resistor_colors_3[2]
    elif resistance < 100000:
        color_3 = resistor_colors_3[3]
    elif resistance < 1000000:
        color_3 = resistor_colors_3[4]
    elif resistance < 10000000:
        color_3 = resistor_colors_3[5]
    elif resistance < 100000000:
        color_3 = resistor_colors_3[6]
    elif resistance < 1000000000:
        color_3 = resistor_colors_3[7]

    return f"{color_1},{color_2},{color_3}"


print(resistor_color_cal(383))