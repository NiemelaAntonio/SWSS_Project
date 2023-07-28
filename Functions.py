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
    INPUT  --> Whole data
    OUTPUT --> Min value and time of this min value
    
    ''' 
    Min = np.nanmin(data['sym_h'])                  # Numpy function that ignores nan values and looks for the min in a range
    print(Min)                                      # This is just for trial
    for i in range(len(data['sym_h'])):             # Indexing the data
        if data['sym_h'][i] == Min:                 # When the data is equal to the min, it does something
            print(data['times'][i])                 # This is for trial
            Time_of_min = data['times'][i]          # This is the time of the minimum
    return Min, Time_of_min                         # Function returns the min value found and the time of the min


def Time_Gap(start_time):
    """Done by Antonio
    
    This should be the function that calculates the time gap betweeen storms
    INPUT : start_time = list of <datetime.datetime>
    OUTPUT: time_gap   = list of <datetime.timedelta>
    """ 
    time_gap = []
    for index in range(len(start_time)):
        time_gap.append(start_time[i]-start_time[i-1])
    return time_gap