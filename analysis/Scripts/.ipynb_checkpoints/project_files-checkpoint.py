{
 "cells": [],
 "metadata": {},
 "nbformat": 4,
 "nbformat_minor": 5
}

#In[3]

import pandas as pd
import seaborn as sns 


project_files1 = pd.read_csv('../../data/raw/project files.csv')


#In[5]

def load_and_process(url_or_path_to_csv_file):
    
    df = (pd.read_csv(url_or_path_to_csv_file)
          .drop(columns = ['DIVERTED','CANCELLED', 'CANCELLATION_REASON', 'AIR_SYSTEM_DELAY', 'SECURITY_DELAY','AIRLINE_DELAY', 'LATE_AIRCRAFT_DELAY','WEATHER_DELAY'])
          .dropna(axis = 0)
          .rename(columns = {"WHEELS_OFF" : "GATE_TO_TAKEOFF"}))
    return df

#In[10]

def group_by(df):
    return df.groupby('DELAYED_OR_NOT', as_index = False).mean()



def displot(df):
    sns.displot(df['DAY'], kde=True, bins=31)
    
#In[11]
    
    
def displot2(df):
    sns.displot(df['AIRLINE'], kde=False, bins=13)
    
#In[12]
    
    
def displot3(df):
    sns.displot(df['ORIGIN_AIRPORT'], kde=False, bins=322)
    
#In[9]
    
def barplot(df):
    sns.barplot(y = count, x = 'DELAYED_OR_NOT', data =df).set_title('number of flights delayed versus on time')
    
#[]
    
def barplot2(df):
    sns.barplot(y = 'AIRLINE', x = 'DELAYED_OR_NOT', data =df).set_title('Airlines that experienced most delays')
   

def stripplot(df):
    sns.stripplot(y = 'DISTANCE', x ='DELAYED_OR_NOT', data = df).set_title('Flight distance and delays')
