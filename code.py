import hashlib
import os
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


def scandir(arguments):
    with os.scandir(arguments) as ficheros:
        for fichero in ficheros:
            if fichero.is_file():
                print(fichero.name)
            if fichero.is_dir():
                nameCarpet = arguments + '/' + fichero.name
                scandir(nameCarpet)

if __name__ == '__main__':
    # arguments = sys.argv[1:]
    arguments = '/home/roberto/PycharmProjects/Crontab'
    scandir(arguments)
