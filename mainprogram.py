import linearsearch
import bubblesortprogram
import program_to_lowercase_a_file
import program_to_capitalize_a_file
import binarysearch
import time
import os

print("Welcome to the Search & Sort algorithms multi tool!")
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
    file = input("What is the wordlist document?: ").strip()
    key = input("What item are you searching for?: ").strip()
    linearsearch.linearSearch(file, key)

elif choice == "2": #Binary search
    print("Welcome to Binary Search Program!")
    file = input("What is the wordlist document?: ").strip()
    target = input("What item are you searching for?: ").strip().lower()

    # Folder for lowercased files
    lowercase_folder = "lowercased_files"
    binarysearch.ensure_folder(lowercase_folder)

    print("Lowercasing your file to continue... (It could be capitalized later!) ")
    # Always save lowercased file in the folder
    lowercased_file = program_to_lowercase_a_file.lowerCase(file, output_folder=lowercase_folder)

    if lowercased_file is None:
        print("No lowercased file to continue with.")
    else:
        print("For Binary Search to take place, the list must be sorted...")
        sort_or_no = input("Would you like to continue with a bubble sort algorithm?:(y/n) ").lower()
        if sort_or_no == "y":
            try:
                with open(lowercased_file, "r") as f:
                    items = f.read().splitlines()
            except FileNotFoundError:
                print(f"{lowercased_file} could not be found for sorting.")
                items = []
            if items:
                sorted_data, duration = bubblesortprogram.bubbleSort(items)
                print(f"File sorted in {duration:.6f} seconds.")
                download_choice = input("Save sorted data? (y/n): ").strip().lower()
                if download_choice == "y":
                    sorted_folder = "sorted_files"
                    binarysearch.ensure_folder(sorted_folder)
                    file_choice = input("Save to a new file? (y = new file / n = overwrite original): ").strip().lower()
                    if file_choice == "y":
                        new_filename = "sorted_" + os.path.basename(lowercased_file)
                        new_filepath = binarysearch.get_path_in_folder(sorted_folder, new_filename)
                        bubblesortprogram.writeFile(new_filepath, sorted_data)
                        print(f"Sorted file saved as '{new_filepath}'")
                        time.sleep(1)
                        print("Done with bubble sort")
                        time.sleep(1)
                        print("Performing Binary Search on Sorted file")
                        binarysearch.binarySearch(new_filepath, target)
                        time.sleep(1)
                    elif file_choice == "n":
                        bubblesortprogram.writeFile(lowercased_file, sorted_data)
                        print("Original file overwritten with sorted data.")
                        time.sleep(1)
                        print("Done with bubble sort")
                        time.sleep(1)
                        print("Performing Binary Search on Sorted file")
                        binarysearch.binarySearch(lowercased_file, target)
                    else:
                        print("Invalid choice. No file saved.")
                else:
                    print("Sorted data not saved.")
            else:
                print(f"{lowercased_file} could not be sorted")
        else:
            print("Skipping sorting. Performing Binary Search on lowercased file.")
            binarysearch.binarySearch(lowercased_file, target)

elif choice == "3": #Bubble Sort
    print("Welcome to Bubble Sort Program!")
    file = input("Enter the filename to sort: ").strip()
    data = bubblesortprogram.readFile(file)
    if data:
        sorted_data, duration = bubblesortprogram.bubbleSort(data)
        print(f"File sorted in {duration:.6f} seconds.")
        download_choice = input("Save sorted data? (y/n): ").strip().lower()
        if download_choice == "y":
            sorted_folder = "sorted_files"
            binarysearch.ensure_folder(sorted_folder)
            file_choice = input("Save to a new file? (y = new file / n = overwrite original): ").strip().lower()
            if file_choice == "y":
                new_filename = "sorted_" + os.path.basename(file)
                new_filepath = binarysearch.get_path_in_folder(sorted_folder, new_filename)
                bubblesortprogram.writeFile(new_filepath, sorted_data)
                print(f"Sorted file saved as '{new_filepath}'")
            elif file_choice == "n":
                bubblesortprogram.writeFile(file, sorted_data)
                print("Original file overwritten with sorted data.")
            else:
                print("Invalid choice. No file saved.")
        else:
            print("Sorted data not saved.")
    else:
        print(f"{file} could not be sorted")