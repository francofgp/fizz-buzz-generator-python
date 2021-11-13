import time
from art import text2art
from rich.console import Console
from rich.prompt import Prompt
from rich.theme import Theme

TITLE = """
# Welcome to
# the Fizz Buzz Generator

"""
colors = {
    "yellow": "#ffd319",
    "orange": "#ff901f",
    "red": "#ff2975",
    "purple": "#f222ff",
    "blue": "#8c1eff"
}
custom_theme = Theme({
    "number": f"bold {colors['purple']}",
    "Fizz": f"bold {colors['red']}",
    "Buzz": f"bold {colors['orange']}",
    "FizzBuzz": f"bold {colors['yellow']}",
    "normal": f"bold {colors['blue']}",

})

console = Console(theme=custom_theme)


def print_fizz_buzz(text_to_print: str):
    """It prints what you want, if the text_to_print argument is "Fizz", "Buzz","FizzBuzz",
    or whatever, it will print with an unique style for each

    Args:
        text_to_print (str): what you want to print
    """
    font = {
        "Fizz": "clr7x8",
        "Buzz": "clr7x8",
        "FizzBuzz": "coil_cop",
        "number": "clr6x6",
    }
    if text_to_print == "FizzBuzz":
        console.print(text2art(text=text_to_print,
                      font=font[text_to_print]), style=text_to_print)
        return
    elif text_to_print == "Fizz":
        console.print(text2art(text=text_to_print,
                      font=font[text_to_print]), style=text_to_print)
        return
    elif text_to_print == "Buzz":
        console.print(text2art(text=text_to_print,
                      font=font[text_to_print]), style=text_to_print)
        return
    else:
        console.print(text2art(text=text_to_print,
                      font=font["number"]), style="number")
        return


def fizzBuzz(num: int) -> str:
    """It returns Fizz, Buzz, FizzBuzz or the number that you passed
    if is divisible by 3, 5, 3 or 5, or the number if it is none of the later

    Args:
        num (int): The number that you want to use for the FizzBuzz algorith

    Returns:
        str: Fizz, Buzz, FizzBuzz or the number that you passed as a string
        if is divisible by 3, 5, 3 or 5, respectively
    """
    return "Fizz"*(num % 3 == 0) + "Buzz"*(num % 5 == 0) or str(num)


def title_printer(*args):
    """Print the arguments that you pass
    """
    TITLE_FONT = "standard"
    for arg in args:
        console.print(text2art(text=arg,
                               font=TITLE_FONT), style="normal")


def execute_fizz_buzz():
    number = "not a number"
    while True:
        number = Prompt.ask(
            "From 1 to what number you want to generate the Fizz Buzz:", default="100")
        if number.isdigit():
            break
        else:
            console.print("That's not a number", style=f"bold {colors['red']}")
    number = int(number)

    for i in range(1, number+1):
        print_fizz_buzz(fizzBuzz(i))
        time.sleep(0.2)


def run_fizz_buzz():
    title_printer("Welcome to the", "Fizz Buzz", "Generator")
    execute_fizz_buzz()
    title_printer("That's", "all", "Folks")
    pass


if __name__ == '__main__':
    run_fizz_buzz()
