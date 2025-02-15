import sys
import argparse
from datetime import datetime, timedelta
from functions import capture_picture, is_time_between, print_settings, prepare_filesystem, ensure_directory_exists, get_free_space
import os
from time import sleep


def main():

    # gather inbound arguments from the command line
    parser = argparse.ArgumentParser(description='Get CLI input.')
    parser.add_argument('--start_time_of_day', type=str, default="06:00", help='Start time of day in "HH:MM" format')
    parser.add_argument('--end_time_of_day', type=str, default="18:00", help='End time of day in "HH:MM" format')
    parser.add_argument('--save_location', type=str, default="./photos", help='Relative directory path to save pictures')
    parser.add_argument('--total_hours_duration', type=int, default="168", help='Total duration in number of hours format')
    parser.add_argument('--frequency_of_pictures', type=int, default=1, help='Frequency of pictures in minutes')
    args = parser.parse_args()

    # get the current time
    current_date_time = datetime.now()
    complete_date_time = current_date_time + timedelta(hours=args.total_hours_duration)
    start_time = datetime.strptime(args.start_time_of_day, "%H:%M").time()
    end_time = datetime.strptime(args.end_time_of_day, "%H:%M").time()
    total_hours_duration = args.total_hours_duration
    frequency_of_pictures = args.frequency_of_pictures
    
    # get the current path
    folder_path = os.path.abspath(args.save_location)

    ensure_directory_exists(folder_path)
    disk_free_space = get_free_space(folder_path)

    # show the user all the settings we have calculated
    print_settings(start_time, end_time, total_hours_duration, frequency_of_pictures,current_date_time.time(), complete_date_time, folder_path, disk_free_space)

    while datetime.now() < complete_date_time:
        if is_time_between(start_time, end_time):
            print("we are in the time span")
            capture_picture()
            print(f"sleeping for {frequency_of_pictures} minute(s)")
            sleep(frequency_of_pictures * 60)
        else:
            print(f"we are NOT in the time span, sleeping until {start_time}")
        #todo: calculate how long to sleep
        sleep(frequency_of_pictures * 60)

if __name__ == "__main__":
    main()