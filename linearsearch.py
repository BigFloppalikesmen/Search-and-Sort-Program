# LINEAR SEARCH PROGRAM

import time
from pynput import keyboard

start_input = False         # flag to start search outside listener

def on_press(key):
    global start_input        # Global Variable
    try:
        if key.char == 'a':     # Listener for key a 
            start_input = True
            return False         # Stop the listener
    except AttributeError:
        pass

def linearSearch(filename, target): # MAIN PROGRAM
    try:
        with open(filename, "r") as file: # Opens file for searching
            items = file.read().splitlines()  # Takes line by line of contents inside file

            start = time.time()     # Starts a timer for {duration}
            for index, item in enumerate(items):    # enumerate allows to display both value and index
                if item.strip().lower() == target.lower():
                    end = time.time()                   #ends timer
                    print(f"{target} was found at index {index+1} in {end - start:.6f} seconds")
                    return
            end = time.time()
            print(f"{target} was not found in the document in {end - start:.6f} seconds")
    except FileNotFoundError:                       # Incase the filename is invalid
        print(f"{filename} document not found")

print("Welcome to Linear Search Program!")
print("Press 'a' to start...")

# 🔁 Wait for 'a' to be pressed, then stops immediately 
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

# 🛑 Keyboard listener is now fully stopped = Reduces lag when typing
if start_input:
    time.sleep(0.1)  # optional, just to be safe
    file = input("What is the wordlist document?: ")
    target = input("What item are you searching for?: ")
    linearSearch(file, target)

#End lol