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

import reusable_functions as rf

#Change these global variables to your corresponding filename and institution name
filename = '1figr_U_Virginia_Original (1) (1).xlsx'
your_institution = 'UVA'


def figure3a():
    """Using cost data per provider, plots cost per jr1 download for each provider. Divides total package
    price by total number of JR1 downloads. JR1 downloads are all years' downloads in current year.
    Fix this to incorporate the usual csv reading the data instead of hard coded values
    
    Chart Type: Dot Plot/Scatter Plot
    Y-Axis: Provider name
    Y-Axis Data Source: Original 1Figr Dataset
    
    X-Axis: Cost per download
    X-Axis Data Source: Original 1Figr Dataset
    """

    data = pd.read_excel(filename, sheet_name='Journals per Provider', skiprows=8)


    #reads cost data per provider from the following supplementary file
    cost_data = pd.read_excel('1figr_U_Virginia_edit_Supp_Data.xlsx')
    cost_per_provider = cost_data.groupby(['Package'], as_index=False).sum().values.tolist()
    
    big5 = ['Elsevier', 'Sage', 'Springer', 'Taylor & Francis', 'Wiley']
    
    stats_by_provider = []
    
    for provider_name in big5:
        for cost in cost_per_provider:
            if cost[0] == provider_name:
                provider_cost = cost[1]
                
        subset_by_provider = data.loc[data['Provider'] == provider_name]

        journals_data = subset_by_provider.groupby('Journal', as_index=False).sum().values.tolist()
        
        for i in journals_data:
            if i[0] == provider_name:
                jr1_total = i[4]

        cost_per_download = provider_cost/jr1_total

        stats_by_provider.append((provider_name, cost_per_download))
        
        
    providers = [x[0] for x in stats_by_provider]
    cost = [x[1] for x in stats_by_provider]
    
    
    plt.figure(num=None, figsize=(8,8))
    plt.suptitle('Big5 Providers Cost Per JR1 Download (for 2017)\n (Package Cost / # of JR1 Downloads)')
    plt.ylabel('Dollars')
                 
    plot = plt.bar(providers, cost, color='green')
    
    for i in plot:
        score = i.get_height()
        
        plt.text(i.get_x() + i.get_width()/2., 
                 1.01 * score, 
                 '${:,.2f}'.format(score),
                 ha='center',
                 va='bottom')


def figure3b():
    """Using cost data per provider, plots cost per jr5 download for each provider. Divides total package
    price by total number of JR5 downloads. JR5 downloads are all years' downloads in current year.
    Fix this to incorporate the usual csv reading the data instead of hard coded values
    
    Chart Type: Dot Plot/Scatter Plot
    Y-Axis: Provider name
    Y-Axis Data Source: Original 1Figr Dataset
    
    X-Axis: Cost per download
    X-Axis Data Source: Original 1Figr Dataset
    """

    data = pd.read_excel(filename, sheet_name='Journals per Provider', skiprows=8)


    #reads cost data per provider from the following supplementary file
    cost_data = pd.read_excel('1figr_U_Virginia_edit_Supp_Data.xlsx')
    cost_per_provider = cost_data.groupby(['Package'], as_index=False).sum().values.tolist()
    
    big5 = ['Elsevier', 'Sage', 'Springer', 'Taylor & Francis', 'Wiley']
    
    stats_by_provider = []
    
    for provider_name in big5:
        for cost in cost_per_provider:
            if cost[0] == provider_name:
                provider_cost = cost[1]
                
        subset_by_provider = data.loc[data['Provider'] == provider_name]

        journals_data = subset_by_provider.groupby('Journal', as_index=False).sum().values.tolist()
        
        for i in journals_data:
            if i[0] == provider_name:
                jr5_total = i[5]

        cost_per_download = provider_cost/jr5_total

        stats_by_provider.append((provider_name, cost_per_download))
        
        
    providers = [x[0] for x in stats_by_provider]
    cost = [x[1] for x in stats_by_provider]
    
    
    plt.figure(num=None, figsize=(8,8))
    plt.suptitle('Big5 Providers Cost Per JR1 Download (for 2017)\n (Package Cost / # of JR1 Downloads)')
    plt.ylabel('Dollars')
                 
    plot = plt.bar(providers, cost, color='green')
    
    for i in plot:
        score = i.get_height()
        
        plt.text(i.get_x() + i.get_width()/2., 
                 1.01 * score, 
                 '${:,.2f}'.format(score),
                 ha='center',
                 va='bottom')


def figure3c():
    """Represents cost per JR1 download by provider
    Reads in cost data from supplementary file for each provider
    Cost per JR1 download = total cost per provider / # of JR1 downloads by provider
    Represented as "big 7" providers, including Elsevier Freedom and Elsevier Subscribed titles
    
    
    Chart Type: Bar Graph
    Y-Axis: Cost (in dollars) per JR1 Download
    Y-Axis Data Source: Original 1Figr Dataset, Journals Per Provider, Provider
                        1figr_U_Virginia_edit_Supp_Data, Total cost for 2017
    X-Axis: Provider Name
    X-Axis Data Source: Original 1Figr Dataset, Journals Per Provider, Provider
                        1figr_U_Virginia_edit_Supp_Data, Total cost for 2017
    """
    
    data = pd.read_excel(filename, sheet_name='Journals per Provider', skiprows=8)


    big7 = ['Elsevier', 'Sage', 'Springer', 'Taylor & Francis', 'Wiley', 'Elsevier Freedom', 'Elsevier Subscribed']

    stats_by_provider = []
    
    for provider_name in big7:
        
        subset_by_provider = data.loc[data['Provider'] == provider_name]

        journals_data = subset_by_provider.groupby('Journal', as_index=False).sum().values.tolist()
        
        for i in journals_data:
            if i[0] == provider_name:
                jr1_total = i[4]
                stats_by_provider.append((i[0], jr1_total))    #i[0] = name of provider

    #calculate downloads for elsevier freedom collection
    elsevier_freedom_collection = rf.make_freedom_collection_provider()
    elsevier_freedom_jr1_downloads = elsevier_freedom_collection['Downloads JR1 2017'].sum()
    stats_by_provider.append(('Elsevier Freedom', elsevier_freedom_jr1_downloads))
    
    #calculate downloads for elsevier subscribed titles
    elsevier_subscribed_titles = rf.make_elsevier_subscribed_titles_provider()
    elsevier_subscribed_jr1_downloads = elsevier_subscribed_titles['Downloads JR1 2017'].sum()
    stats_by_provider.append(('Elsevier Subscribed', elsevier_subscribed_jr1_downloads))
    
    #reads cost data per provider from the following supplementary file
    cost_data = pd.read_excel('1figr_U_Virginia_edit_Supp_Data.xlsx')
    cost_per_provider = cost_data.groupby(['Package'], as_index=False).sum().values.tolist()
    
    cost_per_jr1_download = []
    
    for stat in stats_by_provider:
        for cost in cost_per_provider:
            if stat[0] == cost[0]:             #first element in each item is the name
                cost_per_jr1_download.append(cost[1]/stat[1])


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
#    plt.savefig('test.jpg', bbox_inches='tight')      #saves image in working directory



def figure3d():
    """Represents cost per JR5 download by provider
    Reads in cost data from supplementary file for each provider
    Cost per JR1 download = total cost per provider / # of JR5 downloads by provider
    Represented as "big 7" providers, including Elsevier Freedom and Elsevier Subscribed titles
    
    Chart Type: Bar Graph
    Y-Axis: Cost (in dollars) per JR5 Download
    Y-Axis Data Source: Original 1Figr Dataset, Journals Per Provider, Provider
                        1figr_U_Virginia_edit_Supp_Data, Total cost for 2017
    X-Axis: Provider Name
    X-Axis Data Source: Original 1Figr Dataset, Journals Per Provider, Provider
                        1figr_U_Virginia_edit_Supp_Data, Total cost for 2017
    """
    
    data = pd.read_excel(filename, sheet_name='Journals per Provider', skiprows=8)


    big7 = ['Elsevier', 'Sage', 'Springer', 'Taylor & Francis', 'Wiley', 'Elsevier Freedom', 'Elsevier Subscribed']

    stats_by_provider = []
    
    for provider_name in big7:
        
        subset_by_provider = data.loc[data['Provider'] == provider_name]

        journals_data = subset_by_provider.groupby('Journal', as_index=False).sum().values.tolist()
        
        for i in journals_data:
            if i[0] == provider_name:
                jr5_total = i[5]
                stats_by_provider.append((i[0], jr5_total))    #i[0] = name of provider

    elsevier_freedom_collection = rf.make_freedom_collection_provider()

    elsevier_freedom_jr5_downloads = elsevier_freedom_collection['Downloads JR5 2017 in 2017'].sum()
    
    stats_by_provider.append(('Elsevier Freedom', elsevier_freedom_jr5_downloads))
    
    
    elsevier_subscribed_titles = rf.make_elsevier_subscribed_titles_provider()
    
    elsevier_subscribed_jr5_downloads = elsevier_subscribed_titles['Downloads JR5 2017 in 2017'].sum()
    
    stats_by_provider.append(('Elsevier Subscribed', elsevier_subscribed_jr5_downloads))
    
    #reads cost data per provider from the following supplementary file
    cost_data = pd.read_excel('1figr_U_Virginia_edit_Supp_Data.xlsx')
    
    cost_per_provider = cost_data.groupby(['Package'], as_index=False).sum().values.tolist()
    
    cost_per_jr5_download = []
    
    for stat in stats_by_provider:
        for cost in cost_per_provider:
            if stat[0] == cost[0]:             #first element in each item is the name
                cost_per_jr5_download.append(cost[1]/stat[1])
                
                
    #make plot        
    mpl.rcParams['ytick.major.width'] = 1
    mpl.rcParams['xtick.major.width'] = 1
    plt.figure(num=None, figsize=(8,8))
    plt.suptitle(f'Cost per Download, current year 2017 downloads (JR5)')
    plot = plt.bar(big7, cost_per_jr5_download, width=.8, color='green')   
    plt.ylabel('Cost (dollars)')
    plt.ylim(0, 37)  #changes top and bottom limit of y axis in plot
    plt.xticks(rotation=90)

    for i in plot:
        score = i.get_height()
        
        plt.text(i.get_x() + i.get_width()/2, 
                 1.05 * score, 
                 '${:,.2f}'.format(score),
                 ha='center',
                 va='bottom')

#    plt.show()        
#    plt.savefig('test.jpg', bbox_inches='tight')      #saves image in working directory
