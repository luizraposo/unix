from datetime import timezone,datetime


def date(ano, mes, dia):
    '''

    :param ano: int
    :param mes: int
    :param dia: int
    :return: date
    '''

    date = datetime(ano,mes,dia)

    return date

def unix(date):
    '''

    :param date: function date
    :return:
    return date to format unix.

    '''

    timestamp = date.replace\
        (
            tzinfo=timezone.utc
         ).timestamp()


    return int(timestamp)


def temp(days, hours, minutes, seconds):

    days = int(days) * 3600 * 24

    hours = int(hours) * 3600

    minutes = int(minutes) * 60

    seconds = int(seconds)

    time = days + hours + minutes + seconds

    return int(time)
