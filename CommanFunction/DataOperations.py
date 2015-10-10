#-*-coding=utf-8
'''
Created on 2015-8-31

@author: zhao
'''
import  xml.dom.minidom

class DataOperation(object):
    '''
    classdocs
    '''
    
    def __init__(self,filename):
        global dom
        dom=xml.dom.minidom.parse("../TestData/"+filename)

    def readxml(self,tagname,):
        
        root=dom.documentElement
        node=root.getElementsByTagName(tagname)
        tdata=node[0].firstChild.data
        return tdata
        