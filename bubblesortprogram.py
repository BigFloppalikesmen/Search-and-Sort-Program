import time
from colorama import Fore, Style, init
init(autoreset=True)

def bubbleSort(arr):
    start = time.time()
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    end = time.time()
    duration = end - start
    return arr, duration

def readFile(filename):
    try:
        with open(filename, "r") as file:
            items = file.read().splitlines()
            return items
    except FileNotFoundError:
        print(Fore.RED + f"Bruh, '{filename}' not found.")
        return None

def writeFile(filename, data):
    with open(filename, "w") as file:
        for item in data:
            file.write(item + "\n")



#How it would work:
    # print("Welcome to Bubble Sort Program!")
    # file = input("Enter the filename to sort: ").strip()

    # data = readFile(file)
    # if data:
    #     sorted_data, duration = bubbleSort(data)
    #     print(f"File sorted in {duration:.6f} seconds.")

    #     download_choice = input("Save sorted data? (y/n): ").strip().lower()
    #     if download_choice == "y":
    #         file_choice = input("Save to a new file? (y = new file / n = overwrite original): ").strip().lower()
    #         if file_choice == "y":
    #             new_filename = "sorted_" + file
    #             writeFile(new_filename, sorted_data)
    #             print(f"Sorted file saved as '{new_filename}'")
    #         elif file_choice == "n":
    #             writeFile(file, sorted_data)
    #             print("Original file overwritten with sorted data.")
    #         else:
    #             print("Invalid choice. No file saved.")
    #     else:
    #         print("Sorted data not saved.")
    # else:
    #     print(f"{file} was not sorted succesfully")