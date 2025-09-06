RESISTORS_VALUES = {
    "black":  "0",
    "brown":  "1",
    "red":    "2",
    "orange": "3",
    "yellow": "4",
    "green":  "5",
    "blue":   "6",
    "violet": "7",
    "grey":   "8",
    "white":  "9",
}

def simplify_value(value: int) -> str:
    while value % 1000 == 0 :
        value = value / 1000
    return str(int(value))
            
    

def label(colors):
    value_colors = RESISTORS_VALUES[colors[0]] +RESISTORS_VALUES[colors[1]]
    value_colors_int = int(value_colors) * (10 ** int(RESISTORS_VALUES[colors[2]]))
    # Prevents cero division
    if value_colors_int == 0: return "0 ohms"
    # clean the resistor N° value
    value_simplified = simplify_value(value_colors_int)

    
    if value_colors_int >= 1_000_000_000:
        return value_simplified + " gigaohms"
    if value_colors_int >= 1_000_000:
        return value_simplified + " megaohms"
    if value_colors_int >= 1_000:
        return value_simplified + " kiloohms"
    return value_simplified + " ohms"

