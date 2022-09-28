import pathlib
import sys

from crontab import CronTab

def cron(arguments):

    my_cron = CronTab(user=True)
    commandFin = 'python' + ' ' + str(pathlib.Path().resolve()) + '/' + 'code.py' + ' ' + arguments[3] + ' ' + arguments[4] + ' ' + arguments[5]
    job = my_cron.new(command=commandFin)
    job.minute.every(arguments[0])
    job.hour.every(arguments[1])
    job.day.every(arguments[2])

    try:
        my_cron.write()
    except:
        print("you dont have put valid values")

if __name__ == '__main__':
    arguments = sys.argv[1:]
    cron(arguments)
