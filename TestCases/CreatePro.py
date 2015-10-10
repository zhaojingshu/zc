#-*-coding=utf-8
'''
Created on 2015-9-14

@author: zhao
'''
import unittest,time
from CommanFunction.WebDriverHelp import WebDriverHelp 
from CommanFunction.QT_Operations import Operation
from CommanFunction.DataOperations import DataOperation
from selenium.webdriver.support.ui import Select

class Test(unittest.TestCase):
   

    def setUp(self):
        WebDriverHelp("open","firefox","local").setup("http://www.zhongchou.com")


    def tearDown(self):
        WebDriverHelp().teardown()


    def testCreate(self):
#        Operation().login("18601152182","infra1234")
        Operation().login(DataOperation("Testcase_QT_Login.xml").readxml( "username"),DataOperation("Testcase_QT_Login.xml").readxml("password"))
        WebDriverHelp().clickoperate("bylinktext","发起众筹")
        time.sleep(10)
        WebDriverHelp().clickoperate("bylinktext","立即创建")
        time.sleep(10)
       
        select = Select(WebDriverHelp().findele("bytag","select"))
        
        select.select_by_visible_text("北京")
        time.sleep(100)
        WebDriverHelp().promptcon()
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()