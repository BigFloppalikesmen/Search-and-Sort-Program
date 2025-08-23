from ast import For
from colorama import Fore, Style, init
init(autoreset=True)
import linearsearch
import bubblesortprogram
import program_to_lowercase_a_file
import program_to_capitalize_a_file
import binarysearch
import time
import os
import mergesort

print(Fore.YELLOW + "Welcome to the Search & Sort algorithms multi tool!")
choice = input(
'''
1. Linear Search
2. Binary Search
3. Bubble Sort
4. Merge Sort (Work in progress...) 

(Enter 1-4)
''').lower()

if choice == "1": #Linear search
    print("Proceeding to Linear Search...")
    time.sleep(1)
    print("Welcome to Linear Search Program!")
    time.sleep(0.1)
    file = input(Fore.CYAN + "What is the wordlist document?: ").strip()
    key = input(Fore.CYAN + "What item are you searching for?: ").strip()
    linearsearch.linearSearch(file, key)

elif choice == "2": #Binary search
    print("Welcome to Binary Search Program!")
    file = input(Fore.CYAN + "What is the wordlist document?: ").strip()
    target = input(Fore.CYAN + "What item are you searching for?: ").strip().lower()

    # Folder for normalized files
    normalized_folder = "normalized_files"
    binarysearch.ensure_folder(normalized_folder)

    print("Lowercasing your file to continue... (It could be capitalized later!) ")
    # Always save lowercased file in the folder
    lowercased_file = program_to_lowercase_a_file.lowerCase(file, output_folder=normalized_folder)

    if lowercased_file is None:
        print("No lowercased file to continue with.")
    else:
        print("For Binary Search to take place, the list must be sorted...")
        sort_or_no = input(Fore.CYAN + "Would you like to continue with a Merge sort algorithm?:(y/n) ").lower()
        if sort_or_no == "y":
            try:
                with open(lowercased_file, "r") as f:
                    items = f.read().splitlines()
            except FileNotFoundError:
                print(Fore.RED + f"{lowercased_file} could not be found for sorting.")
                items = []
            if items:
                start = time.time()
                sorted_data = mergesort.mergeSort(items)
                end = time.time()
                duration = end - start
                print(Fore.GREEN + f"File sorted in {duration:.6f} seconds.")
                download_choice = input(Fore.CYAN + "Save sorted data? (y/n): ").strip().lower()
                if download_choice == "y":
                    sorted_folder = "sorted_files"
                    binarysearch.ensure_folder(sorted_folder)
                    file_choice = input(Fore.CYAN + "Save to a new file? (y = new file / n = overwrite original): ").strip().lower()
                    if file_choice == "y":
                        new_filename = "sorted_" + os.path.basename(lowercased_file)
                        new_filepath = binarysearch.get_path_in_folder(sorted_folder, new_filename)
                        bubblesortprogram.writeFile(new_filepath, sorted_data)
                        print(Fore.GREEN + f"Sorted file saved as '{new_filepath}'")
                        time.sleep(1)
                        print(Fore.GREEN + "Done with bubble sort")
                        time.sleep(1)
                        print("Performing Binary Search on Sorted file")
                        result = binarysearch.binarySearch(new_filepath, target)
                        time.sleep(1)
                        # Option to capitalize after search
                        capitalize_choice = input(Fore.CYAN + "Would you like to capitalize the file? (y/n): ").strip().lower()
                        if capitalize_choice == "y":
                            program_to_capitalize_a_file.capitalize(new_filepath)
                    elif file_choice == "n":
                        bubblesortprogram.writeFile(lowercased_file, sorted_data)
                        print(Fore.GREEN + "Original file overwritten with sorted data.")
                        time.sleep(1)
                        print(Fore.GREEN + "Done with bubble sort")
                        time.sleep(1)
                        print(Fore.GREEN + "Performing Binary Search on Sorted file")
                        result = binarysearch.binarySearch(lowercased_file, target)
                        time.sleep(1)
                        capitalize_choice = input(Fore.CYAN + "Would you like to capitalize the file? (y/n): ").strip().lower()
                        if capitalize_choice == "y":
                            program_to_capitalize_a_file.capitalize(lowercased_file)
                    else:
                        print(Fore.RED + "Invalid choice. No file saved.")
                else:
                    print("Sorted data not saved.")
            else:
                print(Fore.RED + f"{lowercased_file} could not be sorted")
        else:
            print("Skipping sorting. Performing Binary Search on lowercased file.")
            result = binarysearch.binarySearch(lowercased_file, target)
            time.sleep(1)
            capitalize_choice = input(Fore.CYAN + "Would you like to capitalize the file? (y/n): ").strip().lower()
            if capitalize_choice == "y":
                program_to_capitalize_a_file.capitalizeFile(lowercased_file)

elif choice == "3": #Bubble Sort
    print("Welcome to Bubble Sort Program!")
    file = input(Fore.CYAN + "Enter the filename to sort: ").strip()
    data = bubblesortprogram.readFile(file)
    if data:
        sorted_data, duration = bubblesortprogram.bubbleSort(data)
        print(Fore.GREEN + f"File sorted in {duration:.6f} seconds.")
        download_choice = input(Fore.CYAN + "Save sorted data? (y/n): ").strip().lower()
        if download_choice == "y":
            sorted_folder = "sorted_files"
            binarysearch.ensure_folder(sorted_folder)
            file_choice = input(Fore.CYAN + "Save to a new file? (y = new file / n = overwrite original): ").strip().lower()
            if file_choice == "y":
                new_filename = "sorted_" + os.path.basename(file)
                new_filepath = binarysearch.get_path_in_folder(sorted_folder, new_filename)
                bubblesortprogram.writeFile(new_filepath, sorted_data)
                print(Fore.GREEN + f"Sorted file saved as '{new_filepath}'")
            elif file_choice == "n":
                bubblesortprogram.writeFile(file, sorted_data)
                print(Fore.GREEN + "Original file overwritten with sorted data.")
            else:
                print(Fore.RED + "Invalid choice. No file saved.")
        else:
            print(Fore.RED + "Sorted data not saved.")
    else:
        print(Fore.RED + f"{file} could not be sorted")