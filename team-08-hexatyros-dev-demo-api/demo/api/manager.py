# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 11:18:31 2020

@author: keerthika02.TRN
"""

#from ProjectType import projectType
#from ProjectTypeWithTech import projectTypeWithTech
#from Client import client
from enum_p import Feelings,EcoSystem 
import copy

#from Client import client
class Manager:
    def __init__(self,patient_level):
        #print(project_type)
        #self.__project_type=project_type
        #self.__deadline=deadline
        #self.project=project()
        self.client_list=[]
        self.project_list=[]
        self.__patient_level=patient_level
        self.Ecosystem=EcoSystem.normal
        self.__feelings=Feelings.normal
    
    #Method to add new project to the manager,client1-->object of the client
    def addProject(self,client1):
        self.project_list.append(copy.copy(client1.project))
        self.client_list.append(client1)
        
    def ecoSystemChange(self,name):
        #print(name)
        self.EcoSystem=name.value
    def changeFeelings(self,feeling):
        self.__feelings=feeling
    def findProject(self,p_id):
        for i in self.project_list:
            if i.project_id==p_id:
                return copy.copy(i)
    def updateProjectStatus(self,p_id,status):
        project=self.findProject(p_id)
        project.updateStatus(status)
        
    #swaping the employee in the middle of project  progress
    def swapingEmployeeWithOtherProject(self,emp1,emp2):
        p_id=emp1.allocatedProjectId
        emp1.projectChange(emp2.allocatedProjectId)
        emp2.projectChange(p_id)
        
    def completedProject(self,p_id):
        projectCompleted=self.findProject(p_id)
        self.project_list.remove(projectCompleted)
   
#e=Manager(projectType.web,"","","")
#print(e._Manager__project_type)
#e.EcoSystemChange(ecoSystem.Holiday)
#print(e.EcoSystem)
        