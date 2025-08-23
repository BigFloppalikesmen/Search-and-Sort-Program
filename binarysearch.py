#BINARY SEARCH
import os
from colorama import Fore, Style, init
init(autoreset=True)
#Imports required for it to work. 
    # import program_to_capitalize_a_file
    # import bubblesortprogram
    # import program_to_lowercase_a_file
    # import time


# To run binary search use the mainprogram.py file instead do not run here
def ensure_folder(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

def get_path_in_folder(folder, filename):
    return os.path.join(folder, filename)

def binarySearch(filename, target):
    try:
        with open(filename, "r") as file:
            items = file.read().splitlines()
        lowerPos = 0
        upperPos = len(items) - 1
        found = False
        while lowerPos <= upperPos and not found:
            mid = (lowerPos + upperPos) // 2
            if items[mid] == target:
                found = True
                print(Fore.GREEN + f"{target} was found.")
            elif target < items[mid]:
                upperPos = mid - 1
            else:
                lowerPos = mid + 1
        if not found:
            print(Fore.RED + f"{target} was NOT found in the list.")
        return found
    except FileNotFoundError:
        print(Fore.RED + f"{filename} was not found")
        print(Style.RESET_ALL)
        return False



# How it WOULD work
    # print("Welcome to Binary Search Program!")
    # file = input("What is the wordlist document?: ").strip()
    # target = input("What item are you searching for?: ").strip().lower()

    # # Folder for lowercased files
    # lowercase_folder = "lowercased_files"
    # ensure_folder(lowercase_folder)

    # print("Lowercasing your file to continue... (It could be capitalized later!) ")
    # # Always save lowercased file in the folder
    # lowercased_file_name = os.path.basename(file)
    # lowercased_file_path = get_path_in_folder(lowercase_folder, lowercased_file_name)
    # lowercased_file = program_to_lowercase_a_file.lowerCase(file)

    # # If user chose to save to a new file, move it to the folder
    # if lowercased_file != file:
    #     # Move/rename the new file into the folder if not already there
    #     if not os.path.dirname(lowercased_file):
    #         os.replace(lowercased_file, lowercased_file_path)
    #         lowercased_file = lowercased_file_path
    #     else:
    #         # Overwrote original, so copy to folder for consistency
    #         os.replace(file, lowercased_file_path)
    #         lowercased_file = lowercased_file_path

    # print("For Binary Search to take place, the list must be sorted...")
    # sort_or_no = input("Would you like to continue with a bubble sort algorithm?:(y/n) ").lower()
    # if sort_or_no == "y":
    #     try:
    #         with open(lowercased_file, "r") as f:
    #             items = f.read().splitlines()
    #     except FileNotFoundError:
    #         print(f"{lowercased_file} could not be found for sorting.")
    #         items = []
    #     if items:
    #         sorted_data, duration = bubblesortprogram.bubbleSort(items)
    #         print(f"File sorted in {duration:.6f} seconds.")
    #         download_choice = input("Save sorted data? (y/n): ").strip().lower()
    #         if download_choice == "y":
    #             sorted_folder = "sorted_files"
    #             ensure_folder(sorted_folder)
    #             file_choice = input("Save to a new file? (y = new file / n = overwrite original): ").strip().lower()
    #             if file_choice == "y":
    #                 new_filename = "sorted_" + os.path.basename(lowercased_file)
    #                 new_filepath = get_path_in_folder(sorted_folder, new_filename)
    #                 bubblesortprogram.writeFile(new_filepath, sorted_data)
    #                 print(f"Sorted file saved as '{new_filepath}'")
    #                 time.sleep(1)
    #                 print("Done with bubble sort")
    #                 time.sleep(1)
    #                 print("Performing Binary Search on Sorted file")
    #                 binarySearch(new_filepath, target)
    #                 time.sleep(1)
    #             elif file_choice == "n":
    #                 bubblesortprogram.writeFile(lowercased_file, sorted_data)
    #                 print("Original file overwritten with sorted data.")
    #                 time.sleep(1)
    #                 print("Done with bubble sort")
    #                 time.sleep(1)
    #                 print("Performing Binary Search on Sorted file")
    #                 binarySearch(lowercased_file, target)
    #             else:
    #                 print("Invalid choice. No file saved.")
    #         else:
    #             print("Sorted data not saved.")
    #     else:
    #         print(f"{lowercased_file} could not be sorted")


