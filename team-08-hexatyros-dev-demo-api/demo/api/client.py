# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from enum_p import Feelings
from enum_p import ProjectExpand
from project import Project
class Client:
    Id_generator=1000
    def __init__(self,project_type,deadline,patient_level,cost):
        #print("Inside")
        self.project=Project(Client.Id_generator,project_type,deadline)
        self.projectExp=project_type
        self.__patient_level=patient_level
        self.__cost=cost
        self.__feelings=Feelings.normal
        Client.Id_generator+=1
    
    #Fetching the details of client as a String
    def getDetails(self):
        
        return "The Project Type is: "+ProjectExpand[self.projectExp].value+" and the deadline is  "+str(self.project.duration)+". cost of the project is "+str(self.__cost)+". Patient Level is "+str(self.__patient_level)
    
    
    def changeFeelings(self,feeling):
        self.__feelings=feeling
        return feeling
    
       
        
        
