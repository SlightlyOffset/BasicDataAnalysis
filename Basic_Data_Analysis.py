"""
Basic Data Analysis Program
===========================

This program performs basic statistical analysis on numeric data provided by the user,
calculating the mean, median, and mode(single, multi) of the dataset.

Features:
---------
* Automatically checks for and installs required dependencies (statistics module)
* Offers three different input methods:
    1. Whole list - Enter all numbers at once, comma-separated
    2. Single entry - Enter numbers one at a time
    3. Read from file - Read data from a txt file
* Offer one extra feature to randomly generate data for file input (Option 4)
* Handles non-numeric inputs gracefully by filtering them out
* Provides clear user prompts and error messages

Usage:
------
1. Run the program
2. Authorize installation of required packages if prompted
3. Select an input mode from the main menu:
   - Option 1: Enter a comma-separated list of numbers
   - Option 2: Enter numbers one at a time, type 'done' when finished
   - Option 3: Enter file path to open and read data from file.
   - Option 4 (extra): Unrelated to data input mode, but use to randomly generate data for file input.
4. Review the calculated statistics (mean, median, mode)
5. Type 'Exit' at the main menu to quit the program

Functions:
----------
- Initialization(): Initialization phrase of the program to install necessary dependencies.
    install_and_import(package): Attempts to import a package, installing it if necessary
- analysis(data): Processes the input data and calculates statistics
- filter(raw): Separates valid numerical data from invalid entries
- WholeList(): Handles the whole-list input mode
- Single(): Handles the one-at-a-time input mode
- ReadFile(): Handle txt file input.
- RandomGen(): Use local module(random_data.py) to randomly generate data.
- main_menu(requirements): Displays and manages the main program menu

Dependencies:
------------
- subprocess: Python's built-in subprocess module
- sys: Python's built-in sys module
- statistics: Python's built-in statistics module (installed automatically if needed)
- random: Python's built-in random module (installed automatically if needed)
- random_data.py: Local modlule (must exist within same directory)

Returns:
--------
For valid numerical inputs, the program calculates and displays:
- Mean (average)
- Median (middle value)
- Mode (most common value)
- MultiMode (multiple common value)
- List of any invalid entries that were filtered out

Author:
-------
SlightlyOffset

Version:
--------
1.2

Update 9 May 2025
- Add more error handling
    - Case where random_data.py is missing
- Add status report text in initialization phrase
- Localize imported modules
- Improve modularity
    - Initialization phrase have it own function
- Remove redundant
"""

def Initialization():
    '''
    Initialization phrase of the program to install necessary dependencies.
    '''
    def install_and_import(package):
        """
        Attempts to import a package. If it's not installed, it installs it using pip.
        """
        import subprocess
        import sys
        
        try:
            __import__(package)
            print(f"\n[{package}] is already installed or existed.")
            return True #indicate successful import
        except ImportError:
            if package == "random_data":
                print(f"\nLocal module [{package}] is missing.")
                print(f"\nNOTICE: Make sure [random_data.py] is in the same directory as the main program and try again.")
                print("NOTICE: Or you may download it from the GitHub page [https://github.com/SlightlyOffset/BasicDataAnalysis]")
                
                return False    #Indicate missing random_data.py
                
            print(f"\n[{package}] is not installed. Installing...")
            authorization = input(f"\nAuthorize istallation of {package}? (y/N):  ")
            if authorization.strip().lower() == "y":
                try:
                    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
                    print(f"\n[{package}] installed successfully.")
                    __import__(package) #try import again after install
                    return True #indicate successful import after install
                except subprocess.CalledProcessError as e:
                    print(f"\nERROR installing {package}: {e}")
                    return False #Indicate install failure
                    
            elif authorization.strip().lower() == "n" or authorization.strip().lower() == "":
                print("\nAborted...\n")
                print(f"Note: The program might not work if the package {package} is not installed.")
                input("Press 'Enter' to continue...")
                return False # Package not installed. 
                
    print("--- Initialization... ---")
    requirements = {
    "statistics" : False,
    "random" : False,
    "random_data" : False
    }
    
    all_installed = True
    for req in requirements:
        if install_and_import(req):
            requirements[req] = True
        else:
            all_installed = False   
    
    if all_installed:
        print("\n\n--- Status Report ---\n")
        for module in requirements:
            print(f"Package: {module:<15} Status: {"OK" if requirements[module] else "Missing"}")
            
        return all_installed, requirements, False
        
    else:
        print("\n\n--- Status Report ---\n")
        for module in requirements:
            print(f"Package: {module:<15} Status: {"OK" if requirements[module] else "Missing"}")
            
        confirmation = input("\nNOTICE: Not all requirements is met. Run the program anyway? (y/N): ")
        if confirmation.strip().lower() == "y":
            return all_installed, requirements, False
            
        elif confirmation.strip().lower() == "n" or confirmation.strip().lower() == "":
            return all_installed, requirements, True

def main():
    def analysis(data):
        '''
        Function to perform statistical processes.
        '''
        import statistics as st
        def filter(raw):
            
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
        
        if len(valid_data) == 0:
            print("\nERROR: Can't operate on empty sequence.")
            print("     - valid_data(list) is empty.")
            
        try:
            procmean = st.mean(sorted_data)
            procmedian = st.median(sorted_data)
            procmode = st.mode(sorted_data)
            procmultimode = st.multimode(sorted_data)
        
            print("\n--- Result ---")
            print(f"Mean: {procmean}")
            print(f"Median: {procmedian}")
            print(f"Mode(single): {procmode}")
            print(f"Mode(multi): {procmultimode}")
            print(f"Invalid data include: {invalid_data}")
            
        except Exception as e:
            print(f"\nFETAL ERROR: {e}")
            print("NOTICE: This error may occur when critical package is missing.")
        
    def WholeList():
        '''
        Function to allow user to enter the list of data.
        Ex:
            1, 2, 3, 4,...,n
            or
            (1, 2, 3, 4,...,n)
        '''
        print("\n--- Whole List Mode ---")
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
                print("\nERROR: Data can't be empty.")
            else:
                break

        analysis(data)
        input("\nPress 'Enter' to return to menu...\n")
        print("\nReturn to menu...\n")
        return

    def Single():
        '''
        Function to allow user to enter each data one by one.
        '''
        print("\n--- Single Input Mode ---")
        print("Put each element into the list one at a time.")
        print("Every non-numerical elements will not be included in the calculation.")
        
        data = []
        
        while True:
            print(f"\nCurrent: {data}")
            print("Type 'done' to finish and continue.")
            data_in = input("Enter here(single): ")
            
            if data_in.lower().strip() == "done":
                if len(data) < 1:
                    print("\nERROR: Data can't be empty.")
                else:
                    break
                
            data.append(data_in.strip())
                
        analysis(data)
        input("\nPress 'Enter' to return to menu...\n")
        print("\nReturn to menu...\n")
        return
    
    def ReadFile():
        '''
        A function to read data from a file.
        '''
        def OpenFile(namepath):
            '''
            Try to open the file with path given then hand over to analysis(function)
            '''
            print("\n>> Opening file...")
            data_list = []
            try:
                with open(namepath, "r", encoding="utf8") as data:
                    print(f"\n>> File opened: {namepath}")
                    for line in data:
                        try:
                            number = float(line.strip())
                            data_list.append(number)
                        except ValueError:
                            print(f"\nWarning: Skipping non-numeric line: '{line.strip()}'")
            
            except FileNotFoundError:
                print("\nERROR: File not found.")
            except PermissionError:
                print("ERROR: Access denied.")
            except OSError as e:
                print(f"ERROR: An operating system error occurred while operating '{namepath}': {e}")
            except UnicodeDecodeError:
                print(f"ERROR: Unable to decode correctly. Provided file might not encoded in utf8.")
                
            finally:
                analysis(data_list)
                return
                
            
        print("\n--- Read From File Mode ---")
        print("Read data from provided file path(full path)\nor file name within the same directory.")
        print("\nExample for file input:")
        print("- Full path -")
        print("  --> D:\\code\\BasicDataAnalysis\\Example.txt")
        print("- File name -")
        print("For file within the same directory only.")
        print("  --> Example.txt")
        
        while True:
            print("\nType 'format ex' for supported data format.")
            print("Type 'exit' to stop and return to menu.")
            namepath = input("Enter file(path/name): ").strip()
            
            if namepath.lower() == "exit":
                print("\nExiting...")
                break
            
            if namepath.lower() == "format ex":
                print("\nAccepted format:")
                print("- File extension must be .txt UTF8")
                print("- All individual data must be separated with newline.")
                print("    Ex:\n    452.28\n    330.22\n    449.27\n    306.87\n    228.87")
            
            if namepath.startswith('"') and namepath.endswith('"'):
                namepath = namepath.replace('"', '')
                if namepath.endswith(".txt"):
                    OpenFile(namepath)
                    break
                else:
                    print("\nERROR: Not a .txt extension. Try again.")
            
            if not namepath.endswith(".txt"):
                print("\nERROR: Not a .txt extension. Try again.")
            else:
                OpenFile(namepath)
                break
            
        input("\nPress 'Enter' to return to menu...\n")
        print("\nReturn to menu...\n")
        return
    
    def RandomGen():
        import random_data as rdgen
        rdgen.main()
        return
    
    def main_menu(requirements):
        '''
        User main menu to choose input mode.
        '''
        input_mode = {
        "1" : WholeList,
        "2" : Single,
        "3" : ReadFile,
        "4" : RandomGen
        }
        
        while True:
            print("--- Basic Data Analysis ---")
            print("Calculate the mean, median, and mode.\n")
            print("What input mode do you want to use?")
            print("1. Whole list.")
            print("2. One at a time.")
            print("3. Read from file.")
            print(f"4. Randomly generate data (extra){"":<5} Status: {"OK" if requirements["random_data"] else "Missing"}")
            print("Type 'Exit' to exit.")
            
            if not requirements["random_data"]:
                print("\nNOTICE: Option 4 is unavailable due to its file [random_data.py] is missing")
            
            mode = input("\nEnter here(menu): ")
            
            if mode.lower().strip() == "exit":
                print("\nExiting...")
                return
            
            if mode == "4" and not requirements["random_data"]:
                print("\nNOTICE: Option 4 is unavailable due to its file [random_data.py] is missing")
            else:
                if mode in input_mode:
                    input_mode[mode]()
                else:
                    print("\nERROR: Invalid menu option. Please enter 1 to 4 or 'Exit'.\n")
        
    all_installed, requirements, abort_flag = Initialization()
    
    if not abort_flag:
        if all_installed:
            print("\nAll requirements is met. Running the program...\n")
            main_menu(requirements)
        else:
            print("\nWARNING: The program may crash due to missing packages.\n")
            main_menu(requirements)
    else:
        print("\nAborted...")
        
if __name__ == "__main__":
    main()