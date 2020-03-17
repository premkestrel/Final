# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 16:58:16 2020

@author: pothulathrimurt.TRN
"""

from enum import Enum

class ProjectExpand(Enum):
    web="Web Application"
    app="Mobile Application"
    VR="Vritual Reality"

class Feelings(Enum):
    sad=-1
    normal=0
    ok=1
    happy=2

class ProjectType(Enum):
    web={'html','css','bootstrap'}
    app={'kotlin','java','c#'}
    VR={'A-Frame','Babylon'}

class EcoSystem(Enum):
    normal=0
    holiday=1
    weather=2
    personal=3
    externalFactor=4

class Status(Enum):
    notStarted=-1
    inProgress=0
    completed=1