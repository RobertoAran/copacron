import hashlib
import os
import pathlib
import sys
import shutil


# def comparatorToDelete(origin, destination):
#     i = 0
#     with os.scandir(origin) as originFiles:
#         with os.scandir(destination) as destinationFiles:
#             if len(originFiles) != len(destinationFiles):
#                 if len(originFiles) > len(destinationFiles):
#                     for originFile in originFiles:
#                         while
#                 else:

def createDir(destination):
    os.mkdir(destination)


def copyFile(origin, destination):
    shutil.copy(origin, destination)


def createFile(origin, destination):
    shutil.copy(origin, destination)


def scanDestinyDelete():
    print("deleted")


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
    print(original, destiny)
    if os.path.isdir(original):
        with os.scandir(original) as ficheros:
            # comparatorToDelete(origin, destiny)
            for fichero in ficheros:
                origin = original + '/' + fichero.name
                destination = destiny + '/' + fichero.name
                if fichero.is_file():
                    response = scanDestiny(destination, True)
                    if response != "none" and hash_file(origin) != response:
                        copyFile(origin, destiny)
                    else:
                        createFile(origin, destiny)
                else:
                    if fichero.is_dir():
                        response = scanDestiny(destination, False)
                        if response == "dir":
                            scanOrigin(origin, destination)
                        else:
                            createDir(destination)
                            scanOrigin(origin, destination)
    print("bucles terminados")


if __name__ == '__main__':
    # arguments = sys.argv[1:]
    arguments = ['/home/roberto/PycharmProjects/Crontab', '/home/roberto/PycharmProjects/Cronta']
    origin = arguments[0]
    destiny = arguments[1]
    if not os.path.isdir(destiny):
        createDir(destiny)
    scanOrigin(origin, destiny)
