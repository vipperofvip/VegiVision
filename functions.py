import os
import shutil

def prepare_filesystem(path):
    # Get the absolute path of the current file
    current_file_path = os.path.abspath(__file__)

    print(f"The current file path is: {current_file_path}")

def ensure_directory_exists(directory_path):
    """
    Check if a directory exists, if not, create it.

    :param directory_path: The path of the directory to ensure exists.
    """
    if not os.path.exists(directory_path):
        os.makedirs(directory_path)
        print(f"Directory '{directory_path}' was created.")
    else:
        print(f"Directory '{directory_path}' already exists, no need to create it")


def drive_space_free(path):
    return
    #returns the amount of space free on the drive

def print_settings(args, current_time, file_path, disk_free_space):
    current_time_printable = current_time.strftime("%H:%M")
    print("\n")
    print("Settings:")
    print(f"\tThe current time is {current_time_printable} (24h format)")
    print(f"\tPictures will be taken between {args.start_time_of_day} and {args.end_time_of_day}")
    print(f"\tImages will be saved in {args.save_location}")
    print(f"\tTotal duration is {args.total_time_duration} hours")
    print(f"\tPictures will be taken every {args.frequency_of_pictures} seconds")
    print(f"\tPictures will be saved in the folder {file_path}")
    print(f"\tThe pictures folder has {disk_free_space:.2f} MB free space")
    print("\n")

    # Here you would implement the actual picture-taking logic
    # For this example, we'll just simulate it with print statements:
    print("Simulating picture taking...")

def get_free_space(path):
    """
    Get the amount of free disk space at the given path.

    :param path: The directory path for which to check free space.
    :return: Free space in bytes or None if an error occurred.
    """
    try:
        # Convert path to absolute path to ensure we're checking the right location
        abs_path = os.path.abspath(path)
        # Get the free space in bytes
        free_space = shutil.disk_usage(abs_path).free
        # Convert bytes to a more human-readable format
        free_space_mb = free_space / (1024 * 1024)  # Convert to MB
        free_space_gb = free_space / (1024 * 1024 * 1024)  # Convert to GB
        
        #print(f"Free space on {abs_path}:")
        #print(f"  - {free_space} bytes")
        #print(f"  - {free_space_mb:.2f} MB")
        #print(f"  - {free_space_gb:.2f} GB")
        return free_space_mb

    except Exception as e:
        print(f"An error occurred while checking free space: {e}")
        return None