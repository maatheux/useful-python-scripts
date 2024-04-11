import datetime


class GetDay:
    def __init__(self):
        self.__dateToday = datetime.datetime.now()
        self.__monthNumber = self.__dateToday.strftime("%m")
        self.__yearNumber = self.__dateToday.strftime("%Y")
        self.__dayNumber = self.__dateToday.strftime(f"%d")

    def getDay(self):
        return self.__dayNumber

    def getMonth(self):
        return self.__monthNumber

    def getYear(self):
        return self.__yearNumber

    def getYesterday(self, nDays):
        yesterday = self.__dateToday - datetime.timedelta(days=nDays)
        return yesterday.strftime("%d-%m-%Y")

    def getMonthName(self):
        return self.__dateToday.strftime("%B")

    def getDayOfWeek(self):
        return self.__dateToday.strftime("%w")


if __name__ == '__main__':
    sla = GetDay()

    print(sla.getDayOfWeek())


