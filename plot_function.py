#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import matplotlib.pyplot as plt
save_path = "/Users/shreejankhanal/Documents/SWSS_Project/symh_al_plot.png"
def plot_and_save(symh_index, al_index, time_index, save_path):
    # Create the plot
    #symh = data['sym_h']
    #al = data['al']
    #time = data['times']
    
    fig, axs = plt.subplots(2, 1, figsize=(16, 8), sharex=True)
#plotting
    axs[0].plot(time_index, symh_index, color='tab:cyan', label='SYM_H')
    axs[0].set_ylabel('SYM/H (nT)', fontsize=16)
    axs[0].set_xlabel('{}'.format(time_index), fontsize=16)
    axs[0].legend(fontsize=10)
    axs[0].grid(True, linestyle='--', alpha=0.5)
    #axs[0].set_xlim(x_min, x_max)
    axs[0].xaxis.set_major_locator(mdates.dayLocator())
    axs[0].xaxis.set_major_formatter(mdates.DateFormatter('%y-%m-%d'))
    axs[0].set_title(fontsize = 15)

    axs[1].plot(time_index, al_index, color='tab:green', label='AL')
    axs[1].set_ylabel('AL (nT)', fontsize=16)
    axs[1].set_xlabel('{}'.format(time_index), fontsize=16)
    axs[1].legend(fontsize=10)
    axs[1].grid(True, linestyle='--', alpha=0.5)
    #axs[1].set_xlim(x_min, x_max)
    axs[1].xaxis.set_major_locator(mdates.dayLocator())
    axs[1].xaxis.set_major_formatter(mdates.DateFormatter('%y-%m-%d'))
    axs[1].set_title(fontsize = 15)
                                                          
    plt.suptitle('Solar Magnetic Field Variation', fontsize=16)
    plt.tight_layout()
    #save_path = "/Users/shreejankhanal/Documents/SWSS_Project/symh_al_plot.png"
   
    
    plt.savefig(save_path, bbox_inches='tight')
    plt.close()
    print(f"Plot saved to {os.path.abspath(save_path)}")
    plt.show()

    return 

