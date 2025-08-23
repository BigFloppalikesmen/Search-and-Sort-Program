# LINEAR SEARCH PROGRAM
from colorama import Fore, Style, init
init(autoreset=True)

import time

def linearSearch(filename, target): # MAIN PROGRAM
    try:
        with open(filename, "r") as file: # Opens file for searching
            items = file.read().splitlines()  # Takes line by line of contents inside file

            start = time.time()     # Starts a timer for {duration}
            for index, item in enumerate(items):    # enumerate allows to display both value and index
                if item.strip().lower() == target.lower():
                    end = time.time()                   #ends timer
                    print(Fore.GREEN + f"{target} was found at position {index+1} in {end - start:.6f} seconds")
                    return
            end = time.time()
            print(Fore.RED + f"{target} was not found in the document in {end - start:.6f} seconds")
    except FileNotFoundError:                       # Incase the filename is invalid
        print(Fore.RED + f"{filename} document not found")

#End lol