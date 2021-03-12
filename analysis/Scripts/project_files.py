{
 "cells": [],
 "metadata": {},
 "nbformat": 4,
 "nbformat_minor": 5
}

#line 22

import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt


#line 30

def load_and_process(url_or_path_to_csv_file):
    
    
    df = (pd.read_csv(url_or_path_to_csv_file)
          .drop(columns = ['DIVERTED','CANCELLED', 'CANCELLATION_REASON', 'AIR_SYSTEM_DELAY', 'SECURITY_DELAY','AIRLINE_DELAY', 'LATE_AIRCRAFT_DELAY','WEATHER_DELAY','Unamed: 31'])
          .dropna(axis = 0)
          .rename(columns = {"WHEELS_OFF" : "GATE_TO_TAKEOFF"}))
    return df


def displot(df):
    sns.displot(df['DAY'], kde=False, bins=31).set_title('number of flights on days during the month')
    
    
def displot2(df):
    sns.displot(df['AIRLINE'], kde=False, bins=13).set_title('amount of flights per airline')
    
    
def displot3(df):
    sns.displot(df['ORIGIN_AIRPORT'], kde=False, bins=322).set_title('departing flights')
    
    
def barplot(df):
    sns.barplot(y = 'DELAYED_OR_NOT', data =df).set_title('number of flights delayed versus on time')