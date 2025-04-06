# File detector
from time import sleep
from threading import Thread as t
import os
import sys
import keyboard as k

# Used to check if dirs are already in use
dir_conts = []

# Directories
dirs = []

def get_file_name(list_files: list, file: str):
    if file not in list_files:
        return True
    else:
        return False

# Main function where the folder is detected for any added file
def check_files(directory):
    initial_files = os.listdir(directory)
    print(f"WAITING IN DIR: {directory}...")

    while True:

        f = os.listdir(directory)

        if len(f) > len(initial_files):

            file = []
            new_files = len(f) - len(initial_files)
            print(f"CHECK FOR FILES IN dir[ #{directory} #]. NEW FILES ADDED: {new_files} file(s)")

            for file in f:
                if get_file_name(initial_files, file):
                    print(f"{file}: THIS FILE/DIRECTORY(file) WAS ADDED")
            
            initial_files = f
        
        sleep(1)

def quit():
    while True:
        if k.is_pressed("q"):
            print("EXITING...")
            sys.exit()
            break

def add_dir():
    while True:
        if k.is_pressed("ctrl+shift+o"):
            dir = input('Enter dir: ')
            dirs.append(dir)

def test():
    while True:
        if k.is_pressed("ctrl+o"):
            direct = input("Enter filename: ")
            filename = input("Enter filename: ")
            with open(f"{direct}/{filename}", "w") as f:
                f.write("made file")

# Function to run multiple Threads to not focus one Dirctory but may
def thread():
    while True:
        try:
            for dir in dirs:
                # Checking if dir is already being scanned or has already been scanned
                if dir in dir_conts:
                    continue

            # Thread initialisation
                thr = t(target=check_files, args=(dir,))
                thr.daemon = True
                thr.start()
                dir_conts.append(dir)
        except FileNotFoundError as e:
            print(f"{e}: {dir}")
    
        thr2 = t(target=add_dir)
        thr2.daemon = True
        thr2.start()

# Starting the Func( !Dont Change! )
if __name__ == "__main__":
    thr = t(target=quit)
    thr.start()
    thr2 = t(target=test)
    thr2.daemon = True
    thr2.start()

    with open("Directories.txt", "r") as f:
        text = f.readlines()
        for directory in text:
            dirs.append(directory)

    prompt = input("Enter a directory you want to scan( Else type in start): ")
    if prompt == "start":
        thread()
    else:
        dirs.append(dir)
        thread()
