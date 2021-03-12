{
 "cells": [],
 "metadata": {},
 "nbformat": 4,
 "nbformat_minor": 5
}

#line 22

import pandas as pd
import seaborn as sns

#line 30

def load_and_process(url_or_path_to_csv_file):
    
    
    df = (pd.read_csv(url_or_path_to_csv_file)
          .drop(columns = ['DIVERTED','CANCELLED', 'CANCELLATION_REASON', 'AIR_SYSTEM_DELAY', 'SECURITY_DELAY','AIRLINE_DELAY', 'LATE_AIRCRAFT_DELAY','WEATHER_DELAY'])
          .dropna(axis = 0)
          .rename(columns = {"WHEELS_OFF" : "GATE_TO_TAKEOFF"}))
    return df