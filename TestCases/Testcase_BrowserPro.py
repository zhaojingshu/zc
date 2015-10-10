#-*-coding=utf-8
'''
Created on 2015-9-9

@author: zhao
'''
import unittest,time
from CommanFunction.WebDriverHelp import WebDriverHelp 
from CommanFunction.QT_Operations import Operation

class TestBrowser(unittest.TestCase):


    def setUp(self):
        WebDriverHelp("open","firefox","local").setup("http://www.zhongchou.com")


    def tearDown(self):
        WebDriverHelp().teardown()


    def testBrowser(self):
        Operation().login("18601152182","infra1234")
        WebDriverHelp().clickoperate("byxpath","//div[@class='indexZCWrap'][2]/div/a")
        time.sleep(5)
        WebDriverHelp().switchre("window","众筹网-众筹中项目", "")
        WebDriverHelp().clickoperate("byxpath","//a[@class='normalPage'][2]")
        time.sleep(5)
        WebDriverHelp().switchre("window", "众筹网-众筹中项目_第3页","")
        Operation().logout()



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()