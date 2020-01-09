#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 11:15:35 2019

@author: ep9k
"""

import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter
import matplotlib.patches as mpatches


import reusable_functions as rf


def figure7e():
    """This is counting JR1 downloads by Domain for the subscribed titles and freedom collection providers
    
    Chart Type: Dot Plot/Scatter Plot
    Y-Axis: Domain
    Y-Axis Data Source: Original 1Figr Dataset, Journals Per Provider, Provider
                        Elsevier_2019, Subscribed Journal List 2019
    X-Axis: Number of JR1 Downloads
    X-Axis Data Source: Original 1Figr Dataset, Journals Per Provider, Provider
                        Elsevier_2019, Subscribed Journal List 2019
    """
   
    original_1figr_data = pd.read_excel('JournalsPerProvider.xls', skiprows=8)
    subscribed_titles_provider = rf.make_elsevier_subscribed_titles_provider()
    freedom_collection_provider = rf.make_freedom_collection_provider()
    
    unique_domains = original_1figr_data['Domain'].unique().tolist()
        
    for i in unique_domains:    #this drops the 'nan' column from the unique domains
        if type(i) == float:
            unique_domains.remove(i)
    unique_domains.sort()

    stats_by_domain = []
    
    #builds list of tuples containing (Domain name, # of subscribed titles JR1 downloads, # of Freedom titles downloads)
    for domain in unique_domains:

        subscribed_subset_by_domain = subscribed_titles_provider.loc[subscribed_titles_provider['Domain'] == domain]
        subscribed_jr1_downloads = subscribed_subset_by_domain['Downloads JR1 2017'].sum()

        freedom_subset_by_domain = freedom_collection_provider.loc[freedom_collection_provider['Domain'] == domain]
        freedom_jr1_downloads = freedom_subset_by_domain['Downloads JR1 2017'].sum()

        stats_by_domain.append((domain, subscribed_jr1_downloads, freedom_jr1_downloads))        
        

    #sorts domains by sum of total # of jr1 downloads
    arrangement = sorted(stats_by_domain, key=lambda x: (x[1] + x[2])) 

    #splitting elements of tuples in arrangement into lists so it is easier to plot
    domains_list = [i[0] for i in arrangement]
    subscribed_total = [i[1] for i in arrangement]
    freedom_total = [i[2] for i in arrangement]

    #make plot
    mpl.rcParams['ytick.major.width'] = 1
    mpl.rcParams['xtick.major.width'] = 1
    plt.figure(num=None, figsize=(8,8))
    plt.suptitle(f'JR1 downloads by Domain')

    plot = plt.scatter(subscribed_total, domains_list, color='blue')
    plot2 = plt.scatter(freedom_total, domains_list, color='orange')

    subscribed_legend_label = mpatches.Patch(color='blue', label='Elsevier Subscribed')
    freedom_legend_label = mpatches.Patch(color='orange', label='Elsevier Freedom')
    plt.xlabel('Number of JR1 Downloads')
    plt.legend(loc='lower right', handles=[subscribed_legend_label, freedom_legend_label])

        
def figure7f():
    """This is counting JR5 downloads by Domain for the subscribed titles and freedom collection providers
    
    Chart Type: Dot Plot/Scatter Plot
    Y-Axis: Domain
    Y-Axis Data Source: Original 1Figr Dataset, Journals Per Provider, Provider
                        Elsevier_2019, Subscribed Journal List 2019
    X-Axis: Number of JR5 Downloads
    X-Axis Data Source: Original 1Figr Dataset, Journals Per Provider, Provider
                        Elsevier_2019, Subscribed Journal List 2019
    """
    
    original_1figr_data = pd.read_excel('JournalsPerProvider.xls', skiprows=8)
    subscribed_titles_provider = rf.make_elsevier_subscribed_titles_provider()
    freedom_collection_provider = rf.make_freedom_collection_provider()
    
    unique_domains = original_1figr_data['Domain'].unique().tolist()
    
    for i in unique_domains:    #this drops the 'nan' column from the unique domains
        if type(i) == float:
            unique_domains.remove(i)
    unique_domains.sort()

    
    stats_by_domain = []
    
    #builds list of tuples containing (Domain name, # of subscribed titles JR5 downloads, # of Freedom titles downloads)
    for domain in unique_domains:

        subscribed_subset_by_domain = subscribed_titles_provider.loc[subscribed_titles_provider['Domain'] == domain]
        subscribed_jr5_downloads = subscribed_subset_by_domain['Downloads JR5 2017 in 2017'].sum()

        freedom_subset_by_domain = freedom_collection_provider.loc[freedom_collection_provider['Domain'] == domain]
        freedom_jr5_downloads = freedom_subset_by_domain['Downloads JR5 2017 in 2017'].sum()

        stats_by_domain.append((domain, subscribed_jr5_downloads, freedom_jr5_downloads))        
   
    #sorts domains by sum of total # of jr1 downloads
    arrangement = sorted(stats_by_domain, key=lambda x: (x[1] + x[2])) 

    #splitting elements of tuples in arrangement into lists so it is easier to plot
    domains_list = [i[0] for i in arrangement]
    subscribed_total = [i[1] for i in arrangement]
    freedom_total = [i[2] for i in arrangement]

    #make plot
    mpl.rcParams['ytick.major.width'] = 1
    mpl.rcParams['xtick.major.width'] = 1
    plt.figure(num=None, figsize=(8,8))
    plt.suptitle(f'JR5 downloads by Domain')

    plot = plt.scatter(subscribed_total, domains_list, color='blue')
    plot2 = plt.scatter(freedom_total, domains_list, color='orange')

    subscribed_legend_label = mpatches.Patch(color='blue', label='Elsevier Subscribed')
    freedom_legend_label = mpatches.Patch(color='orange', label='Elsevier Freedom')
    plt.xlabel('Number of JR5 Downloads')
    plt.legend(loc='lower right', handles=[subscribed_legend_label, freedom_legend_label])



def figure7g():
    """This is counting references by Domain for the subscribed titles and freedom collection providers
    
    Chart Type: Dot Plot/Scatter Plot
    Y-Axis: Domain
    Y-Axis Data Source: Original 1Figr Dataset, Journals Per Provider, Provider
                        Elsevier_2019, Subscribed Journal List 2019
    X-Axis: Number of References
    X-Axis Data Source: Original 1Figr Dataset, Journals Per Provider, Provider
                        Elsevier_2019, Subscribed Journal List 2019
    """
    
    original_1figr_data = pd.read_excel('JournalsPerProvider.xls', skiprows=8)
    subscribed_titles_provider = rf.make_elsevier_subscribed_titles_provider()
    freedom_collection_provider = rf.make_freedom_collection_provider()
    
    unique_domains = original_1figr_data['Domain'].unique().tolist()
    
    for i in unique_domains:    #this drops the 'nan' column from the unique domains
        if type(i) == float:
            unique_domains.remove(i)
    unique_domains.sort()

    stats_by_domain = []
    
    #builds list of tuples containing (Domain name, # of subscribed titles references, # of Freedom titles references)
    for domain in unique_domains:

        subscribed_subset_by_domain = subscribed_titles_provider.loc[subscribed_titles_provider['Domain'] == domain]
        subscribed_references = subscribed_subset_by_domain['References'].sum()

        freedom_subset_by_domain = freedom_collection_provider.loc[freedom_collection_provider['Domain'] == domain]
        freedom_references = freedom_subset_by_domain['References'].sum()

        stats_by_domain.append((domain, subscribed_references, freedom_references))        
   
    #sorts domains by sum of total # of jr1 downloads
    arrangement = sorted(stats_by_domain, key=lambda x: (x[1] + x[2])) 

    #splitting elements of tuples in arrangement into lists so it is easier to plot
    domains_list = [i[0] for i in arrangement]
    subscribed_total = [i[1] for i in arrangement]
    freedom_total = [i[2] for i in arrangement]

    #make plot
    mpl.rcParams['ytick.major.width'] = 1
    mpl.rcParams['xtick.major.width'] = 1
    plt.figure(num=None, figsize=(8,8))
    plt.suptitle(f'References by Domain')

    plot = plt.scatter(subscribed_total, domains_list, color='blue')
    plot2 = plt.scatter(freedom_total, domains_list, color='orange')

    subscribed_legend_label = mpatches.Patch(color='blue', label='Elsevier Subscribed')
    freedom_legend_label = mpatches.Patch(color='orange', label='Elsevier Freedom')
    plt.xlabel('Number of References')
    plt.legend(loc='lower right', handles=[subscribed_legend_label, freedom_legend_label])


def figure7h():
    """This is counting papers by Domain for the subscribed titles and freedom collection providers
    
    Chart Type: Dot Plot/Scatter Plot
    Y-Axis: Domain
    Y-Axis Data Source: Original 1Figr Dataset, Journals Per Provider, Provider
                        Elsevier_2019, Subscribed Journal List 2019
    X-Axis: Number of Papers
    X-Axis Data Source: Original 1Figr Dataset, Journals Per Provider, Provider
                        Elsevier_2019, Subscribed Journal List 2019
    """
    
    original_1figr_data = pd.read_excel('JournalsPerProvider.xls', skiprows=8)
    subscribed_titles_provider = rf.make_elsevier_subscribed_titles_provider()
    freedom_collection_provider = rf.make_freedom_collection_provider()
    
    unique_domains = original_1figr_data['Domain'].unique().tolist()
    
    for i in unique_domains:    #this drops the 'nan' column from the unique domains
        if type(i) == float:
            unique_domains.remove(i)
    unique_domains.sort()

    stats_by_domain = []
    
    #builds list of tuples containing (Domain name, # of subscribed titles papers, # of Freedom titles papers)
    for domain in unique_domains:

        subscribed_subset_by_domain = subscribed_titles_provider.loc[subscribed_titles_provider['Domain'] == domain]
        subscribed_papers = subscribed_subset_by_domain['Papers'].sum()

        freedom_subset_by_domain = freedom_collection_provider.loc[freedom_collection_provider['Domain'] == domain]
        freedom_papers = freedom_subset_by_domain['Papers'].sum()

        stats_by_domain.append((domain, subscribed_papers, freedom_papers))        
   
    #sorts domains by sum of total # of jr1 downloads
    arrangement = sorted(stats_by_domain, key=lambda x: (x[1] + x[2])) 

    #splitting elements of tuples in arrangement into lists so it is easier to plot
    domains_list = [i[0] for i in arrangement]
    subscribed_total = [i[1] for i in arrangement]
    freedom_total = [i[2] for i in arrangement]

    #make plot
    mpl.rcParams['ytick.major.width'] = 1
    mpl.rcParams['xtick.major.width'] = 1
    plt.figure(num=None, figsize=(8,8))
    plt.suptitle(f'Papers (Published Articles) by Domain')

    plot = plt.scatter(subscribed_total, domains_list, color='blue')
    plot2 = plt.scatter(freedom_total, domains_list, color='orange')

    subscribed_legend_label = mpatches.Patch(color='blue', label='Elsevier Subscribed')
    freedom_legend_label = mpatches.Patch(color='orange', label='Elsevier Freedom')
    plt.xlabel('Number of Papers')
    plt.legend(loc='lower right', handles=[subscribed_legend_label, freedom_legend_label])

figure7h()
