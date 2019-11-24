from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import time, re
import datetime
import capital

ur = ""
class S7:
   def __init__(self,fromInput,fromOutput,dateIn):
        self.fromInput=fromInput
        self.fromOutput=fromOutput
        self.date1=dateIn[-4:]+"-"+dateIn[3:5]+"-"+dateIn[:2]
        self.year=int(dateIn[-4:])
        self.month=dateIn[3:5]
        self.day=int(dateIn[:2])
   def poisk(self):
        global ur
        print(self.date1)
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        # options = webdriver.ChromeOptions()
        # options.add_argument('headless')
        driver = webdriver.Chrome(chrome_options=options)
        driver.implicitly_wait(30)
        base_url = "http://s7.ru/"
        verificationErrors = []
                        

        driver.get(base_url)
        town1=driver.find_element_by_css_selector('#flights_origin2')
                # datin=driver.find_element_by_id("date0")
                # datin.click()
                # for i in range(13):
                #     pyautogui.press('backspace')
                # datin.send_keys(self.date)
        time.sleep(2)
        town1.clear()
        town1.send_keys(str(self.fromInput))
        time.sleep(3)
        town1.send_keys(Keys.ENTER)
        time.sleep(3)
        #driver.find_element_by_xpath('//*[@id="aviaBot"]/div[2]/div[1]/div/div[3]/div[2]/div[1]/div[1]/div/div/ul/li/div[2]').click()
        outp=driver.find_element_by_xpath('//*[@id="flights_destination2"]') #город прибвтия
        outp.send_keys(str(self.fromOutput))
        time.sleep(5)
        outp.send_keys(Keys.ENTER)
        datefalse=driver.find_element_by_xpath('//*[@id="date-opener2"]') #календарь
        time.sleep(0.4)
        datefalse.click()
        datefalse.click()
        to_one=driver.find_element_by_xpath('//*[@id="aviaBot"]/div[2]/div[4]/div[2]/div[1]/div/div[2]/div/label') #месяц
        to_one.click()
        now=datetime.datetime.now()
        then=datetime.datetime(year=self.year,month=int(self.month),day=self.day)
        delta=then-now
        key=str(self.month)+str(self.year)
        calendar={'112019':[5,5,6,30],'122019':[6,7,2,31],'012020':[5,3,5,31],'022020':[5,6,6,29],'032020':[6,7,2,31],'042020':[5,3,4,30],'052020':[5,5,7,31],'062020':[5,1,2,30],'072020':[5,3,5,31],'082020':[6,6,1,31],'092020':[5,2,3,30],'102020':[5,4,6,31],'112020':[6,7,1,30]}
        cl=(delta.days//30)
        if (now.day+delta.days) < calendar[key][3]:
            print('pass select month')
            
            print('key:'+key)
            print('delta.month=0')
        elif(now.day+delta.days)//calendar[key][3] == 1:
            next_month=driver.find_element_by_xpath('//*[@id="ui-datepicker-next-avia"]')
            next_month.click()
            
            print('delta.month='+str(delta.days//30))
        else:
            next_month=driver.find_element_by_xpath('//*[@id="ui-datepicker-next-avia"]') #месяц
            next_month.click()
            
            print('delta.month=')
            for i in range(cl):
                next_m=driver.find_element_by_xpath('//*[@id="datepicker2"]/div/div/a[2]')
                next_m.click()
        if delta.days>=359:
            print('нема,вводи меньше')
            return("извините,но билетов на эту дату нет,т.к. компанией s7 еще не составлено расписание.Вы можете искать билеты на любой день, который будет не более чем через 359 дней")
        else:
            print('in calendar')
            
            # print(calendar['112019'][0]) #строки
            # print(calendar['112019'][1]) #первый столбик
            # print(calendar['112019'][2]) #последний столбик
            # print(calendar['112019'][3]) #Дни
            print('key:'+key)
            
            raw=1
            max=7
            day=calendar[key][1]
            for i in range(self.day-1):
                print('Цикл номер:'+str(i))
                # if(day==max):
                #     raw=raw+1
                #     day=1
                #     print(raw)
                #     print(day)
                # else:
                #     day=day+1
                #     print(day)
                if(day<7):
                    day+=1
                    print('day'+str(day))

                else:
                    raw+=1
                    day=1
                    print('raw'+str(raw))
                    print('day'+str(day))
            print(raw)
            print(day)
            x=driver.find_element_by_css_selector('#datepicker2 > div > table > tbody > tr:nth-child('+str(raw)+') > td:nth-child('+str(day)+') > a')
            x.click()
            #datepicker2 > div > table > tbody > tr:nth-child(5) > td:nth-child(6) > a
        # x=driver.find_element_by_css_selector('#datepicker2 > div > table')
        #datepicker2 > div > table > tbody > tr:nth-child(5) > 
        # submit=driver.find_element_by_css_selector('#date-opener2')


        time.sleep(2)
        confirm=driver.find_element_by_xpath('//*[@id="search-btn-expand-bot"]')
        time.sleep(2)
        confirm.click()
        
        ur=driver.current_url
        
        return(ur)
        # 

