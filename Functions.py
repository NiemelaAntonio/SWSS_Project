from datetime import datetime, timedelta
from swmfpy.web import get_omni_data
import matplotlib.dates as mdates
from matplotlib import dates
import matplotlib.pyplot as plt
import numpy as np

def Download_Data_omni(start_time,end_time):
    '''Done by Antonio
    This is the donwload data function
    __________________________________________
    Both dates should be in datetime format
    '''
    data       = get_omni_data(start_time,end_time)
    return data


def Look_Min(data):
    '''Done by Antonio
    _______________
    This is the function that would select the minimum of the data provided
    _______________
    
    
    ''' 
    Min = np.nanmin(data['sym_h'])
    print(Min)
    for i in range(len(data['sym_h'])):
        if data['sym_h'][i] == Min:
            print(data['times'][i])
            Time_of_min = data['times'][i]
    return Min, Time_of_min