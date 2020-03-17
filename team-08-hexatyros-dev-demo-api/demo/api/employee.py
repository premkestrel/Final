# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 12:27:00 2020

@author: keerthika02.TRN
"""

from enum_p import EcoSystem
from enum_p import Feelings
class Employee:
    count=500
    def __init__(self,name,skills):
        self.e_id=Employee.count
        self.name=name
        self.skills=skills
        self.ecoSystem=EcoSystem.normal.name
        self.__feelings=Feelings.normal.name
        self.__isAllocated=False
        self.__allocatedProjectId=None
        Employee.count+=1
        
    def ecoSystemChange(self,name):
        #print(name)
        self.ecoSystem=name.value
        
    def changeFeelings(self,feeling):
        self.__feelings=feeling
     
    #allocation of employee to project with id(p_id)
    def allocation(self,p_id):
        if(not self.__isAllocated):
           self.__isAllocated=True
           self.__allocatedProjectId=p_id
           return True
        return False
   
    #changing of project in the middle of the progress
    def projectChange(self,p_id):
        self.__allocatedProjectId=p_id
        
    #changing the employee status to not allocated
    def projectCompleted(self):
        self.allocatedProjectId=None
        self.__isAllocated=False
        
    #Fetching the details of the employee in the String format
    def getDetails(self):
        skill="{"
        for i in self.skills.value:
            skill+=i+" "
        skill+="}"
            
        return "Employee Id  :  "+str(self.e_id)+"\nEmployee Name  : "+self.name+"\nSkills  :  "+skill+" \nAllocated  :  "+str(self.__isAllocated)