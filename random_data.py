# Random data generation script for Basic_Data_Analysis.py

import random

def main():
    def WriteData(data_list, filename="random_data.txt"):
        """
        Writes a list of data to a file.  Handles potential errors.

        Args:
            data_list (list): The list of data to write.
            filename (str, optional): The name of the file to write to.
                Defaults to "random_data.txt".
        """
        print("\n--- Begin writing data. ---")
        try:
            with open(filename, "w") as file:
                #  Write each data point on a new line, handles non-string data
                for item in data_list:
                    file.write(str(item) + "\n")
            print(f"\n>> Saved to {filename}")
            print("NOTICE: File will be save within the same directory as the script.")
        except FileNotFoundError:
            print(f"ERROR: The file '{filename}' was not found.  Check the path.")
        except PermissionError:
            print(f"ERROR: You do not have permission to write to '{filename}'.")
        except OSError as e:
            print(f"ERROR: An operating system error occurred while writing to '{filename}': {e}")
        except Exception as e:
            print(f"An unexpected error occurred while writing to '{filename}': {e}")
        else: # Added else to only print on success
            print("\n--- Data written successfully. ---")
        finally:
            input("\nPress 'Enter' to return to main.\n") #This input should always execute

    def DataGen(mode):
        """
        Generates random data based on the specified mode ('int' or 'float').

        Args:
            mode (str): The data generation mode ('int' or 'float').
        """
        def get_valid_condition(prompt):
            """
            Prompts the user for input and validates that it is an integer.

            Args:
                prompt (str): The prompt to display to the user.

            Returns:
                int: The valid integer input from the user.
            """
            while True:
                data_in = input(prompt)
                
                try:
                    data = int(data_in)
                    return data
                except ValueError:
                    print("\nERROR: Input is not 'int' or cannot be converted to. Try again.")
            
        match mode:
            case "int":     # mode 1
                spoint = get_valid_condition("\nEnter starting point(number): ")
                epoint = get_valid_condition("Enter end point(number): ")
                data_range = get_valid_condition("Enter data range(how many(number)): ")
                
                data_list = []
                for _ in range(data_range):
                    data_list.append(random.randint(spoint, epoint)) # Use randint for integers
                    
                WriteData(data_list)
                   
            case "float":   # mode 2
                spoint = get_valid_condition("\nEnter starting point(number): ")
                epoint = get_valid_condition("Enter end point(number): ")
                dplace = get_valid_condition("Enter decimal places(how many floating-point(number)): ")
                data_range = get_valid_condition("Enter data range(how many(number)): ")
                
                data_list = []
                for _ in range(data_range):
                    data_list.append(round(random.uniform(spoint, epoint), dplace))
                    
                WriteData(data_list)

    print("\n--- Random number generator (extra) ---")

    print("\nRDGen menu:")
    print("1. Generate whole numbers.")
    print("2. Generate floating-point numbers.")
    print("\nNote: Every new generated data will overwirte the existing data.")

    mode_map = {
    "1" : "int",
    "2" : "float"
    }
    
    print("\nType 'stop' to stop and return.")
    mode = input("Enter mode(number): ").strip().lower()
    
    if mode == "stop":
        print("\nStopping...")
    
    if mode in mode_map:
        DataGen(mode_map[mode])
    else:
        print("\nERROR: Selected mode does not exist. Try again.\n")
            
if __name__ == "__main__":
    main()