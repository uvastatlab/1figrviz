#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2 10:18:14 2019

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


"""
Documentation Format
----------------------------------------------------------------
Summary

Chart Type: Chart Type Name
Y-Axis: Dependent Variable Name
Y-Axis Data Source: SheetName, ColumnName
X-Axis:
X-Axis Data Source:

Supplemental Information
"""



def figure1a():
    """Creates stacked bar plot showing jr1 downloads and jr80, jr90, jr95 score for big 5 providers.
    JR80 is journals that make up 80% of downloads. JR90 are journals that make up 90% of downloads.
    JR95 are journals that make up 95% of downloads. These will all be plotted together.
    
    Chart Type: Stacked bar
    Y-Axis: Percentage
    Y-Axis Data Source: Original 1Figr Dataset
    
    X-Axis: Provider Name
    X-Axis Data Source: Original 1Figr Dataset
    """
    
#    TODO: ADD LABELS TO PLOT

    data = pd.read_excel(filename, sheet_name='Journals per Provider', skiprows=8)
    

    big5 = ['Elsevier', 'Sage', 'Springer', 'Taylor & Francis', 'Wiley'] 
        
    stats_by_provider = []
#    plot_stats_by_provider = []                         #used later for labels in plot

    for provider_name in big5:

        subset_by_provider = data.loc[data['Provider'] == provider_name]
        journals_data = subset_by_provider.groupby('Journal', as_index=False).sum().values.tolist()

        for i in journals_data:
            if i[0] == provider_name:
                journals_data.remove(i)                 #removing aggregator column data
        
        total_jr1_downloads = 0
        total_journals = 0                         
        for i in journals_data:
            total_jr1_downloads += i[4]
            total_journals += 1
            
        jr1_tuples = [(i[0], i[4]) for i in journals_data]
        jr1_tuples_sorted = sorted(jr1_tuples, key = lambda i: i[1], reverse=True)      #sorts on second element of jr1_tuples

        jr80_running_tally = 0
        jr90_running_tally = 0
        jr95_running_tally = 0
        jr80_highly_used_journals = []           #THIS HOLDS (JOURNAL NAME, JR1_DOWNLOADS)
        jr90_highly_used_journals = []
        jr95_highly_used_journals = []
        
        for i in jr1_tuples_sorted:
            if jr80_running_tally < (total_jr1_downloads * 0.8):
                jr80_highly_used_journals.append(i)
                jr80_running_tally += i[1]
#                
        jr80_score = (len(jr80_highly_used_journals))/(total_journals)
        print(len(jr80_highly_used_journals))
#                
        for i in jr1_tuples_sorted:
            if jr90_running_tally < (total_jr1_downloads * 0.9):
                jr90_highly_used_journals.append(i)
                jr90_running_tally += i[1]
                
        jr90_score = (len(jr90_highly_used_journals))/(total_journals)
        print(len(jr90_highly_used_journals))
        jr90_score = (jr90_score - jr80_score)


        for i in jr1_tuples_sorted:
            if jr95_running_tally < (total_jr1_downloads * 0.95):
                jr95_highly_used_journals.append(i)
                jr95_running_tally += i[1]

        jr95_score = (len(jr95_highly_used_journals))/(total_journals)
        print(len(jr95_highly_used_journals))
        jr95_score = (jr95_score - (jr80_score + jr90_score))
        
        total_score = (1- (jr80_score+jr90_score+jr95_score))

        stats_by_provider.append((provider_name, jr80_score, jr90_score, jr95_score, total_score))


    #make plot
    plt.figure(num=None, figsize=(10, 10))
    plt.suptitle('Percentage of Titles Downloaded by Provider (JR1 Downloads)')
    plt.ylabel('Percent of total titles')
    plt.gca().yaxis.set_major_formatter(StrMethodFormatter('{x:,.0%}'))    #formats y axis as %
    
    #make custom plot legend
    jr80s = mpatches.Patch(color='violet', label='JR80 titles')
    jr90s = mpatches.Patch(color='moccasin', label='JR90 titles')
    jr95s = mpatches.Patch(color='paleturquoise', label='JR95 titles')
    others = mpatches.Patch(color='silver', label='Total titles')
    
    plt.legend(handles=[jr80s, jr90s, jr95s, others], bbox_to_anchor=(1, 1))   #moves legend outside plot
    
    for i in stats_by_provider: 
        
        provider = i[0]
        jr80 = i[1]
        jr90 = i[2]
        jr95 = i[3]
        total_values = i[4]
        
        plt.bar(provider, jr80, color='violet')
        plt.bar(provider, jr90, bottom=jr80, color='moccasin')
        plt.bar(provider, jr95, bottom=(jr80 + jr90), color='paleturquoise')
        plt.bar(provider, total_values, bottom=(jr80 + jr90 + jr95), color='silver')



def figure1b():
    """Creates stacked bar plot showing jr5 downloads and jr80, jr90, jr95 score for big 5 providers.
    JR80 is journals that make up 80% of downloads. JR90 are journals that make up 90% of downloads.
    JR95 are journals that make up 95% of downloads. These will all be plotted together.
    
    Chart Type: Stacked bar
    Y-Axis: Percentage
    Y-Axis Data Source: Original 1Figr Dataset
    
    X-Axis: Provider Name
    X-Axis Data Source: Original 1Figr Dataset
    """

    
    data = pd.read_excel(filename, sheet_name='Journals per Provider', skiprows=8)

    big5 = ['Elsevier', 'Sage', 'Springer', 'Taylor & Francis', 'Wiley'] 

    stats_by_provider = []
#    plot_stats_by_provider = []                         #used later for labels in plot

    for provider_name in big5:

        subset_by_provider = data.loc[data['Provider'] == provider_name]
        journals_data = subset_by_provider.groupby('Journal', as_index=False).sum().values.tolist()

        for i in journals_data:
            if i[0] == provider_name:
                journals_data.remove(i)                 #removing aggregator column data
        
        total_jr5_downloads = 0
        total_journals = 0                         
        for i in journals_data:
            total_jr5_downloads += i[5]
            total_journals += 1
            
        jr5_tuples = [(i[0], i[5]) for i in journals_data]
        jr5_tuples_sorted = sorted(jr5_tuples, key = lambda i: i[1], reverse=True)     #sorts on second element of jr1_tuples
        
        jr80_running_tally = 0
        jr90_running_tally = 0
        jr95_running_tally = 0
        jr80_highly_used_journals = []           #THIS HOLDS (JOURNAL NAME, JR1_DOWNLOADS)
        jr90_highly_used_journals = []
        jr95_highly_used_journals = []
        
        for i in jr5_tuples_sorted:
            if jr80_running_tally < (total_jr5_downloads * 0.8):
                jr80_highly_used_journals.append(i)
                jr80_running_tally += i[1]
                
        jr80_score = (len(jr80_highly_used_journals))/(total_journals)
        print(len(jr80_highly_used_journals))
                
        for i in jr5_tuples_sorted:
            if jr90_running_tally < (total_jr5_downloads * 0.9):
                jr90_highly_used_journals.append(i)
                jr90_running_tally += i[1]
                
        jr90_score = (len(jr90_highly_used_journals))/(total_journals)
        print(len(jr90_highly_used_journals))
        jr90_score = (jr90_score - jr80_score)

        for i in jr5_tuples_sorted:
            if jr95_running_tally < (total_jr5_downloads * 0.95):
                jr95_highly_used_journals.append(i)
                jr95_running_tally += i[1]

        jr95_score = (len(jr95_highly_used_journals))/(total_journals)
        print(len(jr95_highly_used_journals))
        jr95_score = (jr95_score - (jr80_score + jr90_score))
        print(total_journals)
        
        total_score = (1- (jr80_score+jr90_score+jr95_score))

        stats_by_provider.append((provider_name, jr80_score, jr90_score, jr95_score, total_score))


    #make plot
    plt.figure(num=None, figsize=(10, 10))
    plt.suptitle('Percentage of Titles Downloaded by Provider (JR5 Downloads)')
    plt.ylabel('Percent of total titles')
    
    plt.gca().yaxis.set_major_formatter(StrMethodFormatter('{x:,.0%}'))    #formats y axis as %

    
    #make custom plot legend
    jr80s = mpatches.Patch(color='violet', label='JR80 titles')
    jr90s = mpatches.Patch(color='moccasin', label='JR90 titles')
    jr95s = mpatches.Patch(color='paleturquoise', label='JR95 titles')
    others = mpatches.Patch(color='silver', label='Total titles')
    
    plt.legend(handles=[jr80s, jr90s, jr95s, others], bbox_to_anchor=(1, 1))   #moves legend outside plot
    
    for i in stats_by_provider: 
        
        provider = i[0]
        jr80 = i[1]
        jr90 = i[2]
        jr95 = i[3]
        total_values = i[4]
        
        plt.bar(provider, jr80, color='violet')
        plt.bar(provider, jr90, bottom=jr80, color='moccasin')
        plt.bar(provider, jr95, bottom=(jr80 + jr90), color='paleturquoise')
        plt.bar(provider, total_values, bottom=(jr80 + jr90 + jr95), color='silver')
 

def figure1c():
    """Creates stacked bar plot showing article references and jr80, jr90, jr95 score for big 5 providers.
    JR80 is journals that make up 80% of downloads. JR90 are journals that make up 90% of downloads.
    JR95 are journals that make up 95% of downloads. These will all be plotted together.
    
    Chart Type: Stacked bar
    Y-Axis: Percentage
    Y-Axis Data Source: Original 1Figr Dataset
    
    X-Axis: Provider Name
    X-Axis Data Source: Original 1Figr Dataset
    """

    
    data = pd.read_excel(filename, sheet_name='Journals per Provider', skiprows=8)


    big5 = ['Elsevier', 'Sage', 'Springer', 'Taylor & Francis', 'Wiley'] 
#    big5 = ['AIP']        
    stats_by_provider = []
#    plot_stats_by_provider = []                         #used later for labels in plot

    for provider_name in big5:

        subset_by_provider = data.loc[data['Provider'] == provider_name]
        journals_data = subset_by_provider.groupby('Journal', as_index=False).sum().values.tolist()

        for i in journals_data:
            if i[0] == provider_name:
                journals_data.remove(i)                 #removing aggregator column data
        
        total_references = 0
        total_journals = 0                         
        for i in journals_data:
            total_references += i[6]
            total_journals += 1
            
        reference_tuples = [(i[0], i[6]) for i in journals_data]
        reference_tuples_sorted = sorted(reference_tuples, key = lambda i: i[1], reverse=True)     #sorts on second element of jr1_tuples
        
        jr80_running_tally = 0
        jr90_running_tally = 0
        jr95_running_tally = 0
        jr80_highly_used_journals = []           #THIS HOLDS (JOURNAL NAME, JR1_DOWNLOADS)
        jr90_highly_used_journals = []
        jr95_highly_used_journals = []
        
        for i in reference_tuples_sorted:
            if jr80_running_tally < (total_references * 0.8):
                jr80_highly_used_journals.append(i)
                jr80_running_tally += i[1]
                
        jr80_score = (len(jr80_highly_used_journals))/(total_journals)
        print(len(jr80_highly_used_journals))
                
        for i in reference_tuples_sorted:
            if jr90_running_tally < (total_references * 0.9):
                jr90_highly_used_journals.append(i)
                jr90_running_tally += i[1]
                
        jr90_score = (len(jr90_highly_used_journals))/(total_journals)
        print(len(jr90_highly_used_journals))
        jr90_score = (jr90_score - jr80_score)

        for i in reference_tuples_sorted:
            if jr95_running_tally < (total_references * 0.95):
                jr95_highly_used_journals.append(i)
                jr95_running_tally += i[1]

        jr95_score = (len(jr95_highly_used_journals))/(total_journals)
        print(len(jr95_highly_used_journals))
        jr95_score = (jr95_score - (jr80_score + jr90_score))
        print(total_journals)
        
        total_score = (1- (jr80_score+jr90_score+jr95_score))

        stats_by_provider.append((provider_name, jr80_score, jr90_score, jr95_score, total_score))


    #make plot
    plt.figure(num=None, figsize=(10, 10))
    plt.suptitle('Percentage of Articles Referenced by Provider')
    plt.ylabel('Percent of total titles')
    
    #make custom plot legend
    jr80s = mpatches.Patch(color='violet', label='JR80 titles')
    jr90s = mpatches.Patch(color='moccasin', label='JR90 titles')
    jr95s = mpatches.Patch(color='paleturquoise', label='JR95 titles')
    others = mpatches.Patch(color='silver', label='Total titles')

    plt.gca().yaxis.set_major_formatter(StrMethodFormatter('{x:,.0%}'))    #formats y axis as %
    
    plt.legend(handles=[jr80s, jr90s, jr95s, others], bbox_to_anchor=(1, 1))   #moves legend outside plot
    
    for i in stats_by_provider: 
        
        provider = i[0]
        jr80 = i[1]
        jr90 = i[2]
        jr95 = i[3]
        total_values = i[4]
        
        plt.bar(provider, jr80, color='violet')
        plt.bar(provider, jr90, bottom=jr80, color='moccasin')
        plt.bar(provider, jr95, bottom=(jr80 + jr90), color='paleturquoise')
        plt.bar(provider, total_values, bottom=(jr80 + jr90 + jr95), color='silver')

    plt.savefig('test.jpg', bbox_inches='tight')      #saves image in working directory


def figure1d():
    """Creates stacked bar plot showing publications and jr80, jr90, jr95 score for big 5 providers.
    JR80 is journals that make up 80% of downloads. JR90 are journals that make up 90% of downloads.
    JR95 are journals that make up 95% of downloads. These will all be plotted together.
    
    Chart Type: Stacked bar
    Y-Axis: Percentage
    Y-Axis Data Source: Original 1Figr Dataset
    
    X-Axis: Provider Name
    X-Axis Data Source: Original 1Figr Dataset
    """

    
    data = pd.read_excel(filename, sheet_name='Journals per Provider', skiprows=8)


    big5 = ['Elsevier', 'Sage', 'Springer', 'Taylor & Francis', 'Wiley'] 
#    big5 = ['AIP']        
    stats_by_provider = []
#    plot_stats_by_provider = []                         #used later for labels in plot

    for provider_name in big5:

        subset_by_provider = data.loc[data['Provider'] == provider_name]
        journals_data = subset_by_provider.groupby('Journal', as_index=False).sum().values.tolist()

        for i in journals_data:
            if i[0] == provider_name:
                journals_data.remove(i)                 #removing aggregator column data
        
        total_papers = 0
        total_journals = 0                         
        for i in journals_data:
            total_papers += i[7]
            total_journals += 1
            
        paper_tuples = [(i[0], i[7]) for i in journals_data]
        paper_tuples_sorted = sorted(paper_tuples, key = lambda i: i[1], reverse=True)      #sorts on second element of jr1_tuples
        
        jr80_running_tally = 0
        jr90_running_tally = 0
        jr95_running_tally = 0
        jr80_highly_used_journals = []           #THIS HOLDS (JOURNAL NAME, JR1_DOWNLOADS)
        jr90_highly_used_journals = []
        jr95_highly_used_journals = []
        
        for i in paper_tuples_sorted:
            if jr80_running_tally < (total_papers * 0.8):
                jr80_highly_used_journals.append(i)
                jr80_running_tally += i[1]
                
        jr80_score = (len(jr80_highly_used_journals))/(total_journals)
        print(len(jr80_highly_used_journals))
                
        for i in paper_tuples_sorted:
            if jr90_running_tally < (total_papers * 0.9):
                jr90_highly_used_journals.append(i)
                jr90_running_tally += i[1]
                
        jr90_score = (len(jr90_highly_used_journals))/(total_journals)
        print(len(jr90_highly_used_journals))
        jr90_score = (jr90_score - jr80_score)

        for i in paper_tuples_sorted:
            if jr95_running_tally < (total_papers * 0.95):
                jr95_highly_used_journals.append(i)
                jr95_running_tally += i[1]

        jr95_score = (len(jr95_highly_used_journals))/(total_journals)
        print(len(jr95_highly_used_journals))
        jr95_score = (jr95_score - (jr80_score + jr90_score))
        print(total_journals)
        
        total_score = (1- (jr80_score+jr90_score+jr95_score))

        stats_by_provider.append((provider_name, jr80_score, jr90_score, jr95_score, total_score))


    #make plot
    plt.figure(num=None, figsize=(10, 10))
    plt.suptitle(f'Percentage of Papers Published by {your_institution} Authors')
    plt.ylabel('Percent of total titles')
    
    #make custom plot legend
    jr80s = mpatches.Patch(color='violet', label='JR80 titles')
    jr90s = mpatches.Patch(color='moccasin', label='JR90 titles')
    jr95s = mpatches.Patch(color='paleturquoise', label='JR95 titles')
    others = mpatches.Patch(color='silver', label='Total titles')

    plt.gca().yaxis.set_major_formatter(StrMethodFormatter('{x:,.0%}'))    #formats y axis as %
    
    plt.legend(handles=[jr80s, jr90s, jr95s, others], bbox_to_anchor=(1, 1))   #moves legend outside plot
    
    for i in stats_by_provider: 
        
        provider = i[0]
        jr80 = i[1]
        jr90 = i[2]
        jr95 = i[3]
        total_values = i[4]
        
        plt.bar(provider, jr80, color='violet')
        plt.bar(provider, jr90, bottom=jr80, color='moccasin')
        plt.bar(provider, jr95, bottom=(jr80 + jr90), color='paleturquoise')
        plt.bar(provider, total_values, bottom=(jr80 + jr90 + jr95), color='silver')
   

def figure1e():
    """Makes JR80, JR90, JR95 graph for all 6 big providers,
    splitting elsevier into Elseveier Freedom and Elsevier Subscribed.
    
    Plots JR1 Downloads (Articles published in any year, downloaded in 2017)
    
    JR80 = Journals which make up 80% of JR1 Downloads
    JR90 = Journals which make up 90% of JR1 Downloads
    JR95 = Journals which make up 95% of JR1 Downloads
    
    Chart Type: Stacked Bar Graph
    Y-Axis: Percent of Total Titles
    Y-Axis Data Source: Original 1Figr Dataset, Journals Per Provider, Provider
                        Elsevier_2019, Subscribed Journal List 2019
    X-Axis: Provider Name
    X-Axis Data Source: Original 1Figr Dataset, Journals Per Provider, Provider
                        Elsevier_2019, Subscribed Journal List 2019
    """
    
    data = pd.read_excel(filename, sheet_name='Journals per Provider', skiprows=8)
    
    stats_by_provider = []

    providers = ['Sage', 'Springer', 'Taylor & Francis', 'Wiley']
    
    #make stats for existing providers
    for provider_name in providers:
        
        subset_by_provider = data.loc[data['Provider'] == provider_name]
        journals_data = subset_by_provider.groupby('Journal', as_index=False).sum().values.tolist()

        for i in journals_data:
            if i[0] == provider_name:
                journals_data.remove(i)                 #removing aggregator column data
        
        total_jr1_downloads = 0
        total_journals = 0                         
        for i in journals_data:
            total_jr1_downloads += i[4]
            total_journals += 1

        jr1_tuples = [(i[0], i[4]) for i in journals_data]
        jr1_tuples_sorted = sorted(jr1_tuples, key = lambda i: i[1], reverse=True)      #sorts on second element of jr1_tuples


        jr80_running_tally = 0                  #represents 80% of collections use
        jr90_running_tally = 0
        jr95_running_tally = 0
        jr80_highly_used_journals = []           #THIS HOLDS (JOURNAL NAME, JR1_DOWNLOADS)
        jr90_highly_used_journals = []
        jr95_highly_used_journals = []
        
        for i in jr1_tuples_sorted:
            if jr80_running_tally < (total_jr1_downloads * 0.8):
                jr80_highly_used_journals.append(i)
                jr80_running_tally += i[1]

        for i in jr1_tuples_sorted:
            if jr90_running_tally < (total_jr1_downloads * 0.9):
                jr90_highly_used_journals.append(i)
                jr90_running_tally += i[1]

        for i in jr1_tuples_sorted:
            if jr95_running_tally < (total_jr1_downloads * 0.95):
                jr95_highly_used_journals.append(i)
                jr95_running_tally += i[1]
                
        jr80_score = (len(jr80_highly_used_journals))/(total_journals)
        jr90_score = (len(jr90_highly_used_journals))/(total_journals)
        jr90_score = (jr90_score - jr80_score)
        jr95_score = (len(jr95_highly_used_journals))/(total_journals)
        jr95_score = (jr95_score - (jr80_score + jr90_score))


        total_score = (1- (jr80_score+jr90_score+jr95_score))

        stats_by_provider.append((provider_name, jr80_score, jr90_score, jr95_score, total_score, len(jr80_highly_used_journals), len(jr90_highly_used_journals), len(jr95_highly_used_journals)))

    unmatched_collection_provider = rf.make_elsevier_unmatched_provider()
    unmatched_collection_provider['Provider Name'] = 'Elsevier Unmatched'   #need to create a column which holds provider name

    subscribed_titles_provider = rf.make_elsevier_subscribed_titles_provider()
    subscribed_titles_provider['Provider Name'] = 'Elsevier Subscribed'    #need to create a column which holds provider name
    
    freedom_collection_provider = rf.make_freedom_collection_provider()
    freedom_collection_provider['Provider Name'] = 'Elsevier Freedom'  #need to create a column which holds provider name
    
    elsevier_providers = [unmatched_collection_provider, subscribed_titles_provider, freedom_collection_provider]
    
    for provider_name in elsevier_providers:
        
        first_row = provider_name.iloc[1]
        name = first_row['Provider Name']    #need string of provider name for stats_by_provider
        
        journals_data = provider_name.groupby('Journal', as_index=False).sum().values.tolist()
        
        total_jr1_downloads = 0
        total_journals = 0                         
        for i in journals_data:
            total_jr1_downloads += i[4]
            total_journals += 1

        jr1_tuples = [(i[0], i[4]) for i in journals_data]
        jr1_tuples_sorted = sorted(jr1_tuples, key = lambda i: i[1], reverse=True)      #sorts on second element of jr1_tuples

        jr80_running_tally = 0                  #represents 80% of collections use
        jr90_running_tally = 0
        jr95_running_tally = 0
        jr80_highly_used_journals = []           #THIS HOLDS (JOURNAL NAME, JR1_DOWNLOADS)
        jr90_highly_used_journals = []
        jr95_highly_used_journals = []
        
        for i in jr1_tuples_sorted:
            if jr80_running_tally < (total_jr1_downloads * 0.8):
                jr80_highly_used_journals.append(i)
                jr80_running_tally += i[1]

        for i in jr1_tuples_sorted:
            if jr90_running_tally < (total_jr1_downloads * 0.9):
                jr90_highly_used_journals.append(i)
                jr90_running_tally += i[1]

        for i in jr1_tuples_sorted:
            if jr95_running_tally < (total_jr1_downloads * 0.95):
                jr95_highly_used_journals.append(i)
                jr95_running_tally += i[1]
                
        jr80_score = (len(jr80_highly_used_journals))/(total_journals)
        jr90_score = (len(jr90_highly_used_journals))/(total_journals)
        jr90_score = (jr90_score - jr80_score)
        jr95_score = (len(jr95_highly_used_journals))/(total_journals)
        jr95_score = (jr95_score - (jr80_score + jr90_score))

        total_score = (1- (jr80_score+jr90_score+jr95_score))

        stats_by_provider.append((name, jr80_score, jr90_score, jr95_score, total_score, len(jr80_highly_used_journals), len(jr90_highly_used_journals), len(jr95_highly_used_journals)))
           
    #make plot
    plt.figure(num=None, figsize=(10, 10))
    plt.suptitle('Percentage of Titles Downloaded by Provider (JR1 Downloads)')
    plt.ylabel('Percent of total titles')
    plt.gca().yaxis.set_major_formatter(StrMethodFormatter('{x:,.0%}'))    #formats y axis as %

    jr80s = mpatches.Patch(color='violet', label='JR80 titles')
    jr90s = mpatches.Patch(color='moccasin', label='JR90 titles')
    jr95s = mpatches.Patch(color='paleturquoise', label='JR95 titles')
    others = mpatches.Patch(color='silver', label='Total titles')

    plt.legend(handles=[jr80s, jr90s, jr95s, others], bbox_to_anchor=(1, 1))   #moves legend outside plot
    plt.xticks(rotation=45)

    #NEED TO ADD LABELS TO PLOTS
    for i in stats_by_provider: 
        
        provider = i[0]
        jr80 = i[1]
        jr90 = i[2]
        jr95 = i[3]
        total_values = i[4]

        
        plot1 = plt.bar(provider, jr80, color='violet')
        plot2 = plt.bar(provider, jr90, bottom=jr80, color='moccasin')
        plot3 = plt.bar(provider, jr95, bottom=(jr80 + jr90), color='paleturquoise')
        plot4 = plt.bar(provider, total_values, bottom=(jr80 + jr90 + jr95), color='silver')

        
    
def figure1f():
    """Makes JR80, JR90, JR95 graph for all 6 big providers,
    splitting elsevier into Elseveier Freedom and Elsevier Subscribed.
    
    Plots JR5 Downloads (Articles published in 2017, downloaded in 2017)
    
    JR80 = Journals which make up 80% of JR5 Downloads
    JR90 = Journals which make up 90% of JR5 Downloads
    JR95 = Journals which make up 95% of JR5 Downloads
    
    Chart Type: Stacked Bar Graph
    Y-Axis: Percent of Total Titles
    Y-Axis Data Source: Original 1Figr Dataset, Journals Per Provider, Provider
                        Elsevier_2019, Subscribed Journal List 2019
    X-Axis: Provider Name
    X-Axis Data Source: Original 1Figr Dataset, Journals Per Provider, Provider
                        Elsevier_2019, Subscribed Journal List 2019
    """  
    
    data = pd.read_excel(filename, sheet_name='Journals per Provider', skiprows=8)
    
    stats_by_provider = []

    providers = ['Sage', 'Springer', 'Taylor & Francis', 'Wiley']
    
    #make stats for existing providers
    for provider_name in providers:
        
        subset_by_provider = data.loc[data['Provider'] == provider_name]
        journals_data = subset_by_provider.groupby('Journal', as_index=False).sum().values.tolist()

        for i in journals_data:
            if i[0] == provider_name:
                journals_data.remove(i)                 #removing aggregator column data
        
        total_jr5_downloads = 0
        total_journals = 0                         
        for i in journals_data:
            total_jr5_downloads += i[5]
            total_journals += 1

        jr5_tuples = [(i[0], i[5]) for i in journals_data]
        jr5_tuples_sorted = sorted(jr5_tuples, key = lambda i: i[1], reverse=True)      #sorts on second element of jr5_tuples


        jr80_running_tally = 0                  #represents 80% of collections use
        jr90_running_tally = 0
        jr95_running_tally = 0
        jr80_highly_used_journals = []           #THIS HOLDS (JOURNAL NAME, JR5_DOWNLOADS)
        jr90_highly_used_journals = []
        jr95_highly_used_journals = []
        
        for i in jr5_tuples_sorted:
            if jr80_running_tally < (total_jr5_downloads * 0.8):
                jr80_highly_used_journals.append(i)
                jr80_running_tally += i[1]

        for i in jr5_tuples_sorted:
            if jr90_running_tally < (total_jr5_downloads * 0.9):
                jr90_highly_used_journals.append(i)
                jr90_running_tally += i[1]

        for i in jr5_tuples_sorted:
            if jr95_running_tally < (total_jr5_downloads * 0.95):
                jr95_highly_used_journals.append(i)
                jr95_running_tally += i[1]
                
        jr80_score = (len(jr80_highly_used_journals))/(total_journals)
        jr90_score = (len(jr90_highly_used_journals))/(total_journals)
        jr90_score = (jr90_score - jr80_score)
        jr95_score = (len(jr95_highly_used_journals))/(total_journals)
        jr95_score = (jr95_score - (jr80_score + jr90_score))


        total_score = (1- (jr80_score+jr90_score+jr95_score))

        stats_by_provider.append((provider_name, jr80_score, jr90_score, jr95_score, total_score, len(jr80_highly_used_journals), len(jr90_highly_used_journals), len(jr95_highly_used_journals)))
 
    unmatched_collection_provider = rf.make_elsevier_unmatched_provider()
    unmatched_collection_provider['Provider Name'] = 'Elsevier Unmatched'   #need to create a column which holds provider name

    subscribed_titles_provider = rf.make_elsevier_subscribed_titles_provider()
    subscribed_titles_provider['Provider Name'] = 'Elsevier Subscribed'    #need to create a column which holds provider name
    
    freedom_collection_provider = rf.make_freedom_collection_provider()
    freedom_collection_provider['Provider Name'] = 'Elsevier Freedom'  #need to create a column which holds provider name
    
    elsevier_providers = [unmatched_collection_provider, subscribed_titles_provider, freedom_collection_provider]
    
    for provider_name in elsevier_providers:
        
        first_row = provider_name.iloc[1]
        name = first_row['Provider Name']    #need string of provider name for stats_by_provider
        
        journals_data = provider_name.groupby('Journal', as_index=False).sum().values.tolist()
        
        total_jr5_downloads = 0
        total_journals = 0                         
        for i in journals_data:
            total_jr5_downloads += i[5]
            total_journals += 1

        jr5_tuples = [(i[0], i[5]) for i in journals_data]
        jr5_tuples_sorted = sorted(jr5_tuples, key = lambda i: i[1], reverse=True)      #sorts on second element of jr5_tuples

        jr80_running_tally = 0                  #represents 80% of collections use
        jr90_running_tally = 0
        jr95_running_tally = 0
        jr80_highly_used_journals = []           #THIS HOLDS (JOURNAL NAME, JR5_DOWNLOADS)
        jr90_highly_used_journals = []
        jr95_highly_used_journals = []
        
        for i in jr5_tuples_sorted:
            if jr80_running_tally < (total_jr5_downloads * 0.8):
                jr80_highly_used_journals.append(i)
                jr80_running_tally += i[1]

        for i in jr5_tuples_sorted:
            if jr90_running_tally < (total_jr5_downloads * 0.9):
                jr90_highly_used_journals.append(i)
                jr90_running_tally += i[1]

        for i in jr5_tuples_sorted:
            if jr95_running_tally < (total_jr5_downloads * 0.95):
                jr95_highly_used_journals.append(i)
                jr95_running_tally += i[1]
                
        jr80_score = (len(jr80_highly_used_journals))/(total_journals)
        jr90_score = (len(jr90_highly_used_journals))/(total_journals)
        jr90_score = (jr90_score - jr80_score)
        jr95_score = (len(jr95_highly_used_journals))/(total_journals)
        jr95_score = (jr95_score - (jr80_score + jr90_score))

        total_score = (1- (jr80_score+jr90_score+jr95_score))

        stats_by_provider.append((name, jr80_score, jr90_score, jr95_score, total_score, len(jr80_highly_used_journals), len(jr90_highly_used_journals), len(jr95_highly_used_journals)))
           
    #make plot
    plt.figure(num=None, figsize=(10, 10))
    plt.suptitle('Percentage of Titles Downloaded by Provider (JR5 Downloads)')
    plt.ylabel('Percent of total titles')
    plt.gca().yaxis.set_major_formatter(StrMethodFormatter('{x:,.0%}'))    #formats y axis as %

    jr80s = mpatches.Patch(color='violet', label='JR80 titles')
    jr90s = mpatches.Patch(color='moccasin', label='JR90 titles')
    jr95s = mpatches.Patch(color='paleturquoise', label='JR95 titles')
    others = mpatches.Patch(color='silver', label='Total titles')

    plt.legend(handles=[jr80s, jr90s, jr95s, others], bbox_to_anchor=(1, 1))   #moves legend outside plot
    plt.xticks(rotation=45)

    #NEED TO ADD LABELS TO PLOTS
    for i in stats_by_provider: 
        
        provider = i[0]
        jr80 = i[1]
        jr90 = i[2]
        jr95 = i[3]
        total_values = i[4]

        
        plot1 = plt.bar(provider, jr80, color='violet')
        plot2 = plt.bar(provider, jr90, bottom=jr80, color='moccasin')
        plot3 = plt.bar(provider, jr95, bottom=(jr80 + jr90), color='paleturquoise')
        plot4 = plt.bar(provider, total_values, bottom=(jr80 + jr90 + jr95), color='silver')
    
    

def figure1g():
    """Makes JR80, JR90, JR95 graph for all 6 big providers,
    splitting elsevier into Elseveier Freedom and Elsevier Subscribed.
    
    Plots References (Articles published by your institution, referenced by other authors)
    
    JR80 = Journals which make up 80% of References
    JR90 = Journals which make up 90% of References
    JR95 = Journals which make up 95% of References
    
    Chart Type: Stacked Bar Graph
    Y-Axis: Percent of Total Titles
    Y-Axis Data Source: Original 1Figr Dataset, Journals Per Provider, Provider
                        Elsevier_2019, Subscribed Journal List 2019
    X-Axis: Provider Name
    X-Axis Data Source: Original 1Figr Dataset, Journals Per Provider, Provider
                        Elsevier_2019, Subscribed Journal List 2019
    """
    
    data = pd.read_excel(filename, sheet_name='Journals per Provider', skiprows=8)
    
    stats_by_provider = []

    providers = ['Sage', 'Springer', 'Taylor & Francis', 'Wiley']
    
    #make stats for existing providers
    for provider_name in providers:
        
        subset_by_provider = data.loc[data['Provider'] == provider_name]
        journals_data = subset_by_provider.groupby('Journal', as_index=False).sum().values.tolist()

        for i in journals_data:
            if i[0] == provider_name:
                journals_data.remove(i)                 #removing aggregator column data
        
        total_references = 0
        total_journals = 0                         
        for i in journals_data:
            total_references += i[6]
            total_journals += 1

        reference_tuples = [(i[0], i[6]) for i in journals_data]
        reference_tuples_sorted = sorted(reference_tuples, key = lambda i: i[1], reverse=True)      #sorts on second element of reference_tuples


        jr80_running_tally = 0                  #represents 80% of collections use
        jr90_running_tally = 0
        jr95_running_tally = 0
        jr80_highly_used_journals = []           #THIS HOLDS (JOURNAL NAME, REFERENCES)
        jr90_highly_used_journals = []
        jr95_highly_used_journals = []
        
        for i in reference_tuples_sorted:
            if jr80_running_tally < (total_references * 0.8):
                jr80_highly_used_journals.append(i)
                jr80_running_tally += i[1]

        for i in reference_tuples_sorted:
            if jr90_running_tally < (total_references * 0.9):
                jr90_highly_used_journals.append(i)
                jr90_running_tally += i[1]

        for i in reference_tuples_sorted:
            if jr95_running_tally < (total_references * 0.95):
                jr95_highly_used_journals.append(i)
                jr95_running_tally += i[1]
                
        jr80_score = (len(jr80_highly_used_journals))/(total_journals)
        jr90_score = (len(jr90_highly_used_journals))/(total_journals)
        jr90_score = (jr90_score - jr80_score)
        jr95_score = (len(jr95_highly_used_journals))/(total_journals)
        jr95_score = (jr95_score - (jr80_score + jr90_score))


        total_score = (1- (jr80_score+jr90_score+jr95_score))

        stats_by_provider.append((provider_name, jr80_score, jr90_score, jr95_score, total_score, len(jr80_highly_used_journals), len(jr90_highly_used_journals), len(jr95_highly_used_journals)))

    unmatched_collection_provider = rf.make_elsevier_unmatched_provider()
    unmatched_collection_provider['Provider Name'] = 'Elsevier Unmatched'   #need to create a column which holds provider name

    subscribed_titles_provider = rf.make_elsevier_subscribed_titles_provider()
    subscribed_titles_provider['Provider Name'] = 'Elsevier Subscribed'    #need to create a column which holds provider name
    
    freedom_collection_provider = rf.make_freedom_collection_provider()
    freedom_collection_provider['Provider Name'] = 'Elsevier Freedom'  #need to create a column which holds provider name
    
    elsevier_providers = [unmatched_collection_provider, subscribed_titles_provider, freedom_collection_provider]
    
    for provider_name in elsevier_providers:
        
        first_row = provider_name.iloc[1]
        name = first_row['Provider Name']    #need string of provider name for stats_by_provider
        
        journals_data = provider_name.groupby('Journal', as_index=False).sum().values.tolist()
        
        total_references = 0
        total_journals = 0                         
        for i in journals_data:
            total_references += i[6]
            total_journals += 1

        reference_tuples = [(i[0], i[6]) for i in journals_data]
        reference_tuples_sorted = sorted(reference_tuples, key = lambda i: i[1], reverse=True)      #sorts on second element of reference_tuples

        jr80_running_tally = 0                  #represents 80% of collections use
        jr90_running_tally = 0
        jr95_running_tally = 0
        jr80_highly_used_journals = []           #THIS HOLDS (JOURNAL NAME, REFERENCES)
        jr90_highly_used_journals = []
        jr95_highly_used_journals = []
        
        for i in reference_tuples_sorted:
            if jr80_running_tally < (total_references * 0.8):
                jr80_highly_used_journals.append(i)
                jr80_running_tally += i[1]

        for i in reference_tuples_sorted:
            if jr90_running_tally < (total_references * 0.9):
                jr90_highly_used_journals.append(i)
                jr90_running_tally += i[1]

        for i in reference_tuples_sorted:
            if jr95_running_tally < (total_references * 0.95):
                jr95_highly_used_journals.append(i)
                jr95_running_tally += i[1]
                
        jr80_score = (len(jr80_highly_used_journals))/(total_journals)
        jr90_score = (len(jr90_highly_used_journals))/(total_journals)
        jr90_score = (jr90_score - jr80_score)
        jr95_score = (len(jr95_highly_used_journals))/(total_journals)
        jr95_score = (jr95_score - (jr80_score + jr90_score))

        total_score = (1- (jr80_score+jr90_score+jr95_score))

        stats_by_provider.append((name, jr80_score, jr90_score, jr95_score, total_score, len(jr80_highly_used_journals), len(jr90_highly_used_journals), len(jr95_highly_used_journals)))
           
    #make plot
    plt.figure(num=None, figsize=(10, 10))
    plt.suptitle('Percentage of Titles Referenced by Provider (References)')
    plt.ylabel('Percent of total titles')
    plt.gca().yaxis.set_major_formatter(StrMethodFormatter('{x:,.0%}'))    #formats y axis as %

    jr80s = mpatches.Patch(color='violet', label='JR80 titles')
    jr90s = mpatches.Patch(color='moccasin', label='JR90 titles')
    jr95s = mpatches.Patch(color='paleturquoise', label='JR95 titles')
    others = mpatches.Patch(color='silver', label='Total titles')

    plt.legend(handles=[jr80s, jr90s, jr95s, others], bbox_to_anchor=(1, 1))   #moves legend outside plot
    plt.xticks(rotation=45)

    #NEED TO ADD LABELS TO PLOTS
    for i in stats_by_provider: 
        
        provider = i[0]
        jr80 = i[1]
        jr90 = i[2]
        jr95 = i[3]
        total_values = i[4]

        
        plot1 = plt.bar(provider, jr80, color='violet')
        plot2 = plt.bar(provider, jr90, bottom=jr80, color='moccasin')
        plot3 = plt.bar(provider, jr95, bottom=(jr80 + jr90), color='paleturquoise')
        plot4 = plt.bar(provider, total_values, bottom=(jr80 + jr90 + jr95), color='silver')
        

def figure1h():
    """Makes JR80, JR90, JR95 graph for all 6 big providers,
    splitting elsevier into Elseveier Freedom and Elsevier Subscribed.
    
    Plots Papers (Articles published by authors affiliated with your institution)
    
    JR80 = Journals which make up 80% of Papers
    JR90 = Journals which make up 90% of Papers
    JR95 = Journals which make up 95% of Papers
    
    Chart Type: Stacked Bar Graph
    Y-Axis: Percent of Total Titles
    Y-Axis Data Source: Original 1Figr Dataset, Journals Per Provider, Provider
                        Elsevier_2019, Subscribed Journal List 2019
    X-Axis: Provider Name
    X-Axis Data Source: Original 1Figr Dataset, Journals Per Provider, Provider
                        Elsevier_2019, Subscribed Journal List 2019
    """
    
    data = pd.read_excel(filename, sheet_name='Journals per Provider', skiprows=8)
    
    stats_by_provider = []

    providers = ['Sage', 'Springer', 'Taylor & Francis', 'Wiley']
    
    #make stats for existing providers
    for provider_name in providers:
        
        subset_by_provider = data.loc[data['Provider'] == provider_name]
        journals_data = subset_by_provider.groupby('Journal', as_index=False).sum().values.tolist()

        for i in journals_data:
            if i[0] == provider_name:
                journals_data.remove(i)                 #removing aggregator column data
        
        total_papers = 0
        total_journals = 0                         
        for i in journals_data:
            total_papers += i[7]
            total_journals += 1

        paper_tuples = [(i[0], i[7]) for i in journals_data]
        paper_tuples_sorted = sorted(paper_tuples, key = lambda i: i[1], reverse=True)      #sorts on second element of paper_tuples


        jr80_running_tally = 0                  #represents 80% of collections use
        jr90_running_tally = 0
        jr95_running_tally = 0
        jr80_highly_used_journals = []           #THIS HOLDS (JOURNAL NAME, PAPERS)
        jr90_highly_used_journals = []
        jr95_highly_used_journals = []
        
        for i in paper_tuples_sorted:
            if jr80_running_tally < (total_papers * 0.8):
                jr80_highly_used_journals.append(i)
                jr80_running_tally += i[1]

        for i in paper_tuples_sorted:
            if jr90_running_tally < (total_papers * 0.9):
                jr90_highly_used_journals.append(i)
                jr90_running_tally += i[1]

        for i in paper_tuples_sorted:
            if jr95_running_tally < (total_papers * 0.95):
                jr95_highly_used_journals.append(i)
                jr95_running_tally += i[1]
                
        jr80_score = (len(jr80_highly_used_journals))/(total_journals)
        jr90_score = (len(jr90_highly_used_journals))/(total_journals)
        jr90_score = (jr90_score - jr80_score)
        jr95_score = (len(jr95_highly_used_journals))/(total_journals)
        jr95_score = (jr95_score - (jr80_score + jr90_score))


        total_score = (1- (jr80_score+jr90_score+jr95_score))

        stats_by_provider.append((provider_name, jr80_score, jr90_score, jr95_score, total_score, len(jr80_highly_used_journals), len(jr90_highly_used_journals), len(jr95_highly_used_journals)))

    unmatched_collection_provider = rf.make_elsevier_unmatched_provider()
    unmatched_collection_provider['Provider Name'] = 'Elsevier Unmatched'   #need to create a column which holds provider name

    subscribed_titles_provider = rf.make_elsevier_subscribed_titles_provider()
    subscribed_titles_provider['Provider Name'] = 'Elsevier Subscribed'    #need to create a column which holds provider name
    
    freedom_collection_provider = rf.make_freedom_collection_provider()
    freedom_collection_provider['Provider Name'] = 'Elsevier Freedom'  #need to create a column which holds provider name
    
    elsevier_providers = [unmatched_collection_provider, subscribed_titles_provider, freedom_collection_provider]
    
    for provider_name in elsevier_providers:
        
        first_row = provider_name.iloc[1]
        name = first_row['Provider Name']    #need string of provider name for stats_by_provider
        
        journals_data = provider_name.groupby('Journal', as_index=False).sum().values.tolist()
        
        total_papers = 0
        total_journals = 0                         
        for i in journals_data:
            total_papers += i[7]
            total_journals += 1

        paper_tuples = [(i[0], i[7]) for i in journals_data]
        paper_tuples_sorted = sorted(paper_tuples, key = lambda i: i[1], reverse=True)      #sorts on second element of paper_tuples

        jr80_running_tally = 0                  #represents 80% of collections use
        jr90_running_tally = 0
        jr95_running_tally = 0
        jr80_highly_used_journals = []           #THIS HOLDS (JOURNAL NAME, PAPERS)
        jr90_highly_used_journals = []
        jr95_highly_used_journals = []
        
        for i in paper_tuples_sorted:
            if jr80_running_tally < (total_papers * 0.8):
                jr80_highly_used_journals.append(i)
                jr80_running_tally += i[1]

        for i in paper_tuples_sorted:
            if jr90_running_tally < (total_papers * 0.9):
                jr90_highly_used_journals.append(i)
                jr90_running_tally += i[1]

        for i in paper_tuples_sorted:
            if jr95_running_tally < (total_papers * 0.95):
                jr95_highly_used_journals.append(i)
                jr95_running_tally += i[1]
                
        jr80_score = (len(jr80_highly_used_journals))/(total_journals)
        jr90_score = (len(jr90_highly_used_journals))/(total_journals)
        jr90_score = (jr90_score - jr80_score)
        jr95_score = (len(jr95_highly_used_journals))/(total_journals)
        jr95_score = (jr95_score - (jr80_score + jr90_score))

        total_score = (1- (jr80_score+jr90_score+jr95_score))

        stats_by_provider.append((name, jr80_score, jr90_score, jr95_score, total_score, len(jr80_highly_used_journals), len(jr90_highly_used_journals), len(jr95_highly_used_journals)))
           
    #make plot
    plt.figure(num=None, figsize=(10, 10))
    plt.suptitle('Percentage of Articles Published by Provider (Papers)')
    plt.ylabel('Percent of total titles')
    plt.gca().yaxis.set_major_formatter(StrMethodFormatter('{x:,.0%}'))    #formats y axis as %

    jr80s = mpatches.Patch(color='violet', label='JR80 titles')
    jr90s = mpatches.Patch(color='moccasin', label='JR90 titles')
    jr95s = mpatches.Patch(color='paleturquoise', label='JR95 titles')
    others = mpatches.Patch(color='silver', label='Total titles')

    plt.legend(handles=[jr80s, jr90s, jr95s, others], bbox_to_anchor=(1, 1))   #moves legend outside plot
    plt.xticks(rotation=45)

    #NEED TO ADD LABELS TO PLOTS
    for i in stats_by_provider: 
        
        provider = i[0]
        jr80 = i[1]
        jr90 = i[2]
        jr95 = i[3]
        total_values = i[4]

        
        plot1 = plt.bar(provider, jr80, color='violet')
        plot2 = plt.bar(provider, jr90, bottom=jr80, color='moccasin')
        plot3 = plt.bar(provider, jr95, bottom=(jr80 + jr90), color='paleturquoise')
        plot4 = plt.bar(provider, total_values, bottom=(jr80 + jr90 + jr95), color='silver')


