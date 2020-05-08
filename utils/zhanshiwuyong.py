# CopyRight @yujir 
# 日期处理模块

class dateUtil:
    '''
    日期处理工具
    '''
    def __init__(self):
        pass

    def __conbine_str(self): # 私有方法
        return "PPPP"  

    def __reNumList(self,num1,num2):
        # 返回一个yearList的列表
        # num1 和 num2 都是一个int 类型的数据
        if int(num1) > int(num2):
            # print("第一个数字大于第二个数字，返回一个空列表")
            return []
        return [i for i in range(int(num1),int(num2)+1)]
    
    def __yearList(self,startYear,endYear):
        # 返回一个年份列表
        return self.__reNumList(startYear, endYear)
  
    def __monthList(self,startMonth,endMonth):
        # 返回一个月份列表
        return self.__reNumList(startMonth,endMonth)

    def __dayList(self,startDay,endDay):
        # 返回一个Day列表
        return self.__reNumList(startDay,endDay)

    def __howDayInThisMonth(self,year,month):
        # 获取这个月到底有多少天 函数封装
        if month in [1,3,5,7,8,10,12]:
            return 31
        elif month in [4,6,9,11]:
            return 30
        elif month in [2,]:
            if year % 4 == 0:
                return 28
            else:
                return 29
        else:
            # 返回0的时候，表示这月份不存在
            return 0

    def getWorKDayList(self,s_year,s_month,s_day,e_year,e_month,e_day):
        # 返回一个所有工作日的列表
        # exp ["2018-01-01","2018-01-02"]
        # print(s_year,s_month,s_day,e_year,e_month,e_day)

        yearList = self.__yearList(s_year,e_year)

        yearlen =len(yearList) # 年份列表的长度
        # print("yearlen",yearlen)
        if yearlen <= 0:
            print("逻辑出现问题! 程序即将终止")
            return
        
        elif yearlen == 1:
            monthList= self.__monthList(s_month,e_month)
            for month in monthList:
                days =  self.__howDayInThisMonth(yearList[0], month)
                if monthList.index(month) == 0:
                    dayList = self.__dayList(s_day,days)
                    for day in dayList:
                        print(yearList[0], month, day)
                elif monthList.index(month) == len(monthList) - 1:
                    dayList = self.__dayList(1,e_day)
                    for day in dayList:
                        print(yearList[0], month, day)
                else:
                    dayList = self.__dayList(1,days)
                    for day in dayList:
                        print(yearList[0], month, day)

        else:
            for year in yearList:
                if yearList.index(year) == 0:
                    monthList = self.__monthList(s_month, 12)
                    for month in monthList:
                        days =  self.__howDayInThisMonth(yearList[0], month)
                        if monthList.index(month) == 0:
                            dayList = self.__dayList(s_day,days)
                            for day in dayList:
                                print(yearList[0], month, day)
                        else:
                            dayList = self.__dayList(1,days)
                            for day in dayList:
                                print(yearList[0], month, day)


                elif yearList.index(year) == yearlen - 1:
                    monthList = self.__monthList(1, e_month)
                    for month in monthList:
                        days =  self.__howDayInThisMonth(yearList[0], month)
                        dayList = self.__dayList(1,days)
                        for day in dayList:
                            print(yearList[0], month, day)

                else:
                    monthList = self.__monthList(1, 12)
                    for month in monthList:
                        days =  self.__howDayInThisMonth(yearList[0], month)
                        if monthList.index(month) == len(monthList) - 1:
                            dayList = self.__dayList(1,e_day)
                            for day in dayList:
                                print(yearList[0], month, day)
                        else:
                            dayList = self.__dayList(1,days)
                            for day in dayList:
                                print(yearList[0], month, day)          
           
        
class timeUtil:
    '''
    时间处理工具 调用一个程序 返回00:00
    '''
    def __init__(self):
        pass

    def __conbine_str(self,hours,minutes): # 私有方法
        pass

    def __strToInt(self):
        
        pass

if __name__ == "__main__":
    s_year = "2019"
    s_month = "3"
    s_day = "23"
    e_year = "2020"
    e_month = "2"
    e_day = "3"
    dateUtil1 = dateUtil()
    dateUtil1.getWorKDayList(s_year,s_month,s_day,e_year,e_month,e_day)

    pass