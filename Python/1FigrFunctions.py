
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 14:03:39 2019

@author: ep9k
"""

import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter, PercentFormatter
import matplotlib.patches as mpatches
from operator import itemgetter


your_institution = 'UVA'   #Replace this string with your institution's preferred name. This is an example

#########################################################
#VRL presentation functions


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


def number_of_papers_published_per_year():
    """
    Creates line graph of the total number of papers published by all big 5 providers per year during 2008 - 2017

    Chart Type: Line Graph
    Y-Axis: Paper Count
    Y-Axis Data Source: JournalsPerProvider, Total papers in Scopus per journal/provider
    X-Axis: Year (2008, 2017)
    X-Axis Data Source:
    """
    
    data = pd.read_csv('JournalsPerProvider.csv', skiprows=8)
    
    big5 = ['Elsevier', 'Sage', 'Springer', 'Taylor & Francis', 'Wiley']
    
    papers_by_provider = []
    
    for provider_name in big5:
        
        subset_by_provider = data.loc[data['Provider'] == provider_name]
        
        papers_by_year = []
        
        total_2008 = subset_by_provider.total_2008.tolist()
        papers_by_year.append(total_2008[0])
        total_2009 = subset_by_provider.total_2009.tolist()
        papers_by_year.append(total_2009[0])
        total_2010 = subset_by_provider.total_2010.tolist()
        papers_by_year.append(total_2010[0])
        total_2011 = subset_by_provider.total_2011.tolist()
        papers_by_year.append(total_2011[0])
        total_2012 = subset_by_provider.total_2012.tolist()
        papers_by_year.append(total_2012[0])
        total_2013 = subset_by_provider.total_2013.tolist()
        papers_by_year.append(total_2013[0])
        total_2014 = subset_by_provider.total_2014.tolist()
        papers_by_year.append(total_2014[0])
        total_2015 = subset_by_provider.total_2015.tolist()
        papers_by_year.append(total_2015[0])
        total_2016 = subset_by_provider.total_2016.tolist()
        papers_by_year.append(total_2016[0])
        total_2017 = subset_by_provider.total_2017.tolist()
        papers_by_year.append(total_2017[0])

        papers_by_provider.append(papers_by_year)        
    
    years = ['2008','2009','2010','2011','2012','2013','2014','2015','2016','2017']

    plt.figure(num=None, figsize=(10, 10))
    plt.suptitle(f'Number of Total Papers by Year')
    plt.xlabel('Year')
    plt.ylabel('Paper Count')
    
    plt.plot(years, papers_by_provider[0], label='Elsevier')
    plt.plot(years, papers_by_provider[1], label='Sage')
    plt.plot(years, papers_by_provider[2], label='Springer')
    plt.plot(years, papers_by_provider[3], label='Taylor & Francis')
    plt.plot(years, papers_by_provider[4], label='Wiley')
    
    plt.legend()
    
#    plt.show()
    plt.savefig('test.png', bbox_inches='tight')      #saves image in working directory

# number_of_papers_published_per_year()

def number_papers_over_time():
    """
    Creates line graph of the number of authored publications at your institution in each of the big 5 providers per year during 2008-2017

    Chart Type: Line Graph
    Y-Axis: Paper Count
    Y-Axis Data Source: JournalsPerProvider, Papers per journal/provider by your institution's authors
    X-Axis: Year (2008, 2017)
    X-Axis Data Source:
    """

    data = pd.read_csv('JournalsPerProvider.csv', skiprows=8)
    
    big5 = ['Elsevier', 'Sage', 'Springer', 'Taylor & Francis', 'Wiley']
    
    publications_by_provider = []
    
    for provider_name in big5:
        
        subset_by_provider = data.loc[data['Provider'] == provider_name]
        
        publications_by_year = []
        
        papers_2008 = subset_by_provider.papers_2008.tolist()
        publications_by_year.append(papers_2008[0])
        papers_2009 = subset_by_provider.papers_2009.tolist()
        publications_by_year.append(papers_2009[0])
        papers_2010 = subset_by_provider.papers_2010.tolist()
        publications_by_year.append(papers_2010[0])
        papers_2011 = subset_by_provider.papers_2011.tolist()
        publications_by_year.append(papers_2011[0])
        papers_2012 = subset_by_provider.papers_2012.tolist()
        publications_by_year.append(papers_2012[0])
        papers_2013 = subset_by_provider.papers_2013.tolist()
        publications_by_year.append(papers_2013[0])
        papers_2014 = subset_by_provider.papers_2014.tolist()
        publications_by_year.append(papers_2014[0])
        papers_2015 = subset_by_provider.papers_2015.tolist()
        publications_by_year.append(papers_2015[0])
        papers_2016 = subset_by_provider.papers_2016.tolist()
        publications_by_year.append(papers_2016[0])
        papers_2017 = subset_by_provider.papers_2017.tolist()
        publications_by_year.append(papers_2017[0])
        
        publications_by_provider.append(publications_by_year)
            
    
    years = ['2008','2009','2010','2011','2012','2013','2014','2015','2016','2017']

    plt.figure(num=None, figsize=(10, 10))
    plt.suptitle(f'Number of Papers {your_institution} Authors each year')
    plt.xlabel('Year')
    plt.ylabel('Paper Count')

    #change this to be dynamic instead of hard coded
    plt.plot(years, publications_by_provider[0], label='Elsevier')
    plt.plot(years, publications_by_provider[1], label='Sage')
    plt.plot(years, publications_by_provider[2], label='Springer')
    plt.plot(years, publications_by_provider[3], label='Taylor & Francis')
    plt.plot(years, publications_by_provider[4], label='Wiley')
    
    plt.legend()

#    plt.show()    
    plt.savefig('test.png', bbox_inches='tight')      #saves image in working directory

# number_papers_over_time()

def oa_percent_papers_available_over_time():
    """
    Creates line graph of the ercentage of papers available Open Access (oa) for each of the big 5 providers per year during 2008-2017

    Chart Type: Line Graph
    Y-Axis: Percent Papers Available
    Y-Axis Data Source: JournalsPerProvider, % of OA papers in 1findr per journal/provider (intersection with Scopus)
    X-Axis: Year (2008, 2017)
    X-Axis Data Source:
    """
    
    data = pd.read_csv('JournalsPerProvider.csv', skiprows=8)
    
    big5 = ['Elsevier', 'Sage', 'Springer', 'Taylor & Francis', 'Wiley']
    
    oa_by_provider = []
    
    for provider_name in big5:
        
        subset_by_provider = data.loc[data['Provider'] == provider_name]
    
        oa_by_year = []

        oa_2008 = subset_by_provider.oa_2008.tolist()
        oa_by_year.append(oa_2008[0])
        oa_2009 = subset_by_provider.oa_2009.tolist()
        oa_by_year.append(oa_2009[0])
        oa_2010 = subset_by_provider.oa_2010.tolist()
        oa_by_year.append(oa_2010[0])
        oa_2011 = subset_by_provider.oa_2011.tolist()
        oa_by_year.append(oa_2011[0])
        oa_2012 = subset_by_provider.oa_2012.tolist()
        oa_by_year.append(oa_2012[0])
        oa_2013 = subset_by_provider.oa_2013.tolist()
        oa_by_year.append(oa_2013[0])
        oa_2014 = subset_by_provider.oa_2014.tolist()
        oa_by_year.append(oa_2014[0])
        oa_2015 = subset_by_provider.oa_2015.tolist()
        oa_by_year.append(oa_2015[0])
        oa_2016 = subset_by_provider.oa_2016.tolist()
        oa_by_year.append(oa_2016[0])
        oa_2017 = subset_by_provider.oa_2017.tolist()
        oa_by_year.append(oa_2017[0])
        
        oa_by_provider.append(oa_by_year)
        
    years = ['2008','2009','2010','2011','2012','2013','2014','2015','2016','2017']
        
    plt.figure(num=None, figsize=(10, 10))
    plt.suptitle(f'Percentage of OA Available Papers by Year in 2017 by Provider')
    plt.xlabel('Year')
    plt.ylabel('Percent Papers Available')
    plt.ylim(0, .45)
    
    plt.gca().yaxis.set_major_formatter(StrMethodFormatter('{x:,.0%}'))    #formats y axis as %

    plt.plot(years, oa_by_provider[0], label='Elsevier')
    plt.plot(years, oa_by_provider[1], label='Sage')
    plt.plot(years, oa_by_provider[2], label='Springer')
    plt.plot(years, oa_by_provider[3], label='Taylor & Francis')
    plt.plot(years, oa_by_provider[4], label='Wiley')
    
    plt.legend()

#    plt.show()    
    plt.savefig('test.png', bbox_inches='tight')      #saves image in working directory

# oa_percent_papers_available_over_time()

def references_over_time():
    """
    Creates line graph of Your institution's references by provider by year, referencing Scopus data, during 2008-2017

    Chart Type: Line Graph
    Y-Axis: Number References
    Y-Axis Data Source: JournalsPerProvider, References to journal/provider by your institution's authors (as measured in Scopus)
    X-Axis: Year (2008, 2017)
    X-Axis Data Source:

    References are defined as: Number of References made by researchers of your institution to an article from a given journal
    """

    

    data = pd.read_csv('JournalsPerProvider.csv', skiprows=8)
    
    big5 = ['Elsevier', 'Sage', 'Springer', 'Taylor & Francis', 'Wiley']

    ref_by_provider = []
    
    for provider_name in big5:
        
        subset_by_provider = data.loc[data['Provider'] == provider_name]
    
        ref_by_year = []
    
        ref_2008 = subset_by_provider.ref_2008.tolist()
        ref_by_year.append(ref_2008[0])
        ref_2009 = subset_by_provider.ref_2009.tolist()
        ref_by_year.append(ref_2009[0])
        ref_2010 = subset_by_provider.ref_2010.tolist()
        ref_by_year.append(ref_2010[0])
        ref_2011 = subset_by_provider.ref_2011.tolist()
        ref_by_year.append(ref_2011[0])
        ref_2012 = subset_by_provider.ref_2012.tolist()
        ref_by_year.append(ref_2012[0])
        ref_2013 = subset_by_provider.ref_2013.tolist()
        ref_by_year.append(ref_2013[0])
        ref_2014 = subset_by_provider.ref_2014.tolist()
        ref_by_year.append(ref_2014[0])
        ref_2015 = subset_by_provider.ref_2015.tolist()
        ref_by_year.append(ref_2015[0])
        ref_2016 = subset_by_provider.ref_2016.tolist()
        ref_by_year.append(ref_2016[0])
        ref_2017 = subset_by_provider.ref_2017.tolist()
        ref_by_year.append(ref_2017[0])
        
        ref_by_provider.append(ref_by_year)
        
    years = ['2008','2009','2010','2011','2012','2013','2014','2015','2016','2017']

    plt.figure(num=None, figsize=(10,10))
    plt.suptitle(f'Number of References Made by {your_institution} Researchers by Provider')
    plt.xlabel('Year')
    plt.ylabel('Number References')
    plt.ylim(0, 18000)

    plt.plot(years, ref_by_provider[0], label='Elsevier')
    plt.plot(years, ref_by_provider[1], label='Sage')
    plt.plot(years, ref_by_provider[2], label='Springer')
    plt.plot(years, ref_by_provider[3], label='Taylor & Francis')
    plt.plot(years, ref_by_provider[4], label='Wiley')

    plt.legend()  

#    plt.show()    
    plt.savefig('test.png', bbox_inches='tight')      #saves image in working directory

# references_over_time()

def big5_percent_jr5_of_jr1():
    """
    Creates bar graph the ratios of JR5 downloads to JR1 downloads for each of the Big 5 providers

    Chart Type: Bar Graph
    Y-Axis: Percent of Total (Percent of JR1 Downloads)
    Y-Axis Data Source: JournalsPerProvider, JR1 Downloads and JR5 Downloads columns
    X-Axis: Big 5 Providers
    X-Axis Data Source:

    JR5 downloads are 2017 articles downloaded in 2017.
    JR1 downloads are all years articles downloaded in 2017.
    We want to see what % of current articles people are downloading.
    """
    
    data = pd.read_csv('JournalsPerProvider.csv', skiprows=8)
    
    big5 = ['Elsevier', 'Sage', 'Springer', 'Taylor & Francis', 'Wiley']
    
    percent_jr5_of_jr1 = []
    
    for provider_name in big5:
        
        subset_by_provider = data.loc[data['Provider'] == provider_name]

        journals_data = subset_by_provider.groupby('Journal', as_index=False).sum().values.tolist()
        
        for i in journals_data:
            if i[0] == provider_name:
                jr1_total = i[2]
                jr5_total = i[3]
                ratio = jr5_total/jr1_total
                percent_jr5_of_jr1.append(ratio)
                
    mpl.rcParams['ytick.major.width'] = 1
    mpl.rcParams['xtick.major.width'] = 1
    plt.figure(num=None, figsize=(8,8))
    plt.suptitle(f'Percent JR5 downloads of JR1 downloads (for 2017)')
    plot = plt.bar(big5, percent_jr5_of_jr1, width=.8, color='green')   
    plt.ylabel('Percent of Total')
    plt.ylim(0, 1)  #changes top and bottom limit of y axis in plot

    plt.gca().yaxis.set_major_formatter(StrMethodFormatter('{x:,.0%}'))    #formats y axis as %

    for i in plot:
        score = i.get_height()
        
        plt.text(i.get_x() + i.get_width()/2, 
                 1.05 * score, 
                 '{:.1%}'.format(score),
                 ha='center',
                 va='bottom')

    # plt.show()        
    plt.savefig('test.png', bbox_inches='tight')      #saves image in working directory

big5_percent_jr5_of_jr1()

def jr1_big5_jr80_jr90_jr95_stacked_bar():
    """
    Creates stacked bar graph showing jr80, jr90, jr95 score for big 5 providers

    Chart Type: Stacked Bar Graph
    Y-Axis: Percent of Total Titles
    Y-Axis Data Source: JournalsPerProvider, Downloads JR1 2017
    X-Axis: Publisher Names
    X-Axis Data Source:

    JR80 is journals that make up 80% of your institution's jr1 downloads. JR90 are journals that make up 90% of your institution's jr1 downloads.
    JR95 are journals that make up 95% of your institution's jr1 downloads. These will all be plotted together.
    """
    
#    TODO: ADD LABELS TO PLOT
    
    data = pd.read_csv('JournalsPerProvider.csv', skiprows=8)


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
            total_jr1_downloads += i[2]
            total_journals += 1
            
        jr1_tuples = [(i[0], i[2]) for i in journals_data]
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
    plt.ylabel('Percent of Total Titles')
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

#    plt.show()        
    plt.savefig('test.png', bbox_inches='tight')      #saves image in working directory

# jr1_big5_jr80_jr90_jr95_stacked_bar()()

def jr5_big5_jr80_jr90_jr95_stacked_bar():
    """
    Creates stacked bar graph showing jr80, jr90, jr95 score for big 5 providers

    Chart Type: Stacked Bar Graph
    Y-Axis: Percent of Total Titles
    Y-Axis Data Source: JournalsPerProvider, Downloads JR1 2017
    X-Axis: Publisher Names
    X-Axis Data Source:

    JR80 is journals that make up 80% of your institution's jr1 downloads. JR90 are journals that make up 90% of your institution's jr1 downloads.
    JR95 are journals that make up 95% of your institution's jr1 downloads. These will all be plotted together.
    """

#    TODO: ADD LABELS TO PLOT

    
    data = pd.read_csv('JournalsPerProvider.csv', skiprows=8)

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
            total_jr5_downloads += i[3]
            total_journals += 1
            
        jr5_tuples = [(i[0], i[3]) for i in journals_data]
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

#    plt.show()
    plt.savefig('test.png', bbox_inches='tight')      #saves image in working directory

# jr5_big5_jr80_jr90_jr95_stacked_bar()

def references_big5_jr80_jr90_jr95_stacked_bar():
    """
    Creates stacked bar graph showing jr80, jr90, jr95 score for big 5 providers

    Chart Type: Stacked Bar Graph
    Y-Axis: Percent of Total Titles
    Y-Axis Data Source: JournalsPerProvider, Downloads JR1 2017
    X-Axis: Publisher Names
    X-Axis Data Source:

    JR80 is journals that make up 80% of your institution's references. JR90 are journals that make up 90% of your institution's references.
    JR95 are journals that make up 95% of your institution's references. These will all be plotted together.
    """

#    TODO: ADD LABELS TO PLOT

    
    data = pd.read_csv('JournalsPerProvider.csv', skiprows=8)           


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
            total_references += i[4]
            total_journals += 1
            
        reference_tuples = [(i[0], i[4]) for i in journals_data]
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
    plt.suptitle('Percentage of Titles Referenced by Provider')
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
        
#    plt.show()
    plt.savefig('test.png', bbox_inches='tight')      #saves image in working directory

# references_big5_jr80_jr90_jr95_stacked_bar()

def papers_big5_jr80_jr90_jr95_stacked_bar():
    """
    Creates stacked bar graph showing jr80, jr90, jr95 score for big 5 providers

    Chart Type: Stacked Bar Graph
    Y-Axis: Percent of Total Titles
    Y-Axis Data Source: JournalsPerProvider, Downloads JR1 2017
    X-Axis: Publisher Names
    X-Axis Data Source:

    JR80 is journals that make up 80% of your institution's papers. JR90 are journals that make up 90% of your institution's papers.
    JR95 are journals that make up 95% of your insitution's papers. These will all be plotted together.
    """

#    TODO: ADD LABELS TO PLOT

    
    data = pd.read_csv('JournalsPerProvider.csv', skiprows=8)           


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
            total_papers += i[5]
            total_journals += 1
            
        paper_tuples = [(i[0], i[5]) for i in journals_data]
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
    plt.suptitle(f'Percentage of Titles with Papers by {your_institution} Authors')
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

#    plt.show()
    plt.savefig('test.png', bbox_inches='tight')      #saves image in working directory

# papers_big5_jr80_jr90_jr95_stacked_bar()

#need to avoid hard coded list and populate list of providers dynamically
def total_references_per_year():
    """
    Creates line graph of the number of references made by institution's researchers, during 2008 to 2017.

    Chart Type: Line Graph
    Y-Axis: Number of References
    Y-Axis Data Source: JournalsPerProvider, References to journal/provider by your institution's authors (as measured in Scopus)
    X-Axis: Year (2008, 2017)
    X-Axis Data Source: Year (2008, 2017)

    References are defined as: Number of References made by researchers of your institution to an article from a given journal
    """
    

    data = pd.read_csv('JournalsPerProvider.csv', skiprows=8)
    
    providers = ['Wiley', 'U Chicago Press', 'Taylor & Francis', 'Springer', 'Sage', 'SPIE', 'Royal Society of Chemistry', 'Project MUSE',
                 'ProQuest', 'Oxford UP', 'Ovid', 'Modern Language Association', 'MIT Press', 'Karger', 'JSTOR', 'IOPscience', 'IEEE', 'Gale',
                 'Emerald', 'Elsevier', 'Ebsco', 'DeGruyter', 'Cambridge UP', 'Brill', 'BioOne', 'Association for Computing Machinery', 'Annual Reviews',
                 'American Society of Mechanical Engineers', 'American Society of Civil Engineers', 'American Physical Society', 'American Mathematical Society',
                 'American Institute of Aeronautics and Astronautics', 'American Chemical Society', 'AIP']
                 
    sum_2008 = 0
    sum_2009 = 0
    sum_2010 = 0
    sum_2011 = 0
    sum_2012 = 0
    sum_2013 = 0
    sum_2014 = 0
    sum_2015 = 0
    sum_2016 = 0
    sum_2017 = 0
    
    for provider_name in providers:
        
        subset_by_provider = data.loc[data['Provider'] == provider_name]
    
        ref_2008 = subset_by_provider.ref_2008.tolist()
        sum_2008 += ref_2008[0]
        ref_2009 = subset_by_provider.ref_2009.tolist()
        sum_2009 += ref_2009[0]
        ref_2010 = subset_by_provider.ref_2010.tolist()
        sum_2010 += ref_2010[0]
        ref_2011 = subset_by_provider.ref_2011.tolist()
        sum_2011 += ref_2011[0]
        ref_2012 = subset_by_provider.ref_2012.tolist()
        sum_2012 += ref_2012[0]
        ref_2013 = subset_by_provider.ref_2013.tolist()
        sum_2013 += ref_2013[0]
        ref_2014 = subset_by_provider.ref_2014.tolist()
        sum_2014 += ref_2014[0]
        ref_2015 = subset_by_provider.ref_2015.tolist()
        sum_2015 += ref_2015[0]
        ref_2016 = subset_by_provider.ref_2016.tolist()
        sum_2016 += ref_2016[0]
        ref_2017 = subset_by_provider.ref_2017.tolist()
        sum_2017 += ref_2017[0]
        
    totals_by_year = list((sum_2008, sum_2009, sum_2010, sum_2011, sum_2012, sum_2013, sum_2014, sum_2015, sum_2016, sum_2017))
    
    years = ['2008','2009','2010','2011','2012','2013','2014','2015','2016','2017']

    plt.figure(num=None, figsize=(10,10))
    plt.suptitle(f'Number of References Made by {your_institution} Researchers  \n (across all providers)')
    plt.xlabel('Year')
    plt.ylabel('Number References')
    plt.ylim(0, 120000)

    plt.plot(years, totals_by_year)

#    plt.show()    
    plt.savefig('test.png', bbox_inches='tight')      #saves image in working directory

# total_references_per_year()

###################################################################################
#JR1 functions. Chart sizing and labeling needs to be dynamic

def jr1_by_field_by_provider(provider_name):
    """
    Creates bar graph of the number of JR1 downloads by field for chosen provider.

    Chart Type: Bar Graph
    Y-Axis: Field
    Y-Axis Data Source: 
    X-Axis: Number of JR1 Downloads
    X-Axis Data Source: Journals Per Provider, Downloads JR1 2017

    User inputs provider name and dynamically generates chart for that provider
    """
    
    
    data = pd.read_csv('JournalsPerProvider.csv', skiprows=8)
    
    subset_by_provider = data.loc[data['Provider'] == provider_name]
    
    fields_data = subset_by_provider.groupby(['Field'], as_index=False).sum().values.tolist()
    fields = []
 
    for i in fields_data:
        fields.append(i[0])
    
    fields = list(reversed(fields))             #to add to bar graph in reverse alphabetical order so it looks nicer
    
    sums_by_field = subset_by_provider.groupby(['Field'])['Downloads JR1 2017'].sum()     #sum of downloads per field
    
    sums_by_field = list(reversed(sums_by_field))
    
    mpl.rcParams['ytick.major.width'] = 1
    mpl.rcParams['xtick.major.width'] = 1
    plt.figure(num=None, figsize=(8,8))
    plt.suptitle(f'JR1 Downloads by field for Provider: {provider_name}')
    plt.barh(fields, sums_by_field, height=.8, color='green')
    
    plt.grid()
    plt.show()

# jr1_by_field_by_provider("Elsevier")


def jr1_percent_field_by_provider(provider_name):
    """
    Creates bar graph of the percentage of JR1 downloads by field for chosen provider.

    Chart Type: Bar Graph
    Y-Axis: Field
    Y-Axis Data Source: 
    X-Axis: Percentage of JR1 Downloads
    X-Axis Data Source: Journals Per Provider, Downloads JR1 2017

    User inputs provider name and dynamically generates chart for that provider
    """
    data = pd.read_csv('JournalsPerProvider.csv', skiprows=8)
    
    subset_by_provider = data.loc[data['Provider'] == provider_name]
    
    fields_data = subset_by_provider.groupby(['Field'], as_index=False).sum().values.tolist()
    fields = []
 
    for i in fields_data:
        fields.append(i[0])
       
    fields = list(reversed(fields))             #to add to bar graph in reverse alphabetical order so it looks nicer        

    sums_by_field = subset_by_provider.groupby(['Field'])['Downloads JR1 2017'].sum().tolist()     #sum of downloads per field

    sums_by_field = list(reversed(sums_by_field))  
    
    total_downloads = sum(sums_by_field)
        
    percent_by_field = [round((i/total_downloads), 4) for i in sums_by_field]
   
    mpl.rcParams['ytick.major.width'] = 1
    mpl.rcParams['xtick.major.width'] = 1
    plt.figure(num=None, figsize=(8,8))
    plt.suptitle(f'Percent of total JR1 downloads by field for: {provider_name}')
    plt.barh(fields, percent_by_field, height=.8, color='green')
    plt.gca().xaxis.set_major_formatter(StrMethodFormatter('{x:,.0%}'))    #formats y axis as %
    plt.grid()
    plt.show() 

# jr1_percent_field_by_provider("Elsevier")

def jr1_jr80_value():
    """
    Creates bar graph of 'JR80' value by provider for JR1 downloads

    Chart Type: Bar Graph
    Y-Axis: Provider
    Y-Axis Data Source: 
    X-Axis: 'JR80' Value
    X-Axis Data Source: Journals Per Provider, Downloads JR1 2017

    JR80 is defined as: "Journals representing 80% of downloads for their respective provider"
    Here is how JR80 score is calculated:
        - Reads data for each provider individually
        - Finds total number of JR1 downloads
        - Sorts individual jornals by provider in order of number of downloads
        - Counts jr1 download values until count surpasses 80% of total jr1 downloads
        - Calculates JR80 score as number of journals required to reach 80% / total journals by provider
        - Charts JR80 score of all providers, with Big 5 in red
    """
    
    data = pd.read_csv('JournalsPerProvider.csv', skiprows=8)

    providers = data.groupby(['Provider'], as_index=False).sum().values.tolist()
    
    providers = [i[0] for i in providers]
        
    fluff_by_provider = []
    
    for provider_name in providers:
        subset_by_provider = data.loc[data['Provider'] == provider_name]
      
        journals_data = subset_by_provider.groupby('Journal', as_index=False).sum().values.tolist()
        for i in journals_data:
            if i[0] == provider_name:
                journals_data.remove(i)                 #removing aggregator column data
        
        total_jr1_downloads = 0
        total_journals = 0                         
        for i in journals_data:
            total_jr1_downloads += i[2]
            total_journals += 1

        jr1_tuples = [(i[0], i[2]) for i in journals_data]
        jr1_tuples_sorted = sorted(jr1_tuples, key = lambda i: i[1], reverse=True)       #sorts on second element of jr1_tuples

        running_tally = 0
        highly_used_journals = []           #THIS HOLDS (JOURNAL NAME, JR5_DOWNLOADS)
        for i in jr1_tuples_sorted:
            if running_tally < (total_jr1_downloads * 0.8):
                highly_used_journals.append(i)
                running_tally += i[1]
    
        fluff_score = (len(highly_used_journals))/(total_journals)
#        print(f"{provider_name} : {len(highly_used_journals)} of {total_journals} are JR80 journals")    #used to print each provider with number of journals included
            
        fluff_by_provider.append((provider_name, fluff_score))
        
    fluff_by_provider = sorted(fluff_by_provider, key=itemgetter(1), reverse=True)    #sorting by fluff_index score
    
    providers = [x[0] for x in fluff_by_provider]
    fluff_score = [x[1] for x in fluff_by_provider]
    
    
    #plot results
    mpl.rcParams['ytick.major.width'] = 1
    mpl.rcParams['xtick.major.width'] = 1
    plt.figure(num=None, figsize=(8,8))
    plt.suptitle(f'JR80 Score by provider (JR1 downloads)')
    plot = plt.barh(providers, fluff_score, height=.8, color='green')
    
    plot[13].set_color('red')
    plot[22].set_color('red')
    plot[23].set_color('red')
    plot[26].set_color('red')
    plot[31].set_color('red')

    
    #make custom plot legend
    big5 = mpatches.Patch(color='red', label='Big 5 Provider')
    
    plt.grid()
    plt.legend(handles=[big5])
    plt.show() 

# jr1_jr80_value()

def jr1_not_jr80_value():
    """
    Creates bar graph of 'Not-JR80' value by provider for JR1 downloads

    Chart Type: Bar Graph
    Y-Axis: Provider
    Y-Axis Data Source: 
    X-Axis: 'Not-JR80' Value
    X-Axis Data Source: Journals Per Provider, Downloads JR1 2017

    This is the inverse of the JR80 value.
    JR80 is defined as: "Journals representing 80% of downloads for their respective provider"
    Not-JR80 score is basically the rest of the journals that do not represent 80% of the use. 
    Here is how Not-JR80 score is calculated:
        - Reads data for each provider individually
        - Finds total number of JR1 downloads
        - Sorts individual jornals by provider in order of number of downloads
        - Counts jr1 download values until count surpasses 80% of total jr1 downloads
        - Calculates JR80 score as number of journals required to reach 80% / total journals by provider
        - Then takes 1 - this number to get the not_jr80 score. 
        - Charts not-JR80 score of all providers, with Big 5 in red
    """
    
    data = pd.read_csv('JournalsPerProvider.csv', skiprows=8)

    providers = data.groupby(['Provider'], as_index=False).sum().values.tolist()
    
    providers = [i[0] for i in providers]
        
    fluff_by_provider = []
    
    for provider_name in providers:
        subset_by_provider = data.loc[data['Provider'] == provider_name]
      
        journals_data = subset_by_provider.groupby('Journal', as_index=False).sum().values.tolist()
        for i in journals_data:
            if i[0] == provider_name:
                journals_data.remove(i)                 #removing aggregator column data
        
        total_jr1_downloads = 0
        total_journals = 0                         
        for i in journals_data:
            total_jr1_downloads += i[2]
            total_journals += 1

        jr1_tuples = [(i[0], i[2]) for i in journals_data]
        jr1_tuples_sorted = sorted(jr1_tuples, key = lambda i: i[1], reverse=True)       #sorts on second element of jr1_tuples

        running_tally = 0
        highly_used_journals = []           #THIS HOLDS (JOURNAL NAME, JR5_DOWNLOADS)
        for i in jr1_tuples_sorted:
            if running_tally < (total_jr1_downloads * 0.8):
                highly_used_journals.append(i)
                running_tally += i[1]
    
        fluff_score = 1 - ((len(highly_used_journals))/(total_journals))
            
        fluff_by_provider.append((provider_name, fluff_score))
        
    fluff_by_provider = sorted(fluff_by_provider, key=itemgetter(1), reverse=True)    #sorting by fluff_index score
    
    providers = [x[0] for x in fluff_by_provider]
    fluff_score = [x[1] for x in fluff_by_provider]
    
    #plot results
    mpl.rcParams['ytick.major.width'] = 1
    mpl.rcParams['xtick.major.width'] = 1
    plt.figure(num=None, figsize=(8,8))
    plt.suptitle(f'Not-JR80 Score by provider (JR1 downloads)')
    plot = plt.barh(providers, fluff_score, height=.8, color='green')
    
    plot[3].set_color('red')
    plot[8].set_color('red')
    plot[11].set_color('red')
    plot[12].set_color('red')
    plot[21].set_color('red')

    
    #make custom plot legend
    big5 = mpatches.Patch(color='red', label='Big 5 Provider')
    
    plt.grid()
    plt.legend(handles=[big5])
    plt.show() 

# jr1_not_jr80_value()

def jr1_jr80_big5_downloads():
    """
    Creates bar graph of 'JR80' value by provider for JR1 downloads for Big 5 providers only.

    Chart Type: Bar Graph
    Y-Axis: Provider
    Y-Axis Data Source: Big 5 Providers
    X-Axis: 'JR80' Value
    X-Axis Data Source: Journals Per Provider, Downloads JR1 2017

    This is the inverse of the JR80 value.
    JR80 is defined as: "Journals representing 80% of downloads for their respective provider"
    Not-JR80 score is basically the rest of the journals that do not represent 80% of the use. 
    Here is how Not-JR80 score is calculated:
        - Reads data for each provider individually
        - Finds total number of JR1 downloads
        - Sorts individual jornals by provider in order of number of downloads
        - Counts jr1 download values until count surpasses 80% of total jr1 downloads
        - Calculates JR80 score as number of journals required to reach 80% / total journals by provider
        - Then takes 1 - this number to get the not_jr80 score. 
        - Charts not-JR80 score of all providers, with Big 5 in red
    """

    data = pd.read_csv('JournalsPerProvider.csv', skiprows=8)

    big5 = ['Elsevier', 'Taylor & Francis', 'Sage', 'Springer', 'Wiley']
    
    fluff_by_provider = []
    
    for provider_name in big5:
        
        subset_by_provider = data.loc[data['Provider'] == provider_name]
        
        journals_data = subset_by_provider.groupby('Journal', as_index=False).sum().values.tolist()
        for i in journals_data:
            if i[0] == provider_name:
                journals_data.remove(i)                 #removing aggregator column data                
        
        total_jr1_downloads = 0
        total_journals = 0                         
        for i in journals_data:
            total_jr1_downloads += i[2]
            total_journals += 1

        jr1_tuples = [(i[0], i[2]) for i in journals_data]
        jr1_tuples_sorted = sorted(jr1_tuples, key = lambda i: i[1], reverse=True)       #sorts on second element of jr1_tuples

        running_tally = 0
        highly_used_journals = []           #THIS HOLDS (JOURNAL NAME, JR5_DOWNLOADS)
        for i in jr1_tuples_sorted:
            if running_tally < (total_jr1_downloads * 0.8):
                highly_used_journals.append(i)
                running_tally += i[1]
    
        fluff_score = (len(highly_used_journals))/(total_journals)
        print(f"{provider_name} : {len(highly_used_journals)} of {total_journals} are JR80 journals")    #used to print each provider with number of journals included
            
        fluff_by_provider.append((provider_name, fluff_score))
       
    fluff_by_provider = sorted(fluff_by_provider, key=itemgetter(1), reverse=True)    #sorting by fluff_index score
    
    providers = [x[0] for x in fluff_by_provider]
    fluff_score = [x[1] for x in fluff_by_provider]
    
    #plot results
    mpl.rcParams['ytick.major.width'] = 1
    mpl.rcParams['xtick.major.width'] = 1
    plt.figure(num=None, figsize=(8,8))
    plt.suptitle(f'Percentage of Titles Which Make 80% of JR1 Downloads \n (JR80 Score by Provider)')
    plot = plt.barh(providers, fluff_score, height=.8, color='green')
    
    for i in plot:
        score = i.get_width()
        score = round(score, 4)
        
        plt.text(i.get_width() - .02, 
                 i.get_y() + .35,
                 '{:.2%}'.format(score),   #formats score as percentage
                 ha='center',
                 va='center')
    plt.show()

# jr1_jr80_big5_downloads()

def jr1_jr80_big5_citations():
	""" Creates bar graph of number of citations by provider for Big 5 providers only. 
	
	Chart Type: Bar Graph 
	Y-Axis: Provider 
	Y-Axis Data Source: Big 5 Providers
	X-Axis: Number of Citations 
	X-Axis Data Source: Journals Per Provider, Downloads JR1 2017 
	
	Citations are measured as publications that have cited an article authored by someone affiliated with your institution 
	"""

	data = pd.read_csv('JournalsPerProvider.csv', skiprows=8)

	big5 = ['Elsevier', 'Taylor & Francis', 'Sage', 'Springer', 'Wiley']    

	references_by_provider = []

	for provider_name in big5:
	    
	    subset_by_provider = data.loc[data['Provider'] == provider_name]

	    journals_data = subset_by_provider.groupby('Journal', as_index=False).sum().values.tolist()
	    for i in journals_data:
	        if i[0] == provider_name:
	            total_references = i[4]
	            references_by_provider.append(total_references)
	            
	mpl.rcParams['ytick.major.width'] = 1
	mpl.rcParams['xtick.major.width'] = 1
	plt.figure(num=None, figsize=(8,8))
	plt.suptitle(f"Citations by Provider \n (# of your {your_institution} Authored Papers Cited)")
	plot = plt.barh(big5, references_by_provider, height=.8, color='green')

	for i in plot:
	    score = i.get_width()
	    
	    plt.text(i.get_width() - 5500,          #sets x axis position of labels
	             i.get_y() + .35,
	             score,
	             ha='center',
	             va='center')
	plt.show()

# jr1_jr80_big5_citations()

def jr1_jr80_big5_publications():
    """ Creates bar graph of number of papers/publications by provider for Big 5 providers only. 
	
	Chart Type: Bar Graph 
	Y-Axis: Provider 
	Y-Axis Data Source: Big 5 Providers
	X-Axis: Number of Papers/Publications 
	X-Axis Data Source: 
	
    Publications are measured as papers with at least one author from your institution
    """
    
    data = pd.read_csv('JournalsPerProvider.csv', skiprows=8)
    
    big5 = ['Elsevier', 'Taylor & Francis', 'Sage', 'Springer', 'Wiley']    
#    big5 = ['AIP', 'American Chemical Society']
    publications_by_provider = []
    
    for provider_name in big5:
        
        subset_by_provider = data.loc[data['Provider'] == provider_name]

        journals_data = subset_by_provider.groupby('Journal', as_index=False).sum().values.tolist()
        for i in journals_data:
            if i[0] == provider_name:
                total_publications = i[5]
                publications_by_provider.append(total_publications)
                
    mpl.rcParams['ytick.major.width'] = 1
    mpl.rcParams['xtick.major.width'] = 1
    plt.figure(num=None, figsize=(8,8))
    plt.suptitle(f"Publications by Provider \n (# of your {your_institution} Authored Papers Published)")
    plot = plt.barh(big5, publications_by_provider, height=.8, color='green')
    
    for i in plot:
        score = i.get_width()
        
        plt.text(i.get_width() - 275,           #sets x axis position of labels
                 i.get_y() + .35,
                 score,
                 ha='center',
                 va='center')

    plt.show()

# jr1_jr80_big5_publications()

def jr1_big5_by_field(field_choice):
    """ Creates bar graph of percentage of jr1 downloads by provider for input field for Big 5 providers only. 
	
	Chart Type: Bar Graph 
	Y-Axis: Provider 
	Y-Axis Data Source: 
	X-Axis: Percentage of JR1 Downloads
	X-Axis Data Source: Journals Per Provider, Downloads JR1 2017 
	
    Looks at jr1 downloads by field for the big 5 providers. Charts % use by field for each of the big 5 providers
    """
    
    data = pd.read_csv('JournalsPerProvider.csv', skiprows=8)

    big5 = ['Elsevier', 'Taylor & Francis', 'Sage', 'Springer', 'Wiley']

    big5_data = []
    for provider_name in big5:
        provider_subset = data.loc[data['Provider'] == provider_name]
        
        provider_list = provider_subset.groupby(['Provider', 'Field'], as_index=False).sum().values.tolist()
        for i in provider_list:
            if i[1] == field_choice:
                big5_data.append((i[0], i[1], i[3]))
    print(big5_data)
            

    big5_packages = [x[0] for x in big5_data]
    big5_total_by_field = [x[2] for x in big5_data]
    
    mpl.rcParams['ytick.major.width'] = 1
    mpl.rcParams['xtick.major.width'] = 1
    plt.figure(num=None, figsize=(8,8))
    plt.suptitle(f'Big 5 Providers, JR1 downloads by field: {field_choice}')
    plt.barh(big5_packages, big5_total_by_field, height=.8, color='green')
    plt.grid()
    plt.show() 
        
  
     
#########################################################        
#JR5 functions

def jr5_by_field_by_provider(provider_name):
    """ Creates bar graph of percentage of jr5 downloads by provider for input field for Big 5 providers only. 
	
	Chart Type: Bar Graph 
	Y-Axis: Provider 
	Y-Axis Data Source: 
	X-Axis: Percentage of JR5 Downloads
	X-Axis Data Source: Journals Per Provider, Downloads JR5 2017 in 2017
	
    """
    
    data = pd.read_csv('JournalsPerProvider.csv', skiprows=8)
    
    subset_by_provider = data.loc[data['Provider'] == provider_name]
#    
    fields_data = subset_by_provider.groupby(['Field'], as_index=False).sum().values.tolist()
    fields = []
 
    for i in fields_data:
        fields.append(i[0])
    
    fields = list(reversed(fields))             #to add to bar graph in reverse alphabetical order so it looks nicer
    
    sums_by_field = subset_by_provider.groupby(['Field'])['Downloads JR5 2017 in 2017'].sum()     #sum of downloads per field
    
    sums_by_field = list(reversed(sums_by_field))
    
    mpl.rcParams['ytick.major.width'] = 1
    mpl.rcParams['xtick.major.width'] = 1
    plt.figure(num=None, figsize=(8,8))
    plt.suptitle(f'JR5 Downloads by field for Provider: {provider_name}')
    plt.barh(fields, sums_by_field, height=.8, color='green')
    plt.grid()
    plt.show() 

# jr5_by_field_by_provider("Elsevier")
    
def jr5_percent_field_by_provider(provider_name):
	"""
	Creates bar graph of the percentage of JR5 downloads by field for chosen provider.

	Chart Type: Bar Graph
	Y-Axis: Field
	Y-Axis Data Source: 
	X-Axis: Percentage of JR5 Downloads
	X-Axis Data Source: Journals Per Provider, Downloads JR5 2017 in 2017
	"""
	data = pd.read_csv('JournalsPerProvider.csv', skiprows=8)
	
	subset_by_provider = data.loc[data['Provider'] == provider_name]

	fields_data = subset_by_provider.groupby(['Field'], as_index=False).sum().values.tolist()
	fields = []

	for i in fields_data:
	    fields.append(i[0])

	fields = list(reversed(fields))             #to add to bar graph in reverse alphabetical order so it looks nicer

	sums_by_field = subset_by_provider.groupby(['Field'])['Downloads JR5 2017 in 2017'].sum().tolist()     #sum of downloads per field

	sums_by_field = list(reversed(sums_by_field))

	total_downloads = sum(sums_by_field)
	    
	percent_by_field = [round((i/total_downloads), 4) for i in sums_by_field]

	mpl.rcParams['ytick.major.width'] = 1
	mpl.rcParams['xtick.major.width'] = 1
	plt.figure(num=None, figsize=(8,8))
	plt.suptitle(f'Percent of total JR5 downloads by field for: {provider_name}')
	plt.barh(fields, percent_by_field, height=.8, color='green')
	plt.grid()
	plt.show()     

    
    
def jr5_big5_by_field(field_choice):
	"""
	Creates bar graph of percentage of jr1 downloads by provider for input field for Big 5 providers only. 
	
	Chart Type: Bar Graph 
	Y-Axis: Provider 
	Y-Axis Data Source: 
	X-Axis: Percentage of JR1 Downloads
	X-Axis Data Source: Journals Per Provider, Downloads JR1 2017 
	
    Looks at jr1 downloads by field for the big 5 providers. Charts % use by field for each of the big 5 providers
    """
	data = pd.read_csv('JournalsPerProvider.csv', skiprows=8)

	big5 = ['Elsevier', 'Taylor & Francis', 'Sage', 'Springer', 'Wiley']
	big5_data = []
	for provider_name in big5:
	    provider_subset = data.loc[data['Provider'] == provider_name]
	    
	    provider_list = provider_subset.groupby(['Provider', 'Field'], as_index=False).sum().values.tolist()
	    for i in provider_list:
	        if i[1] == field_choice:
	            big5_data.append((i[0], i[1], i[4]))

	big5_packages = [x[0] for x in big5_data]
	big5_total_by_field = [x[2] for x in big5_data]

	mpl.rcParams['ytick.major.width'] = 1
	mpl.rcParams['xtick.major.width'] = 1
	plt.figure(num=None, figsize=(8,8))
	plt.suptitle(f'Big 5 Providers, JR5 downloads by field: {field_choice}')
	plt.barh(big5_packages, big5_total_by_field, height=.8, color='green')
	plt.grid()
	plt.show()
    


###########################################################
#other functions. Chart sizing and labeling needs to be dynamic

def journals_by_domain():
	""" 
	Creates bar graph of the number of journals assigned to each domain. 

	Chart Type: Bar Graph 
	Y-Axis: Domain 
	Y-Axis Data Source: Journals Per Provider, Domain
	X-Axis: Count of Domain
	X-Axis Data Source: Journals Per Provider, Domain 
	"""
	

	data = pd.read_csv('JournalsPerProvider.csv', skiprows=8)

	domains_list = data.Domain.tolist()

	counted_domains = pd.Series(domains_list).value_counts().reset_index().values.tolist()

	domains = [x[0] for x in counted_domains]
	counts = [x[1] for x in counted_domains]

	mpl.rcParams['ytick.major.width'] = 1
	mpl.rcParams['xtick.major.width'] = 1
	plt.figure(num=None, figsize=(8,8))
	plt.suptitle('Journals by Domain')
	plt.barh(domains, counts, height=.8, color='green')
	plt.grid()
	plt.show()
    
# journals_by_domain()
    
def journals_by_field():
    """ 
    Creates bar graph of the number of journal assigned to each field. 

	Chart Type: Bar Graph 
	Y-Axis: Field 
	Y-Axis Data Source: Journals Per Provider, Field
	X-Axis: Count of Field
	X-Axis Data Source: Journals Per Provider, Field
	"""
    
    
    data = pd.read_csv('JournalsPerProvider.csv', skiprows=8)
    
    fields_list = data.Field.tolist()

    counted_fields = pd.Series(fields_list).value_counts().reset_index().values.tolist()
    
    fields = [x[0] for x in counted_fields]
    counts = [x[1] for x in counted_fields]
    
    mpl.rcParams['ytick.major.width'] = 1
    mpl.rcParams['xtick.major.width'] = 1
    plt.figure(num=None, figsize=(8,8))
    plt.suptitle('Journals by field')
    plt.barh(fields, counts, height=.8, color='green')
    plt.grid()
    plt.show()

# journals_by_field()

def journals_by_field_big5():
	""" 
	Creates bar graph of the number of journals assgined to each field for Big 5 Providers. 

	Chart Type: Bar Graph 
	Y-Axis: Field 
	Y-Axis Data Source: Journals Per Provider, Field
	X-Axis: Count of Field
	X-Axis Data Source: Journals Per Provider, Field
	"""

	data = pd.read_csv('JournalsPerProvider.csv', skiprows=8)

	providers_list = data.Provider.tolist()
	fields_list = data.Field.tolist()

	zipped = list(zip(providers_list, fields_list))

	big5 = ['Elsevier', 'Wiley', 'Springer', 'Taylor & Francis', 'Sage']
	big5_data = []

	for i in zipped:
	    if i[0] in big5:
	        big5_data.append(i)
	        
	fields_only = [x[1] for x in big5_data]

	counted_fields = pd.Series(fields_only).value_counts().reset_index().values.tolist()

	fields = [x[0] for x in counted_fields]
	counts = [x[1] for x in counted_fields]

	mpl.rcParams['ytick.major.width'] = 1
	mpl.rcParams['xtick.major.width'] = 1
	plt.figure(num=None, figsize=(8,8))
	plt.suptitle('Journals by field (Big5 Providers)')
	plt.barh(fields, counts, height=.8, color='green')
	plt.grid()
	plt.show() 



def journals_by_field_other_providers():
	""" 
	Creates bar graph of the number journals assigned to each field for non-Big 5 Providers. 

	Chart Type: Bar Graph 
	Y-Axis: Field 
	Y-Axis Data Source: Journals Per Provider, Feild
	X-Axis: Count of Field
	X-Axis Data Source: Data Source: Journals Per Provider, Field
	"""
    
	data = pd.read_csv('JournalsPerProvider.csv', skiprows=8)

	providers_list = data.Provider.tolist()
	fields_list = data.Field.tolist()

	zipped = list(zip(providers_list, fields_list))

	big5 = ['Elsevier', 'Wiley', 'Springer', 'Taylor & Francis', 'Sage']
	not_big5_data = []

	for i in zipped:
	    if i[0] not in big5:
	        not_big5_data.append(i)
	        
	fields_only = [x[1] for x in not_big5_data]

	counted_fields = pd.Series(fields_only).value_counts().reset_index().values.tolist()

	fields = [x[0] for x in counted_fields]
	counts = [x[1] for x in counted_fields]

	mpl.rcParams['ytick.major.width'] = 1
	mpl.rcParams['xtick.major.width'] = 1
	plt.figure(num=None, figsize=(8,8))
	plt.suptitle('Journals by Field (Not Big5 Providers)')
	plt.barh(fields, counts, height=.8, color='green')
	plt.grid()
	plt.show() 


    
def references_by_field_by_provider(provider_name):
	""" 
	Creates bar graph of the number of references in each field for input provider. 

	Chart Type: Bar Graph 
	Y-Axis: Field 
	Y-Axis Data Source: Journals Per Provider, Domain
	X-Axis: Number of References
	X-Axis Data Source: Journals Per Provider, References

    References are defined as the number of references made by researchers of your institution to an article from a given journal.'
     """
    
	data = pd.read_csv('JournalsPerProvider.csv', skiprows=8)

	subset_by_provider = data.loc[data['Provider'] == provider_name]

	fields_data = subset_by_provider.groupby(['Field'], as_index=False).sum().values.tolist()
	fields = []

	for i in fields_data:
	    fields.append(i[0])
	    
	fields = list(reversed(fields))             #to add to bar graph in reverse alphabetical order so it looks nicer

	sums_by_field = subset_by_provider.groupby(['Field'])['References'].sum().tolist()     #sum of downloads per field

	sums_by_field = list(reversed(sums_by_field))

	mpl.rcParams['ytick.major.width'] = 1
	mpl.rcParams['xtick.major.width'] = 1
	plt.figure(num=None, figsize=(8,8))
	plt.suptitle(f"References by {your_institution} Authors by field for Provider: {provider_name}")
	plt.barh(fields, sums_by_field, height=.8, color='green')
	plt.grid()
	plt.show() 
    

def papers_by_field_by_provider(provider_name):
    """ 
	Creates bar graph of the number of papers in each field for input provider. 

	Chart Type: Bar Graph 
	Y-Axis: Field 
	Y-Axis Data Source: Journals Per Provider, Field
	X-Axis: Number of Publications
	X-Axis Data Source:  Journals Per Provider, Papers

    Papers are defined as the number of documents published in peer-reviewed journals indexed in Scopus and for which at least one author was affiliated to your institution.
    """
    
    data = pd.read_csv('JournalsPerProvider.csv', skiprows=8)
    
    subset_by_provider = data.loc[data['Provider'] == provider_name]
    
    fields_data = subset_by_provider.groupby(['Field'], as_index=False).sum().values.tolist()
    fields = []
 
    for i in fields_data:
        fields.append(i[0])
   
    fields = list(reversed(fields))             #to add to bar graph in reverse alphabetical order so it looks nicer
    
    sums_by_field = subset_by_provider.groupby(['Field'])['Papers'].sum().tolist()     #sum of downloads per field
    
    sums_by_field = list(reversed(sums_by_field))
    
    mpl.rcParams['ytick.major.width'] = 1
    mpl.rcParams['xtick.major.width'] = 1
    plt.figure(num=None, figsize=(8,8))
    plt.suptitle(f"Publications by {your_institution} Authors by field for Provider: {provider_name}")
    plt.barh(fields, sums_by_field, height=.8, color='green')
    plt.grid()
    plt.show()








