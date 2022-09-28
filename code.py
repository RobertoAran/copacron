import hashlib
import os
import shutil
import sys
from datetime import date

# def comparatorToDelete(origin, destination):
#     i = 0
#     with os.scandir(origin) as originFiles:
#         with os.scandir(destination) as destinationFiles:
#             if len(originFiles) != len(destinationFiles):
#                 if len(originFiles) > len(destinationFiles):
#                     for originFile in originFiles:
#                         while
#                 else:

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


def hash_file(filename):
    h = hashlib.sha1()
    with open(filename, 'rb') as file:
        chunk = 0
        while chunk != b'':
            chunk = file.read(1024)
            h.update(chunk)
    return h.hexdigest()


def scanDestiny(destination, is_file):
    if os.path.exists(destination):
        if is_file:
            return hash_file(destination)
        return "dir"
    return "none"


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


if __name__ == '__main__':
    arguments = sys.argv[1:]
    origin = arguments[0]
    destiny = arguments[1]
    logRoute = arguments[2]
    if not os.path.isdir(destiny):
        createDir(destiny)
    scanOrigin(origin, destiny)
