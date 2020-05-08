
        elif len(yearList) == 1:
            this_year = yearList[0]
            monthList = self.__monthList(s_month,e_month)
            if len(monthList) <= 0:
                print("逻辑出现问题! 程序即将终止")
                return

            else:
                for month in monthList:
                    if month in [1,3,5,7,8,10,12]:
                        print("这个月31天",month)
                        
                    elif month in [4,6,9,11]:
                        print("这个月30天",month)
                    elif month in [2,]:
                        if this_year % 4 == 0:
                            print("则是一个特殊的年份，2月份只有28天")
                            pass
                        else:
                            print("则是一个正常的年份，2月份只有29天")
                            pass
                    else:
                        print("这是一个不存在的月份",month)
                        pass
                        
            print(this_year,monthList)