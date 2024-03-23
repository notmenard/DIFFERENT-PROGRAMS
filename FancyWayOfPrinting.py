# Importing different libraries for different functions to be used in this program
import pyfiglet
import time
from colorama import Fore

# Defining function to print text with animation effect
def print_with_animation(text, color=Fore.WHITE, delay=0.03):
    for char in text:
        print (color + char, end='', flush=True)
        time.sleep(delay) # Adding Delay
    print()

# Defining function to print ASCII art with animation effect
# Taking user's input for the name and their dream job
# Printing the ASCII art for the user's name with specified color and width
# Printing the ASCII art for the user's dream job with specified color and width
