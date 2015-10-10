# coding=UTF-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains

import unittest, time, re
'''
Created on 2015-8-31

@author: zhao
'''

class WebDriverHelp(object):
    '''
    classdocs
    '''


    def __init__(self, atype='close',btype='firefox',ctype='local'):
        '''
        Constructor
        '''
        global driver
        if (atype=='open'):
            if(btype=='firefox'):
                if(ctype=='local'): 
                    driver = webdriver.Firefox()
                elif(ctype=='notlocal'):
                    driver=webdriver.Remote("http://192.167.3.61:4444/wd/hub",webdriver.DesiredCapabilities.FIREFOX)
            elif(btype=='chrome'):
                if(ctype=='local'): 
                    driver = webdriver.Chrome()
                elif(ctype=='notlocal'):
                    driver=webdriver.Remote("http://192.167.3.61:4444/wd/hub",webdriver.DesiredCapabilities.CHROME)
            elif(btype=='ie'):
                 if(ctype=='local'): 
                    driver = webdriver.Ie()
                 elif(ctype=='notlocal'):
                    driver=webdriver.Remote("http://192.167.3.61:4444/wd/hub",webdriver.DesiredCapabilities.INTERNETEXPLORER)
        self.driver=driver
    def setup(self,url):
        
        self.driver.get(url)
    def teardown(self):
        self.driver.quit()
    def inputvalue(self,findby,proper,value):
        if(findby=="byid"):
            self.driver.find_element_by_id(proper).send_keys(value)
        elif(findby=="byname"):
            self.driver.find_element_by_name(proper).send_keys(value)
        elif(findby=="byclassname"):
            self.driver.find_element_by_class_name(proper).send_keys(value)
    
    def clickoperate(self,findby,proper):
        if(findby=="byid"):
            self.driver.find_element_by_id(proper).click()
        elif(findby=="byname"):
            self.driver.find_element_by_name(proper).click()
        elif(findby=="byclassname"):
            self.driver.find_element_by_class_name(proper).click()
        elif(findby=="bylinktext"):
            self.driver.find_element_by_link_text(proper).click()
        elif(findby=="byxpath"):
            self.driver.find_element_by_xpath(proper).click()
        elif(findby=="bycss"):
            self.driver.find_element_by_css_selector(proper).click()
        elif(findby=="bytag"):
            return self.driver.find_element_by_tag_name(proper)
  
    def gettext(self,findby,proper):
        if(findby=="byid"):
            return self.driver.find_element_by_id(proper).text
        elif(findby=="byname"):
            return self.driver.find_element_by_name(proper).text
        elif(findby=="byclassname"):
            return self.driver.find_element_by_class_name(proper).text
        elif(findby=="byxpath"):
            return self.driver.find_element_by_xpath(proper).text       
    def findele(self,findby,proper):
        if(findby=="byid"):
            return self.driver.find_element_by_id(proper)
        elif(findby=="byname"):
            return self.driver.find_element_by_name(proper)
        elif(findby=="byclassname"):
            return self.driver.find_element_by_class_name(proper)
        elif(findby=="bylinktext"):
            return self.driver.find_element_by_link_text(proper)
        elif(findby=="byxpath"):
            return self.driver.find_element_by_xpath(proper)
        elif(findby=="bycss"):
            return self.driver.find_element_by_css_selector(proper)
        elif(findby=="bytag"):
            return self.driver.find_element_by_tag_name(proper)
    def switchre(self,ttype,tchar,fvalue=None):
#        self.driver.get(turl)
        if(ttype=="iframe"):
            self.driver.switch_to_frame(fvalue)
        elif(ttype=="window"):    
            return self.driver.switch_to_window(self.driver.window_handles[-1])
            
#            print (self.driver.title)
    def geturl(self,turl):
        self.driver.get(turl)
    
    def chain(self,ele):
        ActionChains(self.driver).move_to_element(ele).perform()  
    

    
    def promptcon(self):
        self.driver.switch_to_alert().accept()
          
        
        
        
                    
            