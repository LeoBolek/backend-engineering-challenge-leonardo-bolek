import argparse
import json
from collections import deque
from datetime import datetime, timedelta


class MovingAverageCalculator:
    def __init__(self, window_size):
        """
        Initializes the MovingAverageCalculator class with a window size for calculating moving averages.
        """
        self.window_size = window_size  # Set the window size
        self.window = deque()  # Initialize a deque to store events within the window
        self.total_duration = 0  # Initialize the total duration of events within the window

    def add_event(self, event):
        """
        Adds an event to the window and updates the total duration, while keeping the window size within the limit.
        """
        timestamp = datetime.strptime(event["timestamp"], "%Y-%m-%d %H:%M:%S.%f")  # Convert timestamp to datetime object
        duration = event["duration"]  # Get the duration of the event
        self.total_duration += duration  # Update the total duration
        self.window.append((timestamp, duration))  # Add the event to the window

        # Remove events that are outside the window size
        while self.window and timestamp - self.window[0][0] >= timedelta(minutes=self.window_size):
            self.total_duration -= self.window.popleft()[1]  # Remove the oldest event from the window

    def get_average_delivery_time(self):
        """
        Calculates the average delivery time based on events within the window.
        """
        if not self.window:  # If the window is empty, return 0
            return 0
        return self.total_duration / len(self.window)  # Calculate and return the average delivery time

def process_events(input_file, window_size):
    """
    Processes events from an input file, calculates the moving average delivery time, and yields the results.
    """
    calculator = MovingAverageCalculator(window_size)  # Initialize the MovingAverageCalculator
    with open(input_file, "r") as file:
        for line in file:
            event = json.loads(line)  # Parse JSON data into a Python dictionary
            calculator.add_event(event)  # Add the event to the calculator
            timestamp = datetime.strptime(event["timestamp"], "%Y-%m-%d %H:%M:%S.%f")  # Convert timestamp to datetime object
            minute = timestamp.replace(second=0, microsecond=0)  # Round down to the nearest minute
            average_delivery_time = calculator.get_average_delivery_time()  # Get the average delivery time
            yield {"date": minute.strftime("%Y-%m-%d %H:%M:%S"), "average_delivery_time": average_delivery_time}  # Yield the result

def main():
    """
    Main function for command-line execution.
    """
    parser = argparse.ArgumentParser(description="Calculate moving average delivery time")  # Create argument parser
    parser.add_argument("--input_file", type=str, help="Path to the input file", required=True)  # Input file argument
    parser.add_argument("--window_size", type=int, help="Window size for moving average calculation", required=True)  # Window size argument
    args = parser.parse_args()  # Parse command-line arguments

    output_file = f"output_{args.window_size}.json"  # Generate output file name based on window size

    with open(output_file, "w") as file:
        for result in process_events(args.input_file, args.window_size):
            file.write(json.dumps(result) + "\n")  # Write the result as JSON to the output file

if __name__ == "__main__":
    main()  # Call the main function when the script is executed directly
