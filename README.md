# Objective:
The objective of this challenge is to build a simple command-line application that parses a stream of events related to translation delivery and produces an aggregated output. 
The application calculates, for every minute, a moving average of the translation delivery time for the last X minutes.

# Requirements:
- The application should accept input from a JSON file containing a stream of translation delivery events.
- It should allow specifying the window size (X) for calculating the moving average delivery time.
- The output should be written to a JSON file and contain average delivery times for each minute.
- The application should maintain a moving window of events and update the average delivery time accordingly.

# Implementation:
The solution provided consists of a Python script named unbabel_cli.py, which utilizes the argparse module for command-line argument parsing. It includes a class named MovingAverageCalculator responsible for calculating the moving average delivery time and a function process_events for processing the input events and generating the output.

# How to test:
1. Ensure Python is installed on your system.
2. Download the unbabel_cli.py script and save it in your desired directory.
3. Run the script from the command line, specifying the input file containing translation events and the desired window size: python3 unbabel_cli.py --input_file events.json --window_size 50

# Output:
The output will be written to a JSON file named output_X.json, where X is the specified window size. 
Each entry in the output file contains the date (rounded down to the nearest minute) and the corresponding moving average delivery time.

# NOTE:
I took the liberty to add more events inside the events.json file to have more outputs.
