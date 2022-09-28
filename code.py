import hashlib
import os
import pathlib
import sys
import shutil

def createDir(destination):
    os.mkdir(destination)

def copyFile(origin, destination):
    shutil.copy(origin, destination)

def createFile(origin, destination):
    shutil.copy(origin, destination)


def hash_file(filename):
    h = hashlib.sha1()
    with open(filename, 'rb') as file:
        chunk = 0
        while chunk != b'':
            chunk = file.read(1024)
            h.update(chunk)
    return h.hexdigest()

def scanDestinyDelete():
    print("deleted")

def scanDestiny(destination, is_file):
    if os.path.exists(destination):
        if is_file:
            return hash_file(destination)
        return "dir"
    return "none"

# Scan original route file per file
# call to scanDestiny to comprobate if the file or dir are in the destiny or not
# Recolect hash of origin file and destiny file and if is necesary send to copyFile
def scanOrigin(origin, destiny):
    with os.scandir(origin) as ficheros:
        actualSize = len(ficheros)
        for fichero in ficheros:
            origin = origin + '/' + fichero.name
            destination = destination + '/' + fichero.name
            if fichero.is_file():
                response = scanDestiny(destination, True)
                if response != "none" and hash_file(origin) != response:
                    copyFile(origin, destination)
                else:
                    createFile(origin, destination)
            else:
                response = scanDestiny(destination, False)
                if response == "dir":
                    scanOrigin(origin, destiny)
                else:
                    createDir(destination)
                    scanOrigin(origin, destiny)

if __name__ == '__main__':
    # arguments = sys.argv[1:]
    arguments = ['/home/roberto/PycharmProjects/Crontab', '/home/roberto/PycharmProjects/Cronta']
    origin = arguments[0]
    destiny = arguments[1]
    scanOrigin(origin, destiny)
