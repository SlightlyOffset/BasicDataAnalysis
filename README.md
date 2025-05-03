# BasicDataAnalysis
 Basic Data Analysis Script to calculate mean, median, and mode.

## Update
- (3 May 2025 9:42PM) Successfully implemented both file support and random data generation.
- (3 May 2025) Currently working on random data generation.
- (3 May 2025) Working on file support

# Basic Data Analysis Script Documentation

## Overview
This script performs basic data analysis on a given list of numbers, calculating the **mean**, **median**, and **mode**. It provides two input methods: entering a whole list at once or entering numbers one by one.

## Features
- **Automatic Package Installation**: Ensures required Python packages are installed.
- **Two Input Modes**:
  - **Whole List Mode**: Users can input an entire list of numbers at once.
  - **Single Entry Mode**: Users can enter numbers one at a time.
- **Data Validation**: Filters valid numerical data from invalid entries.
- **Basic Statistics Calculation**: Computes mean, median, and mode.
- **Interactive Menu**: Provides a user-friendly interface.

## Requirements
- Python 3.x
- `statistics` module (automatically installed if missing)

## Script Flow
1. **Initialization**
   - Checks if the required package (`statistics`) is installed.
   - Prompts user for installation if missing.
   - Imports necessary modules.
2. **Main Menu**
   - Asks the user to select an input mode.
   - Options: Enter a whole list at once or enter numbers one by one.
3. **Data Processing**
   - Filters out invalid (non-numeric) inputs.
   - Converts valid inputs to floats.
4. **Statistical Analysis**
   - Computes and displays:
     - **Mean** (Average)
     - **Median** (Middle value)
     - **Mode** (Most common value)
   - Lists invalid inputs (if any).
5. **User Interaction**
   - Returns to the menu for new inputs.
   - Allows exiting the program at any point.

## Functions Overview
### `install_and_import(package)`
- Checks if a package is installed.
- If missing, prompts the user for installation.
- Returns `True` if successful, `False` otherwise.

### `analysis(data)`
- Filters valid numbers from user input.
- Calculates and displays mean, median, and mode.
- Prints invalid inputs if present.

### `WholeList()`
- Accepts a comma-separated list or a tuple-like input.
- Calls `analysis(data)` to process the input.

### `Single()`
- Accepts one number at a time until the user types `done`.
- Calls `analysis(data)` to process the input.

### `ReadFile()`
- Prompts for a `.txt` file containing space-separated numbers.
- Reads and processes the content, passing it to `analysis(data)`.

### `RandomGen()`
- Allows the user to specify how many numbers to generate and the range.
- Generates random floats and sends them to `analysis(data)`.

### `main_menu()`
- Displays the main menu.
- Allows users to choose between input modes or exit.

### `main()`
- Ensures dependencies are installed.
- Initiates the main menu.

## Usage
Run the script using:
```bash
python Basic_Data_Analysis.py
```
Follow the prompts to enter data and perform calculations.

## Notes
- Invalid inputs (non-numeric entries) are ignored and displayed separately.
- The script handles exceptions and provides interactive feedback.
- File input must point to a valid `.txt` file with readable numeric data.

## Future Enhancements
- Support for additional statistical measures (variance, standard deviation).
- Graphical representation of results (e.g., histograms).
- Export results to a file (CSV or JSON).
- Add unit tests or interactive learning prompts.
---

## Author
- SlightlyOffset

---

## Version
- 1.1 (3 May 2025)
