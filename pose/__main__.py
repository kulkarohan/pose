#!/usr/bin/python3

from datetime import datetime
import os
from signal import signal, SIGINT
from sys import exit
import time


ROOT_DATA_PATH = os.path.join(os.getenv("HOME"), "Pose")


def _handle_exit(signal_received, frame):
    print("\nStopping Pose ...")
    exit(0)


def capture_images(path_to_save: str, minutes_interval: float):
    timestamp = datetime.now().strftime("%Y-%m-%d--%-I:%M%p")
    capture = f"fswebcam -r 1280x720 --save {path_to_save}/{timestamp}.jpg --no-banner"

    print("\n## Press CTRL-C to stop ##")

    # Call _handle_exit() when CTRL-C (ie. SIGINT) is received
    signal(SIGINT, _handle_exit)

    while True:
        os.system(capture)
        print(f"Saving {timestamp}.jpg to {path_to_save} ...")
        time.sleep(60 * minutes_interval)



def _get_time_interval():
    while True:
        try:
            time = float(input("\nMinutes between images: "))
            return time
        except ValueError:
            continue


def _create_folder(path: str):
    if not os.path.exists(path):
        os.mkdir(path)
        print(f"\nImages will be stored in: {path}")
    else:
        print(f"\nAppending images to: {path}")


def _get_folder_path():
    while True:
        name = input("Experiment Name: ")
        path = os.path.join(ROOT_DATA_PATH, name)

        if os.path.exists(path):
            print(f"**WARNING** a folder named '{name}' already exists at: {path}\n")
            choice = input(f"Enter 'a' to append to {name} or Enter 'r' to choose a different name: ")
        else:
            choice = input("Confirm with 'y' or Rename with 'r': ")

        if choice in ('a', 'y'):
            return path


def _display_welcome_message():
    print("#######################")
    print("#   Welcome to Pose   #")
    print("#######################\n")


def main():
    _display_welcome_message()

    path = _get_folder_path()
    _create_folder(path)

    time_interval = _get_time_interval()

    capture_images(path, time_interval)


if __name__ == "__main__":
    main()
