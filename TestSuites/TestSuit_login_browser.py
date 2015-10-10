#-*-coding=utf-8
'''
Created on 2015-9-10

@author: zhao
'''
import unittest
from TestCases.Testcase_QT_Login import TestLogin 
from TestCases.Testcase_BrowserPro import TestBrowser

#class Test(unittest.TestCase):

#    def testName(self):
#        suit=unittest.TestSuite()
#        suit.addTest(TestBrowser,TestLogin)
        
#        return suit

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    #unittest.main()
#    suite1 = unittest.TestLoader().loadTestsFromTestCase(TestLogin)  
#    suite2 = unittest.TestLoader().loadTestsFromTestCase(TestBrowser)  
#    suite = unittest.TestSuite([suite1, suite2])  
#    unittest.TextTestRunner(verbosity=2).run(suite) 
    suit=unittest.TestSuite()
    suit.addTest(TestLogin("testLogin"))
#    suit.addTest(TestBrowser("testBrowser"))
    unittest.TextTestRunner().run(suit) 