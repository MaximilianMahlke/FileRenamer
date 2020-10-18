import os
import shutil
from os import path

# modified version, original tutorial at https://lerneprogrammieren.de/dateien-pfade-umbenennen-tutorial/
def main():

    dir = "C:/CODING/Playground/Projects/FileRenamer/"
    fileName = "1.txt"

    #check if file exists
    if path.exists(dir + fileName):
        #rename file
        os.rename(dir + fileName, dir + "MrOne.txt")

if __name__ == "__main__":
    main()
