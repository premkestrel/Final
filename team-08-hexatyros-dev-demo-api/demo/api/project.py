# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 14:13:01 2020

@author: keerthika02.TRN
"""
from enum_p import Status
#from projectType import ProjectType
from enum_p import ProjectType
class Project:
    def __init__(self,p_id,p_type,duration):
        self.project_id=p_id
        self.project_type=ProjectType[p_type]
        self.status=Status.notStarted
        self.duration=duration
        self.employees_allocated=[]
        self.team_size=None
        
    #Method to update the status of the project
    def updateStatus(self,status):
        self.status=status
        
    #Allocating Project to employee
    def allocate(self,e_id):
        self.employees_allocated.append(e_id)
    

