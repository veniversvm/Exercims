
COMMANDS_TUPLE = ("Reverse", "jump", "close your eyes", "double blink", "wink")

def commands(binary_str) -> list:
    """
        This solution uses a functional approach; no variables were modified during execution.;-)

        Args: 
            binary_str:  compose of characters '1' and '0'.

        Returns:
            Tuple of strings with the commands. 
    """
    commands_list = [ COMMANDS_TUPLE[index + 1]  for index, bit in enumerate(binary_str[1:]) if bit == "1"]
    # The list is alredy inverted
    return commands_list[::-1] if binary_str[0] == "0" else commands_list
