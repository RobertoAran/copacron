from crontab import CronTab
import sys


def cron():
    arguments = sys.argv[1:]
    my_cron = CronTab(user=True)
    commandFin = 'python code.py' + ' ' + arguments[3] + ' ' + arguments[4] + ' ' + arguments[5]
    job = my_cron.new(command=commandFin)
    job.minute.every(arguments[0])
    job.hour.every(arguments[1])
    job.day.every(arguments[2])

    my_cron.write()


if __name__ == '__main__':
    cron()
