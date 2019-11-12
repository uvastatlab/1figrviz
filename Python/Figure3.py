#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 14:47:42 2019

@author: ep9k
"""

import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter
import matplotlib.patches as mpatches

import sandbox as sb

filename = '1figr_U_Virginia_Original (1) (1).xlsx'
your_institution = 'UVA'


def figure3c():

    data = pd.read_excel(filename, sheet_name='Journals per Provider', skiprows=8)

    big7 = ['Elsevier', 'Sage', 'Springer', 'Taylor & Francis', 'Wiley', 'Elsevier Freedom', 'Elsevier Subscribed']

    stats_by_provider = []
    
    for provider_name in big7:
        
        subset_by_provider = data.loc[data['Provider'] == provider_name]

        journals_data = subset_by_provider.groupby('Journal', as_index=False).sum().values.tolist()
        
        for i in journals_data:
            if i[0] == provider_name:
                jr1_total = i[4]
                jr5_total = i[5]
                stats_by_provider.append((i[0], jr1_total, jr5_total))    #i[0] = name of provider

    
    elsevier_freedom_collection = sb.make_freedom_collection_provider()

    elsevier_freedom_jr5_downloads = elsevier_freedom_collection['Downloads JR5 2017 in 2017'].sum()
    elsevier_freedom_jr1_downloads = elsevier_freedom_collection['Downloads JR1 2017'].sum()
    
    stats_by_provider.append(('Elsevier Freedom', elsevier_freedom_jr1_downloads, elsevier_freedom_jr5_downloads))
    
    
    elsevier_subscribed_titles = sb.make_elsevier_subscribed_titles_provider()
    
    elsevier_subscribed_jr5_downloads = elsevier_subscribed_titles['Downloads JR5 2017 in 2017'].sum()
    elsevier_subscribed_jr1_downloads = elsevier_subscribed_titles['Downloads JR1 2017'].sum()
    
    stats_by_provider.append(('Elsevier Subscribed', elsevier_subscribed_jr1_downloads, elsevier_subscribed_jr5_downloads))

    
    #reads cost data per provider from the following supplementary file
    cost_data = pd.read_excel('1figr_U_Virginia_edit_Supp_Data.xlsx')
    
    cost_per_provider = cost_data.groupby(['Package'], as_index=False).sum().values.tolist()
    
    cost_per_jr1_download = []
    
    for i in stats_by_provider:
        for x in cost_per_provider:
            if i[0] == x[0]:
                cost_per_jr1_download.append(x[1]/i[1])
#                cost_per_jr1_download.append((i[0], x[1]/i[1]))
#                print((i[0], x[1], x[1]/i[1], x[1]/i[2]))


    #make plot        
    mpl.rcParams['ytick.major.width'] = 1
    mpl.rcParams['xtick.major.width'] = 1
    plt.figure(num=None, figsize=(8,8))
    plt.suptitle(f'Cost per Download, all 2017 downloads (JR1)')
    plot = plt.bar(big7, cost_per_jr1_download, width=.8, color='green')   
    plt.ylabel('Cost (dollars)')
    plt.ylim(0, 8)  #changes top and bottom limit of y axis in plot
    plt.xticks(rotation=90)

    for i in plot:
        score = i.get_height()
        
        plt.text(i.get_x() + i.get_width()/2, 
                 1.05 * score, 
                 '${:,.2f}'.format(score),
                 ha='center',
                 va='bottom')

#    plt.show()        
    plt.savefig('test.jpg', bbox_inches='tight')      #saves image in working directory


    
    
    
    
figure3c()