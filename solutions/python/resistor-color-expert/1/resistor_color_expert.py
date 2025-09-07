from functools import reduce

"""
    This implementation follows a functional programming approach. Functional
    programming is a paradigm that treats computation as the evaluation of
    mathematical functions and avoids changing state or mutable data. In this
    function, variables are assigned once and never modified, and the higher-order
    function `reduce` is used to transform the input list into a value without
    side effects.
"""


RESISTORS = ("black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white")
TOLERANCE = {
    "grey": 0.05,
    "violet": 0.1,
    "blue": 0.25,
    "green": 0.5,
    "brown": 1,
    "red": 2,
    "gold": 5,
    "silver": 10,
}

def get_final_value(resistor_total_value: int) -> tuple[str, int| float]:
    """Converts a numerical resistance value into a more readable metric format.
    """
    if resistor_total_value >= 1_000_000_000:
        return "giga", resistor_total_value / 1_000_000_000
    if resistor_total_value >= 1_000_000:
        return "mega", resistor_total_value / 1_000_000
    if resistor_total_value >= 1_000:
        return "kilo", resistor_total_value / 1_000
    
    return "", resistor_total_value


def resistor_label(colors) -> str:
    """
        Calculates a resistor's value and generates a formatted label from its color bands.
    """
    # For resistors with fewer than 3 bands, a simple direct value is assumed.
    if len(colors) < 3:
        return f"{RESISTORS.index(colors[0])} ohms"

    # The last band always indicates the tolerance.
    tolerance = TOLERANCE[colors[-1]]
    # The second-to-last band corresponds to the multiplier.
    multiplier = RESISTORS.index(colors[-2])

    # The remaining bands (all except the last two) are the significant digits.
    # Their numerical values are concatenated to form the base resistance number.
    significant_digits = reduce(lambda acc, x: acc + str(RESISTORS.index(x)), colors[:-2], "")
    
    # Calculate the total value in ohms by multiplying the digits by 10^multiplier.
    resistor_total_value = int(significant_digits) * (10 ** multiplier)

    # Get the scaled value and its corresponding metric prefix.
    metric, value = get_final_value(resistor_total_value)
    
    # Format the final value, ensuring that unnecessary decimals are not shown (e.g., "10" instead of "10.0").
    formatted_value = int(value) if value % 1 == 0 else value
    
    return f"{formatted_value} {metric}ohms ±{tolerance}%"