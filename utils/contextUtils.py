# CopyRight @yujir 
# 日期处理模块
# 目前时间节点选择只能实现一个小时打一次车

import datetime
import random

class contextUtils:
    '''
    日期处理工具
    '''
    def __init__(self):
        self.hoursLits = [h for h in range(7,20)]
        # 目前的hoursList只能按照7 20 zhong 去随机选择 还不能只能的按照出现规律去生成
        self.minutesList = [m for m in range(0,60)]

    def WdayToChn(self,thisWday):
        if thisWday == "Monday":
            return "周一"
        elif thisWday == "Tuesday":
            return "周二"
        elif thisWday == "Wednesday":
            return "周三"
        elif thisWday == "Thursday":
            return "周四"
        elif thisWday == "Friday":
            return "周五"
        elif thisWday == "Saturday":
            return "周六"
        elif thisWday == "Sunday":
            return "周日"
        else:
            return ""

    def HowManyTimeOneDay(self):
        randonMun = random.random()
        if randonMun <= 0.01:
            return 0
        elif randonMun <= 0.02:
            return 5
        elif randonMun <= 0.12:
            return 1
        elif randonMun <= 0.22:
            return 4
        elif randonMun <= 0.61:
            return 2
        else:
            return 3

    def dateTimeAndWday(self,s_year,s_month,s_day,e_year,e_month,e_day):
        datetimeList = []
        begin = datetime.date(int(s_year),int(s_month),int(s_day))
        end = datetime.date(int(e_year),int(e_month),int(e_day))
        d = begin
        delta = datetime.timedelta(days=1)
        while d <= end:
            # print("%y-%m-%d")
            thisDate = d.strftime("%m-%d")
            thisWday = d.strftime("%A")
            thisWdayChn = self.WdayToChn(str(thisWday))
            datetimeList.append((str(thisDate),thisWdayChn))
            d += delta
        return datetimeList
    
    def getTimeList(self,aboardTimes):
        # 通过检验的标识checkOk
        todayTimeList = list()
        checkOk = False
        while not checkOk:
            todayTimeList = []
            hours = random.sample(self.hoursLits, aboardTimes)
            hours.sort()
            minutes = random.sample(self.minutesList, aboardTimes)
            checkOk = self.CheckTime(hours,minutes)
            # 需要检测数据是否满足要求
        for i in range(0,len(hours)):
            hourStr = str(hours[i])
            minuteStr = str(minutes[i])
            
            if hours[i] == 0:
                hourStr = "00"
            elif hours[i] < 10:
                hourStr = "0" + str(hours[i])
            
            if hours[i] == 0:
                minuteStr = "00"
            if minutes[i] < 10:
                minuteStr = "0" + str(minutes[i])
            todayTimeList.append((hourStr,minuteStr))
        return todayTimeList
    
    def CheckTime(self,hours,minutes):
        for m in range(0, len(hours) - 1):
            temp2 = hours[m+1] * 100 + minutes[m+1]
            temp1 = hours[m] * 100 + minutes[m]
            if temp2 - temp1 <= 70:
                return False
        return True

    def contextItems(self,s_year,s_month,s_day,e_year,e_month,e_day):
        # 行程时间 abordtime
        '''
        return aboardDayList [{'date': '2019-09-08', 'wday': '周日', 'aboardTimes': 1, 'TimeList': [('10', '29')]},{'date': '2019-09-08', 'wday': '周日', 'aboardTimes': 1, 'TimeList': [('10', '29')]}]
        '''
        aboardDayList = list()
        datetimeList = self.dateTimeAndWday(s_year,s_month,s_day,e_year,e_month,e_day)
        for oneday in datetimeList:
            oneDayDict = dict()
            aboardTimes = self.HowManyTimeOneDay()
            todayTimeList = self.getTimeList(aboardTimes)
            # print(todayTimeList)
            oneDayDict["date"] = oneday[0]
            oneDayDict["wday"] = oneday[1]
            oneDayDict["aboardTimes"] = aboardTimes
            oneDayDict["TimeList"] = todayTimeList
            aboardDayList.append(oneDayDict)
        # print(aboardDayList)
        return aboardDayList
                           

if __name__ == "__main__":
    s_year = "2019"
    s_month = "9"
    s_day = "8"
    e_year = "2019"
    e_month = "10"
    e_day = "10"

    gogo =contextUtils()
    gogo.contextItems(s_year,s_month,s_day,e_year,e_month,e_day)
