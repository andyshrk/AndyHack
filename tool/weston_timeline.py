#!/usr/bin/env python
import json
import argparse

def parse_time(time_arr):
    # Convert seconds and nanoseconds to total nanoseconds
    return time_arr[0] * 1_000_000_000 + time_arr[1]

def calculate_time_differences(log_lines):
    times = []
    
    # Parse each log line
    for line in log_lines:
        # Remove whitespace and parse JSON
        data = json.loads(line.strip())
        times.append(parse_time(data['T']))
    
    # Calculate time differences (in milliseconds)
    differences = []
    for i in range(1, len(times)):
        diff_ns = times[i] - times[i-1]  # difference in nanoseconds
        diff_ms = diff_ns / 1_000_000    # convert to milliseconds
        differences.append(diff_ms)
    
    return differences

def main():
    # Create command line argument parser
    parser = argparse.ArgumentParser(description='Calculate time differences between adjacent timestamps in log file')
    parser.add_argument('log_file', help='Path to the log file')
    args = parser.parse_args()

    try:
        # Read log file
        with open(args.log_file, 'r') as file:
            log_lines = file.readlines()

        # Calculate time differences
        time_diffs = calculate_time_differences(log_lines)

        # Print results
        print("Time differences between adjacent lines (milliseconds):")
        for i, diff in enumerate(time_diffs, 1):
            print(f"Line {i} to {i+1} diff: {diff:.2f} ms")

    except FileNotFoundError:
        print(f"Error: File not found '{args.log_file}'")
    except json.JSONDecodeError:
        print("Error: Invalid log file format. Please ensure each line is valid JSON")
    except Exception as e:
        print(f"Error occurred: {str(e)}")

if __name__ == '__main__':
    main()
