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


# Assigning Variable and Getting user's input for each questions
name = input("Enter your name: ")
birthday = input("When is your birthday? ")
dream_job = input("What is your dream job? ")
school_attending = input("Which school are you currently attending? ")

# Printing the ASCII art for the user's data with specified color and width
print_ascii_art(name, color=Fore.CYAN, width=200, delay=0.0001)
print_ascii_art(birthday, color=Fore.MAGENTA, width=200, delay=0.0001)
print_ascii_art(dream_job, color=Fore.GREEN, width=240, delay=0.0001)
print_ascii_art(school_attending, color=Fore.LIGHTMAGENTA_EX, width=240, delay=0.0001)
