# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 16:04:15 2020

@author: keerthika02.TRN
"""
from client import Client
import random
class Situation:
    
    #list of situation
    list_situation=[
                    Client('web',58,5,50000),
                    Client('web',48,5,60000),
                    Client('web',38,5,40000),
                    Client('web',50,5,45000),
                    Client('web',40,5,55000),
                    Client('web',38,5,58000),
                    Client('web',48,5,54000),
                    Client('app',58,5,56000),
                    Client('app',88,5,59000),
                    Client('app',68,5,58000),
                    Client('app',78,5,58000),
                    Client('app',98,5,55000),
                    Client('app',48,5,52000),
                    Client('app',88,5,51000),
                    Client('VR',88,5,80000),
                    Client('VR',78,5,90000),
                    Client('VR',58,5,90000),
                    Client('VR',48,5,98000),
                    Client('VR',38,5,100000),
                    Client('VR',38,5,200000)
        
    ]
    
    
    #Randomly giving situation to the player
    @staticmethod
    def getSituation():
        return Situation.list_situation[random.randint(0,19)]
        
#print(situation.getSituation().getDetails())