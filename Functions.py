from datetime import datetime, timedelta
from swmfpy.web import get_omni_data
import matplotlib.dates as mdates
from matplotlib import dates
import matplotlib.pyplot as plt
def Download_Data_omni(start_time,end_time):
    '''
    This is the donwload data function
    __________________________________________
    Both dates should be in datetime format
    '''
    data       = get_omni_data(start_time,end_time)
    return data