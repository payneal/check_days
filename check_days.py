import json
import datetime
import calendar

class Check_days:
    def __init__(self):
        self.results = None
        self.tables_used = []

    # public
    def get_days_data_recieved(self):
        if self.results == None:
            return "need results first"
        return self.__grab_all_data_recieved_days()

    def add_data(self, table, table_data):
        self.tables_used.append(table)
        for x in table_data:
            self.results[x['year']][x['month']][x['day']]['data'][table]=\
                'recieved'
                
    def add_years(self, start, end):
        if start > end:
            return "invalid"
        self.results = self.__gets_multiple_years(start, end)
        
    def months_in_year(self, year):
        
        year_holder = {}
        for x in range(1, 13):
            year_holder[x] = self.days_in_month(year, x) 
        return year_holder

    def days_in_month(self, year, month):
        days = self.__get_days_in_month(year, month) 
        return self.__fill_days_of_months(days, month, year)

    # private

    def __grab_all_data_recieved_days(self):
        data_recieved, not_recieved = self.__get_reciecevd_and_not_structure()
        for year in self.results:
            for month in self.results[year] :
                for day in self.results[year][month]:
                    self.__add_to_recieved_or_not(
                        data_recieved, not_recieved, year, month, day)
        return data_recieved, not_recieved


    def __add_to_recieved_or_not(self,data_recieved, not_recieved, year, month, day):
        for table_name in self.tables_used:
            if table_name in self.results[year][month][day]['data']:
                data_recieved[table_name].append("{}-{}-{}".format(year, month, day))
            else:
                not_recieved[table_name].append("{}-{}-{}".format(year, month, day))


    def __get_reciecevd_and_not_structure(self):
        data_recieved = {}
        not_recieved = {}
        for x in self.tables_used:
            data_recieved[x] = []
            not_recieved[x] = []
        return data_recieved, not_recieved

    def __gets_multiple_years(self, start, end):
        years = {}
        while True:
            start = self.__add_to_years(years, start, end)
            if start > end:
                return years

    def __add_to_years(self, years, start, end):
        year = self.months_in_year(start)
        years[start] = year
        start += 1
        return start
        
    def __fill_days_of_months(self, days, month, year):
        month_holder = {}
        for x in range(1, days+1):
            month_holder = self.__fill_in_day(x, month, year, month_holder)
        return month_holder
    
    def __fill_in_day(self, x, month, year, month_holder):
        day = datetime.datetime(year, month, x)
        month_holder[x] =  {}
        month_holder[x]['dow'] = calendar.day_name[day.weekday()]
        month_holder[x]['data'] = {}
        return month_holder

    def __get_days_in_month(self, year, month):
        d0 = self.__get_date(year, month, 1)
        d1 = self.__get_end_date(year, month)
        return (d1 - d0).days

    def __get_date(self, year, month, day):
        return datetime.datetime(year=year, month=month, day=day)

    def __get_end_date(self, year, month):
        if month != 12:
            return self.__get_date(year, month+1, 1)
        return self.__get_date(year+1, 1,1)
