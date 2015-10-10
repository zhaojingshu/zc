#-*-coding=utf-8
'''
Created on 2015-8-31

@author: zhao
'''
from CommanFunction.WebDriverHelp import WebDriverHelp 
from selenium.webdriver.common.action_chains import ActionChains
import time
from CommanFunction.DataOperations import DataOperation

class Operation(object):
    '''
    classdocs
    '''


    def login(self, user,password):
        '''
        Constructor
        '''
        
        WebDriverHelp().clickoperate("byxpath","//div[@class='mainInnerBox']/div[1]/a[1]")
        time.sleep(5)
        WebDriverHelp().inputvalue("byname", "username",user)
        WebDriverHelp().inputvalue("byname", "user_pwd",password)
        WebDriverHelp().clickoperate("byid","login-btn")
        time.sleep(5)
#        WebDriverHelp().asserteq(DataOperation("Testcase_QT_Login.xml").readxml( "value"), DataOperation("Testcase_QT_Login.xml").readxml( "username"))
    def logout(self):
        ele=WebDriverHelp().findele("byxpath","//div[@class='siteHCountBox']/a")
        WebDriverHelp().chain(ele)
        WebDriverHelp().clickoperate("bylinktext","退出")
        
    
        
        