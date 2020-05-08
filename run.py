# CopyRight @yujir 
from docxtpl import DocxTemplate
from utils.contextUtils import contextUtils
import random
import pymongo


class DiDi:
    def __init__(self):
        # self.context = {"customer_name":"12312121212"}
        self.id = 1
        self.allMoney = 0
        self.client = pymongo.MongoClient(host='localhost', port=27017) 
        self.db = self.client['citys']
        self.collection = self.db['shenz']
        self.colCount = self.collection.count()

    def readFlies(self,tplName):
        '''
        文件读取函数
        '''
        tpl = DocxTemplate(tplName)
        return tpl
    
    def buildPriceAndLong(self):
        # 随机生成价格和公里数
        priceAndLongList = list()
        for i in range(0,100):
            # long = random.uniform(2, 18)
            long = random.uniform(2, 13)
            # unitPrice = random.uniform(2.8, 3.9)
            unitPrice = random.uniform(2.4, 3.2)
            price = long * unitPrice + 2.6
            if price <= 13:
                price = "13.00"
            else:
                price = round(price, 2)
                price = str((price))
            long = str(round(long, 1))
            priceAndLongList.append((long,price))

        return priceAndLongList
    
    def buildStartAndEnd(self):
        randomId = random.randint(1,int(self.colCount))
        oneInfo = self.collection.find({'id':randomId})
        return str(oneInfo[0]["name"])

    def buildContext(self):
        # 构造 context 字典 返回一个字典

        s_year = "2020"
        s_month = "3"
        s_day = "1"
        e_year = "2020"
        e_month = "3"
        e_day = "31"

        contextItem = contextUtils()
        contextList = contextItem.contextItems(s_year,s_month,s_day,e_year,e_month,e_day)
        # print(contextList)     
        itemList = list()
        priceAndLongList = self.buildPriceAndLong()
        for oneday in contextList:
            # print(oneday)
            for eachItem in oneday["TimeList"]:
                item = dict()
                item['id'] = self.id
                if self.id % 2 == 1:
                    item['hasColor'] = "has"
                else:
                    item['hasColor'] = "hasNot"
                item['type'] = "快车"
                item['date'] = oneday["date"]
                item['time'] = eachItem[0] + ":" + eachItem[1]
                item['day'] = oneday["wday"]
                item['city'] = "深圳市"
                item['startPlace'] = self.buildStartAndEnd()
                item['endPlace'] = self.buildStartAndEnd()
                item['long'] = priceAndLongList[self.id][0]
                item['price'] = priceAndLongList[self.id][1]
                self.allMoney += float(priceAndLongList[self.id][1]) 
                itemList.append(item)
                self.id += 1

        context = { 
            'items' : itemList,
            'phoneNum' : '13212341234', # 电话号码 字符串
            'travelTimes': '1', # 总乘车次数 字符串
            'totalAmount': str(round(self.allMoney, 2)), # 总金额 字符串
            'startDate': s_year + "-" + s_month + "-" + s_day,
            'endDate': e_year + "-" + e_month + "-" + e_day,
            'applyDate': e_year + "-" + e_month + "-" + e_day
        }
        return context
        
    def contextSlice(self,context):
        # context 切片，返回数组
        # print(context)
        tempContext = context
        contextList = []

        items = context["items"]
        # print(items)
        itemsLen = len(items)
        print("items的总长度",itemsLen)

        if itemsLen <= 12:
            context["pageId"] = 1
            context["pageAll"] = 1
            context["travelTimes"] = itemsLen
            return [context,]
        else:
            exit_pages = (itemsLen - 12)  // 16 + 1
            items1 = items[0: 12]
            # print(items1)
            tempContext["items"] = items1
            # print(tempContext)
            tempContext["pageId"] = 1
            tempContext["pageAll"] = exit_pages + 1
            tempContext["travelTimes"] = itemsLen
            contextList.append(tempContext)
            print("额外的页面数量", exit_pages)
            for i in range(0,exit_pages):
                newContextDict = dict()
                newContextDict["items"] = items[12 + 16 * i: 12 + 16 * (i + 1)]
                newContextDict["pageId"] = i + 2
                newContextDict["pageAll"] = exit_pages + 1
                # print(newContextDict)
                contextList.append(newContextDict)
            print(exit_pages,itemsLen)
            
            return contextList
    
    def changeKeys(slef,tpl,context):
        '''
        把需要改变的数据写入
        '''
        tpl.render(context)
        return tpl

    def saveFiles(self,tpl,pageId):
        '''
        文件保存
        '''
        documentName = "resluts\page" + str(pageId) + ".docx"
        tpl.save(documentName)
    
    def checkStartMentInputDate(self,dateStr):
        print(dateStr)
        
        return (False,"2019-01-01")
        pass
    
    def startMenu(self):
        # 程序启动菜单
        print("DIDI行程生成工具")
        print("请依次填入以下信息！！！")
        applyDate = input("1.---申请日期： exp：2019-1-1")
        resultLsist = self.checkStartMentInputDate(applyDate)
        
        startDate = input("2.---开始日期： exp：2019-1-1")
        endDate = input("3.---截止日期： exp：2019-1-1")
        telphone = input("4.---电话日期： exp：13212345678")

        


    def run(self):
        # userInfo = self.startMenu()

        context = self.buildContext()
        sliceContextList = self.contextSlice(context)
        
        for eachContext in sliceContextList:
            if sliceContextList.index(eachContext) == 0:
                print("页面不超过12页，只打开第一个模板")
                tplPgae = self.readFlies("./template/didi_tpl_page1.docx")
                tpl = self.changeKeys(tplPgae, eachContext)
                self.saveFiles(tpl, eachContext["pageId"])
            else:
                print("页面超过12页，打开第二个模板")
                tplPgae = self.readFlies("./template/didi_tpl_page2.docx")
                tpl = self.changeKeys(tplPgae, eachContext)
                self.saveFiles(tpl, eachContext["pageId"])
        
        print("此次生成的金额为：", self.allMoney)

if __name__ == "__main__":
    didi = DiDi()
    didi.run()