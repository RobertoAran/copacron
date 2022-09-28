import hashlib
import os
import shutil
import sys
from datetime import date

logRoute = ""


def Log(write):
    print(write)
    time = str(date.today())
    file = open(logRoute + "/" + time + ".log", "a")
    file.write(write)
    file.close()


def deleteDir(destination):
    shutil.rmtree(destination)
    text = "Directory deleted: " + destination
    Log(text)


def deleteFile(destination):
    os.remove(destination)
    text = "File deleted: " + destination
    Log(text)


def createDir(destination):
    os.mkdir(destination)
    text = 'Directory created: ' + destination
    Log(text)


def copyFile(origin, destination):
    shutil.copy(origin, destination)
    text = 'File replaced: ' + destination
    Log(text)


def createFile(origin, destination):
    shutil.copy(origin, destination)
    text = 'File created: ' + destination
    Log(text)

# this function checks if the files in the destination folder are the same as in the original folder, and deletes
# the excess files.
def scanDestinyDelete(origin, destiny):
    originFileArray = []
    with os.scandir(origin) as originFiles:
        with os.scandir(destiny) as destinationFiles:

            for originFile in originFiles:
                originFileArray.append(originFile.name)

            for destinationFile in destinationFiles:
                if destinationFile.name not in originFileArray:
                    removeThis = destiny + '/' + destinationFile.name
                    if os.path.isdir(removeThis):
                        deleteDir(removeThis)
                    else:
                        deleteFile(removeThis)

# This function takes care of creating a hash of the files passed to it, and returns the hash.
def hash_file(filename):
    h = hashlib.sha1()
    with open(filename, 'rb') as file:
        chunk = 0
        while chunk != b'':
            chunk = file.read(1024)
            h.update(chunk)
    return h.hexdigest()

# This function checks if the file checked in the original file exists in the destination, it returns a hash,
# "dir" or nothing.
def scanDestiny(destination, is_file):
    if os.path.exists(destination):
        if is_file:
            return hash_file(destination)
        return "dir"
    return "none"

# This function is in charge of scanning the source directory and sending it to the functions in charge of
# deleting/changing/creating as well as to those in charge of checking if it is in the copy directory.
def scanOrigin(original, destiny):
    if os.path.isdir(original):
        scanDestinyDelete(original, destiny)
        with os.scandir(original) as ficheros:
            for fichero in ficheros:
                origin = original + '/' + fichero.name
                destination = destiny + '/' + fichero.name
                if fichero.is_file():
                    response = scanDestiny(destination, True)
                    if response != "none" and hash_file(origin) != response:
                        copyFile(origin, destiny)
                    if response == "none":
                        createFile(origin, destiny)
                else:
                    if fichero.is_dir():
                        response = scanDestiny(destination, False)
                        if response == "dir":
                            scanOrigin(origin, destination)
                        else:
                            createDir(destination)
                            scanOrigin(origin, destination)


# Main function in charge of starting the processes and creating the copy base directory.
if __name__ == '__main__':
    arguments = sys.argv[1:]
    origin = arguments[0]
    destiny = arguments[1]
    logRoute = arguments[2]
    if not os.path.isdir(destiny):
        createDir(destiny)
    scanOrigin(origin, destiny)
