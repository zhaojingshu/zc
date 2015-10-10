
#-*-coding=utf-8

'''
Created on 2015-8-31

@author: zhao
'''
import unittest,time
from CommanFunction.WebDriverHelp import WebDriverHelp 
import  xml.dom.minidom
from CommanFunction.DataOperations import DataOperation
from CommanFunction.QT_Operations import Operation

class TestLogin(unittest.TestCase):


    def setUp(self):
        WebDriverHelp("open","firefox","local").setup("http://www.zhongchou.com")

    def tearDown(self):
        WebDriverHelp().teardown()
        
    def testLogin(self):
        dataoper=DataOperation("Testcase_QT_Login.xml")
        Operation().login("18601152182", "infra1234")
        self.assertEqual(WebDriverHelp().gettext("byxpath",dataoper.readxml("checkpoint")),dataoper.readxml( "value"))
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
    