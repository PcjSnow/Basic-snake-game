colors = {"red": "\033[31m", "blue": "\033[34m", "cyan": "\033[36m",
 "yellow": "\033[33m", "green": "\033[32m"}
styles = {"bold": "\033[1m", "underline": "\033[4m"}


def styled_print(style: str, color: str):
    print(style + color, end="")

def reset_colors():
    reset = "\033[0m"
    print(reset, end="")
    
