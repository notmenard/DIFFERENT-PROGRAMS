# Importing different libraries for different functions to be used in this program
import pyfiglet
import time
from colorama import Fore

# Defining function to print text with animation effect
def print_with_animation(text, color=Fore.WHITE, delay=0.03):
    for char in text:
        print(color + char, end='', flush=True)
        time.sleep(delay)  # Adding Delay
    print()

# Defining function to print ASCII art with animation effect
def print_ascii_art(text, font='isometric1', color=Fore.YELLOW, width=150, delay=0.001):
    ascii_art = pyfiglet.figlet_format(text,font=font, width=width)
    for line in ascii_art.split('\n'):
        print_with_animation(line,color,delay)

# Taking user's input for the name and their dream job
# Printing the ASCII art for the user's name with specified color and width
# Printing the ASCII art for the user's dream job with specified color and width
