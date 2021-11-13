import time
from art import text2art
from rich.console import Console
from rich.prompt import Prompt
from rich.theme import Theme
from rich.markdown import Markdown

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


def fizzBuzz(num: int):

    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    if num % 3 == 0:
        return "Fizz"
    if num % 5 == 0:
        return "Buzz"
    return str(num)


def show_title():
    TITLE_FONT = "standard"
    console.print(text2art(text="Welcome  to  the",
                           font=TITLE_FONT), style="normal")
    console.print(text2art(text="Fizz  Buzz",
                  font=TITLE_FONT), style="FizzBuzz")
    console.print(text2art(text="Generator", font=TITLE_FONT), style="normal")


def good_bye():
    TITLE_FONT = "standard"
    console.print(text2art(text="That's",
                           font=TITLE_FONT), style="normal")
    console.print(text2art(text="Folks",
                  font=TITLE_FONT), style="FizzBuzz")


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
    show_title()
    execute_fizz_buzz()
    good_bye()
    pass


if __name__ == '__main__':
    run_fizz_buzz()
