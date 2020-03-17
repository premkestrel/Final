# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 11:44:07 2020

@author: chandra05.TRN
"""


import pandas as pd
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.model_selection import train_test_split




class Algoritham:
    
    
   
    def getResult(input_list):
        
        df = pd.read_excel(r'C:\Users\keerthika02.TRN\Desktop\demo\team-08-hexatyros\demo\api\data_set.xlsx')
        #------------------------------------------------build and predict the value returned from model 
        x = df.iloc[:,0:29].values
        y = df.iloc[:,29].values
        x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.2)
        
        from sklearn.preprocessing import StandardScaler
        sc = StandardScaler()
        x_train = sc.fit_transform(x_train)
        x_test = sc.transform(x_test)
        
        model = Sequential()
        model.add(Dense(input_dim = 29,kernel_initializer="uniform" ,units=800,activation = 'relu'))
        model.add(Dense(units=500 ,kernel_initializer="uniform" ,activation = 'relu'))
        model.add(Dense(units=500 ,kernel_initializer="uniform" ,activation = 'relu'))
        model.add(Dense(units=500  ,kernel_initializer="uniform",activation = 'relu'))
        model.add(Dense(units=500  ,kernel_initializer="uniform",activation = 'relu'))
        model.add(Dense(units=600 ,kernel_initializer="uniform",activation = 'relu'))
        model.add(Dense(units= 1 ,kernel_initializer='uniform',activation = 'sigmoid'))
        model.compile(optimizer = 'adam',loss = 'binary_crossentropy', metrics = ['accuracy'])
        model.fit(x_train,y_train,epochs = 5) 
        inpv = sc.transform(np.reshape(input_list,(1,29)))
        val_loss,val_accuracy = model. evaluate(x_test,y_test)
        print('Accuracy %.2f'%(val_accuracy))
        y_pred=model.predict(inpv)
        y_pred = np.where(y_pred > 0.5,1,0)
        return y_pred
        
        
#        print(type(final_output))
        
        
#        print("final output"+final_output)
#        return final_output
        #final_output=model.predict(np.array(np.reshape((,))))
        #print(final_output)
        #return final_output
