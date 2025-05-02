"""
Basic Data Analysis Program
===========================

This program performs basic statistical analysis on numeric data provided by the user,
calculating the mean, median, and mode of the dataset.

Features:
---------
* Automatically checks for and installs required dependencies (statistics module)
* Offers two different input methods:
    1. Whole list - Enter all numbers at once, comma-separated
    2. Single entry - Enter numbers one at a time
* Handles non-numeric inputs gracefully by filtering them out
* Provides clear user prompts and error messages

Usage:
------
1. Run the program
2. Authorize installation of required packages if prompted
3. Select an input mode from the main menu:
   - Option 1: Enter a comma-separated list of numbers
   - Option 2: Enter numbers one at a time, type 'done' when finished
4. Review the calculated statistics (mean, median, mode)
5. Type 'Exit' at the main menu to quit the program

Functions:
----------
- install_and_import(package): Attempts to import a package, installing it if necessary
- analysis(data): Processes the input data and calculates statistics
- filter(raw): Separates valid numerical data from invalid entries
- WholeList(): Handles the whole-list input mode
- Single(): Handles the one-at-a-time input mode
- main_menu(): Displays and manages the main program menu

Dependencies:
------------
- statistics: Python's built-in statistics module (installed automatically if needed)

Returns:
--------
For valid numerical inputs, the program calculates and displays:
- Mean (average)
- Median (middle value)
- Mode (most common value)
- List of any invalid entries that were filtered out

Author:
-------
SlightlyOffset

Version:
--------
1.0
"""

import subprocess
import sys

def main():
    def install_and_import(package):
        """
        Attempts to import a package. If it's not installed, it installs it using pip.
        """
        try:
            __import__(package)
            print(f"\n{package} is already installed.\n")
            return True #indicate successful import
        except ImportError:
            print(f"\n{package} is not installed. Installing...")
            authorization = input(f"\nAuthorize istallation of {package}? (y/N):  ")
            if authorization.strip().lower() == "y":
                try:
                    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
                    print(f"\n{package} installed successfully.")
                    __import__(package) #try import again after install
                    return True #indicate successful import after install
                except subprocess.CalledProcessError as e:
                    print(f"\nError installing {package}: {e}")
                    return False #Indicate install failure
                    
            elif authorization.strip().lower() == "n" or authorization.strip().lower() == "":
                print("\nAborted...\n")
                print(f"Note: The program might not work if the package {package} is not installed.")
                input("Press 'Enter' to continue...")
                return False # Package not installed.    
    
    def analysis(data):
        '''
        Function to perform statistical processes.
        '''
        def filter(raw):
            print("\nFilter called. (Debug)")
            
            valid_data = []
            invalid_data = [] 
            for item in raw:
                try:
                    float(item)
                    valid_data.append(float(item))
                except:
                    invalid_data.append(item)
                
            return valid_data, invalid_data
        
        valid_data, invalid_data = filter(data)
        sorted_data = sorted(valid_data)
        procmean = st.mean(sorted_data)
        procmedian = st.median(sorted_data)
        procmode = st.multimode(sorted_data)
        
        print(f"\nMean: {procmean}")
        print(f"Median: {procmedian}")
        print(f"Mode: {procmode}")
        print(f"Invalid data include: {invalid_data}")
        
        input("\nPress 'Enter' to return to menu...\n")
        return
    
    def WholeList():
        '''
        Function to allow user to enter the list of data.
        Ex:
            1, 2, 3, 4,...,n
            or
            (1, 2, 3, 4,...,n)
        '''
        print("\nWhole List.")
        print("Ex input:")
        print("1, 2, 3, 4,...,n")
        print("or\n(1, 2 3, 4,...,n)")
        
        data = []
        while True:
            data_in = input("\nEnter here(whole): ")
            if not data_in.startswith("(") and not data_in.endswith(")"):
                data = data_in.split(",")
            elif data_in.startswith("(") and data_in.endswith(")"):
                temp_data = data_in.replace("(", "").replace(")", "").split(",")        # Remove "(" and ")" and split each elements into list.
                data = [item.strip() for item in temp_data]         # list comprehension to strip each element.
                
            if len(data) == 1 and data[0] == '':
                print("\nError: Data can't be empty.")
            else:
                break

        analysis(data)
        return

    def Single():
        '''
        Function to allow user to enter each data one by one.
        '''
        print("\nOne at a time.")
        print("Put each element into the list one at a time.")
        print("Every non-numerical elements will not be included in the calculation.")
        
        data = []
        
        while True:
            print(f"\nCurrent: {data}")
            data_in = input("\nEnter here(single): ")
            
            if data_in.lower().strip() == "done":
                if len(data) < 1:
                    print("\nError: Data can't be empty.")
                else:
                    break
                
            data.append(data_in.strip())
                
        analysis(data)
        return
    
    def main_menu():
        '''
        User main menu to choose input mode.
        '''
        input_mode = {
        "1" : WholeList,
        "2" : Single
        }
        
        print("Basic Data Analysis")
        print("Calculate the mean, median, and mode.\n")
        
        while True:
            print("What input mode do you want to use?")
            print("1. Whole list.")
            print("2. One at a time.")
            print("Type 'Exit' to exit.")
            
            mode = input("\nEnter here(menu): ")
            
            if mode.lower().strip() == "exit":
                print("\nExiting...")
                return
            
            if mode in input_mode:
                input_mode[mode]()
            else:
                print("\nError: Invalid menu option. Please enter 1, 2, or 'Exit'.\n")
        
    '''
    Initialization phrase of the program to install necessary dependencies.
    '''
    print("Initialization...")
    requirements = ["statistics"]
    all_installed = True
    for req in requirements:
        if not install_and_import(req):
            all_installed = False
        
    if all_installed:
        import statistics as st
        print("\nAll requirements is met. Running the program...\n")
        main_menu()
    else:
        confirmation = input("\nNot all requirements is met. Run the program anyway? (y/N): ")
        if confirmation.strip().lower() == "y":
            print("\nNoted that the program might crash.\n")
            main_menu()
        elif confirmation.strip().lower() == "n" or confirmation.strip().lower() == "":
            print("\nAborted...\n")
                
if __name__ == "__main__":
    main()