import sys
import argparse
from datetime import datetime
from functions import print_settings, prepare_filesystem, ensure_directory_exists, get_free_space
import os


def main():

    # gather inbound arguments from the command line
    parser = argparse.ArgumentParser(description='Get CLI input.')
    parser.add_argument('--start_time_of_day', type=str, default="06:00", help='Start time of day in "HH:MM" format')
    parser.add_argument('--end_time_of_day', type=str, default="18:00", help='End time of day in "HH:MM" format')
    parser.add_argument('--save_location', type=str, default="./photos", help='Relative directory path to save pictures')
    parser.add_argument('--total_time_duration', type=int, default="168", help='Total duration in number of hours format')
    parser.add_argument('--frequency_of_pictures', type=int, default=300, help='Frequency of pictures in seconds')
    args = parser.parse_args()

    # get the current time
    current_time = datetime.now()

    # get the current path
    folder_path = os.path.abspath(args.save_location)

    ensure_directory_exists(folder_path)
    disk_free_space = get_free_space(folder_path)

    # show the user all the settings we have
    print_settings(args, current_time, folder_path, disk_free_space)




if __name__ == "__main__":
    main()