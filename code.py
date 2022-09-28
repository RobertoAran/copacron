import os
# import sys

def scandir(arguments):
    ejemplo_dir = '/home/roberto/PycharmProjects/Crontab'
    with os.scandir(ejemplo_dir) as ficheros:
        for fichero in ficheros:
            if fichero.is_file() or fichero.is_dir():
                print(fichero.name)

if __name__ == '__main__':
    # arguments = sys.argv[1:]
    arguments = '/home/roberto'
    scandir(arguments)
