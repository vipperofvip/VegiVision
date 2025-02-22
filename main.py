import sys
import argparse
from datetime import datetime, timedelta
from functions import (
    is_time_between,
    print_settings,
    prepare_filesystem,
    ensure_directory_exists,
    get_free_space,
)
import os
import logging
from time import sleep
import time

# TODO: test writing to mounted media (handle prepended / as absolute path)
# TODO: Add logging, debug logs
# TODO: periodically show disk space free
# TODO: make requirements.txt and installation instructions




def main():

    # gather inbound arguments from the command line
    parser = argparse.ArgumentParser(description="Get CLI input.")
    parser.add_argument(
        "--start_time_of_day",
        type=str,
        default="06:00",
        help='Start time of day in "HH:MM" format',
    )
    parser.add_argument(
        "--end_time_of_day",
        type=str,
        default="18:00",
        help='End time of day in "HH:MM" format',
    )
    parser.add_argument(
        "--save_location",
        type=str,
        default="./photos",
        help="Relative directory path to save pictures",
    )
    parser.add_argument(
        "--total_duration_days",
        type=int,
        default="168",
        help="Total duration in number of days (default=28)",
    )
    parser.add_argument(
        "--frequency_of_pictures_seconds",
        type=int,
        default=600,
        help="Frequency of pictures in seconds (default=600)",
    )
    parser.add_argument(
        "--run_name",
        type=str,
        default="test",
        help="Sets the picture folder name and file names",
    )
    parser.add_argument(
        "--debug",
        action="store_true",
        help="Debug logging enabled",
    )
    parser.add_argument(
        "--no_camera",
        action="store_true",
        help="Run the program with no camera for testing",
    )
    args = parser.parse_args()

    # get the current time
    current_date_time = datetime.now()
    complete_date_time = current_date_time + timedelta(days=args.total_duration_days)
    start_time = datetime.strptime(args.start_time_of_day, "%H:%M").time()
    end_time = datetime.strptime(args.end_time_of_day, "%H:%M").time()
    run_name = args.run_name
    total_days_duration = args.total_duration_days
    frequency_of_pictures_seconds = args.frequency_of_pictures_seconds
    debug = args.debug
    no_camera= args.no_camera

    if debug:
        logger.setLevel(logging.DEBUG)

    # get the current path
    folder_path = f"{os.path.abspath(args.save_location)}/{run_name}"
    logger.debug(f"The folder path is {folder_path}")

    ensure_directory_exists(folder_path)
    disk_free_space = get_free_space(folder_path)

    # show the user all the settings we have calculated
    print_settings(
        start_time,
        end_time,
        total_days_duration,
        frequency_of_pictures_seconds,
        current_date_time.time(),
        complete_date_time,
        folder_path,
        disk_free_space,
    )

    if not no_camera:
        from picamera2 import Picamera2, Preview
        picam = Picamera2()
        config = picam.create_preview_configuration(main={"size": (1920, 1080)})
        #config = picam.create_preview_configuration()
        picam.configure(config)
        picam.start_preview(Preview.QTGL)
        picam.start()

    while datetime.now() < complete_date_time:
        if is_time_between(start_time, end_time):
            logger.debug("we are in the time span")
            #capture_picture(picam,folder_path,"test1")
            logger.info(f"About to write file {folder_path}/{run_name}_{time.time()}.jpg")
            if not no_camera:
                picam.capture_file(f"{folder_path}/{run_name}_{time.time()}.jpg")
            logger.debug(f"sleeping for {frequency_of_pictures_seconds} seconds")
            sleep(frequency_of_pictures_seconds)
        else:
            logger.debug(f"we are NOT in the time span, sleeping until {start_time}")
            # todo: calculate how long to sleep
            sleep(frequency_of_pictures_seconds)


if __name__ == "__main__":
    # Basic configuration with DEBUG level
    logging.basicConfig(
        level=logging.INFO,  # Set the logging level to DEBUG
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    # Create a logger object
    logger = logging.getLogger(__name__)
    main()
