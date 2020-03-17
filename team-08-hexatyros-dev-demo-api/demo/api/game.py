# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 14:41:02 2020

@author: keerthika02.TRN
"""
from enum_p import Feelings
from employee import Employee
import copy

#List of Employees in the Management
list_employee=[
         Employee('John',['html','css','java','c#','A-Frame']),
         Employee('Harry',['java','c#','Babylon']),
         Employee('James',['A-Frame','Babylon']),
         Employee('Mark',['html','css','java','c#','A-Frame','Babylon']),
         Employee('Mary',['html','css','bootstrap','kotlin','java']),
         Employee('Jeba',['bootstrap','kotlin','java','c#','A-Frame','Babylon']),
         Employee('Kivi',['bootstrap','kotlin','java','c#','A-Frame','Babylon']),
         Employee('puppu',['html','css','bootstrap','A-Frame','Babylon']),
         Employee('Aparna',['html','Babylon']),
         Employee('Jothi',['html','A-Frame','Babylon']),
         Employee('Kali',['html','c#','A-Frame','Babylon']),
         Employee('madhu',['html','css','bootstrap','kotlin','java','c#','A-Frame','Babylon']),
         Employee('bala',['kotlin','java','c#','A-Frame','Babylon']),
         Employee('Ravi',['html','c#','A-Frame','Babylon']),
         Employee('Abi',['html','css','bootstrap','c#','A-Frame','Babylon']),
         Employee('Tanu',['html','css','c#','A-Frame','Babylon']),
         Employee('prabha',['java','c#','A-Frame','Babylon'])
        ]

#print the employee Id
def getEmployee(e_id):
    for i in list_employee:
        if i.e_id==int(e_id):
            return copy.copy(i)
    return False

def changeEmployee_Feeling(e_id,feelings):
    for i in list_employee:
        if i.e_id==int(e_id):
            i.changeFeelings(Feelings.happy)
    
def Allocation(e_id,p_id):
     for i in list_employee:
        if i.e_id==int(e_id):
            return i.allocation(p_id)
    
