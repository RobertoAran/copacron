import hashlib
import os
import pathlib
import sys
import shutil


def hash_file(filename):
    h = hashlib.sha1()
    with open(filename, 'rb') as file:
        chunk = 0
        while chunk != b'':
            chunk = file.read(1024)
            h.update(chunk)
    return h.hexdigest()


def scanDestiny(destiniDir):
    if os.path.exists(destiniDir):
        if destiniDir.is_file():
            return hash_file(destiniDir)
        return "dir"
    return "none"


def scanOrigin(arguments, actualRute):
    with os.scandir(arguments[0]) as ficheros:
        for fichero in ficheros:
            originDir = arguments[0] + '/' + fichero.name
            destiniDir = arguments[1] + '/' + fichero.name
            if fichero.is_file():
                scanDestiny()
            if fichero.is_dir():
                scanOrigin(destiniDir)


if __name__ == '__main__':
    # arguments = sys.argv[1:]
    arguments = ['/home/roberto/PycharmProjects/Crontab', '/home/roberto/PycharmProjects/Cronta']
    scanOrigin(arguments)
