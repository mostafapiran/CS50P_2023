import sys
import random
from pyfiglet import Figlet

figlet = Figlet()
temp_argv = ["-f", "--font"]


def main():
    if len(sys.argv) < 2:
        font = random.choice(figlet.getFonts())
        figletize("Input: ", font)
    elif len(sys.argv) > 2 and sys.argv[1] in temp_argv and sys.argv[2] in figlet.getFonts():
        font = sys.argv[2]
        figletize("Input: ", font)
    else:
        sys.exit("Invalid usage")

def figletize(prompt, f):
    txt = input(prompt).strip()
    figlet.setFont(font=f)
    print("Output:")
    print(figlet.renderText(txt))




if __name__ == "__main__":
    main()