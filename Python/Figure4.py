#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 13:40:09 2019

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

def figure4a_all_uva_references():
    """UVA references by year, referencing Scopus data.
    Looks at columns under 'References to journal/provider by your institution's authors (as measured in Scopus)
    References are defined as: Number of References made by researchers of your institution to an article from a given journal
    
    Chart Type: Line graph
    Y-Axis: Number of References
    Y-Axis Data Source: Original 1Figr Dataset 
    
    X-Axis: Year
    X-Axis Data Source: Original 1Figr Dataset
    """
    

    data = pd.read_excel(filename, sheet_name='Journals per Provider', skiprows=8)
    
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
            
        ref_2008 = subset_by_provider['2008.1'].tolist()
        sum_2008 += ref_2008[0]
        ref_2009 = subset_by_provider['2009.1'].tolist()
        sum_2009 += ref_2009[0]
        ref_2010 = subset_by_provider['2010.1'].tolist()
        sum_2010 += ref_2010[0]
        ref_2011 = subset_by_provider['2011.1'].tolist()
        sum_2011 += ref_2011[0]
        ref_2012 = subset_by_provider['2012.1'].tolist()
        sum_2012 += ref_2012[0]
        ref_2013 = subset_by_provider['2013.1'].tolist()
        sum_2013 += ref_2013[0]
        ref_2014 = subset_by_provider['2014.1'].tolist()
        sum_2014 += ref_2014[0]
        ref_2015 = subset_by_provider['2015.1'].tolist()
        sum_2015 += ref_2015[0]
        ref_2016 = subset_by_provider['2016.1'].tolist()
        sum_2016 += ref_2016[0]
        ref_2017 = subset_by_provider['2017.1'].tolist()
        sum_2017 += ref_2017[0]
        
    totals_by_year = list((sum_2008, sum_2009, sum_2010, sum_2011, sum_2012, sum_2013, sum_2014, sum_2015, sum_2016, sum_2017))
    
    years = ['2008','2009','2010','2011','2012','2013','2014','2015','2016','2017']

    plt.figure(num=None, figsize=(10,10))
    plt.suptitle(f'Number of References Made by {your_institution} Researchers \n (across all providers)')
    plt.xlabel('Year')
    plt.ylabel('Number References')
    plt.ylim(0, 120000)
    
    plt.plot(years, totals_by_year)



def figure4a_references():
    """UVA references by provider by year, referencing Scopus data.
    Looks at columns under 'References to journal/provider by your institution's authors (as measured in Scopus)
    References are defined as: Number of References made by researchers of your institution to an article from a given journal
    
    Chart Type: Line graph
    Y-Axis: Number of References
    Y-Axis Data Source: Original 1Figr Dataset 
    
    X-Axis: Year
    X-Axis Data Source: Original 1Figr Dataset
    """
    

    data = pd.read_excel(filename, sheet_name='Journals per Provider', skiprows=8)
    
    big5 = ['Elsevier', 'Sage', 'Springer', 'Taylor & Francis', 'Wiley']

    ref_by_provider = []
    
    for provider_name in big5:
        
        subset_by_provider = data.loc[data['Provider'] == provider_name]
    
        ref_by_year = []
    
        ref_2008 = subset_by_provider['2008.1'].tolist()
        ref_by_year.append(ref_2008[0])
        ref_2009 = subset_by_provider['2009.1'].tolist()
        ref_by_year.append(ref_2009[0])
        ref_2010 = subset_by_provider['2010.1'].tolist()
        ref_by_year.append(ref_2010[0])
        ref_2011 = subset_by_provider['2011.1'].tolist()
        ref_by_year.append(ref_2011[0])
        ref_2012 = subset_by_provider['2012.1'].tolist()
        ref_by_year.append(ref_2012[0])
        ref_2013 = subset_by_provider['2013.1'].tolist()
        ref_by_year.append(ref_2013[0])
        ref_2014 = subset_by_provider['2014.1'].tolist()
        ref_by_year.append(ref_2014[0])
        ref_2015 = subset_by_provider['2015.1'].tolist()
        ref_by_year.append(ref_2015[0])
        ref_2016 = subset_by_provider['2016.1'].tolist()
        ref_by_year.append(ref_2016[0])
        ref_2017 = subset_by_provider['2017.1'].tolist()
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


def figure4a_percentage():
    """UVA references by provider by year, referencing Scopus data.
    Looks at columns under 'References to journal/provider by your institution's authors (as measured in Scopus)
    References are defined as: Number of References made by researchers of your institution to an article from a given journal
    
    Chart Type: Line graph
    Y-Axis: Number of References
    Y-Axis Data Source: Original 1Figr Dataset 
    
    X-Axis: Year
    X-Axis Data Source: Original 1Figr Dataset
    """
    

    data = pd.read_excel(filename, sheet_name='Journals per Provider', skiprows=8)
    
    providers = ['Wiley', 'U Chicago Press', 'Taylor & Francis', 'Springer', 'Sage', 'SPIE', 'Royal Society of Chemistry', 'Project MUSE',
                 'ProQuest', 'Oxford UP', 'Ovid', 'Modern Language Association', 'MIT Press', 'Karger', 'JSTOR', 'IOPscience', 'IEEE', 'Gale',
                 'Emerald', 'Elsevier', 'Ebsco', 'DeGruyter', 'Cambridge UP', 'Brill', 'BioOne', 'Association for Computing Machinery', 'Annual Reviews',
                 'American Society of Mechanical Engineers', 'American Society of Civil Engineers', 'American Physical Society', 'American Mathematical Society',
                 'American Institute of Aeronautics and Astronautics', 'American Chemical Society', 'AIP']

                 
    big5 = ['Elsevier', 'Sage', 'Springer', 'Taylor & Francis', 'Wiley']

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
    
        ref_2008 = subset_by_provider['2008.1'].tolist()
        sum_2008 += ref_2008[0]
        ref_2009 = subset_by_provider['2009.1'].tolist()
        sum_2009 += ref_2009[0]
        ref_2010 = subset_by_provider['2010.1'].tolist()
        sum_2010 += ref_2010[0]
        ref_2011 = subset_by_provider['2011.1'].tolist()
        sum_2011 += ref_2011[0]
        ref_2012 = subset_by_provider['2012.1'].tolist()
        sum_2012 += ref_2012[0]
        ref_2013 = subset_by_provider['2013.1'].tolist()
        sum_2013 += ref_2013[0]
        ref_2014 = subset_by_provider['2014.1'].tolist()
        sum_2014 += ref_2014[0]
        ref_2015 = subset_by_provider['2015.1'].tolist()
        sum_2015 += ref_2015[0]
        ref_2016 = subset_by_provider['2016.1'].tolist()
        sum_2016 += ref_2016[0]
        ref_2017 = subset_by_provider['2017.1'].tolist()
        sum_2017 += ref_2017[0]

    totals_by_year = list((sum_2008, sum_2009, sum_2010, sum_2011, sum_2012, sum_2013, sum_2014, sum_2015, sum_2016, sum_2017))   #list of total references by year
        
    ref_by_provider = []
    
    for provider_name in big5:
        
        subset_by_provider = data.loc[data['Provider'] == provider_name]
    
        ref_by_year = []
    
        ref_2008 = subset_by_provider['2008.1'].tolist()
        ref_by_year.append(ref_2008[0])
        ref_2009 = subset_by_provider['2009.1'].tolist()
        ref_by_year.append(ref_2009[0])
        ref_2010 = subset_by_provider['2010.1'].tolist()
        ref_by_year.append(ref_2010[0])
        ref_2011 = subset_by_provider['2011.1'].tolist()
        ref_by_year.append(ref_2011[0])
        ref_2012 = subset_by_provider['2012.1'].tolist()
        ref_by_year.append(ref_2012[0])
        ref_2013 = subset_by_provider['2013.1'].tolist()
        ref_by_year.append(ref_2013[0])
        ref_2014 = subset_by_provider['2014.1'].tolist()
        ref_by_year.append(ref_2014[0])
        ref_2015 = subset_by_provider['2015.1'].tolist()
        ref_by_year.append(ref_2015[0])
        ref_2016 = subset_by_provider['2016.1'].tolist()
        ref_by_year.append(ref_2016[0])
        ref_2017 = subset_by_provider['2017.1'].tolist()
        ref_by_year.append(ref_2017[0])
        
        ref_by_provider.append(ref_by_year)

    all_percent_by_provider_of_total_by_year = []           #for each of big 5 providers, stores list of % of UVA references each provider made up of ALL UVA references for that year

    for i in ref_by_provider:
        individual_percent_total_by_provider_per_year = []
        
        zipped = zip(totals_by_year, i)
        for i in zipped:
            individual_percent_total_by_provider_per_year.append(i[1]/i[0])
        
        all_percent_by_provider_of_total_by_year.append(individual_percent_total_by_provider_per_year)
        
    years = ['2008','2009','2010','2011','2012','2013','2014','2015','2016','2017']


    plt.figure(num=None, figsize=(10,10))
    plt.suptitle(f'Percent of References by {your_institution} by Provider \n (as percent of all UVA references by year)')
    plt.xlabel('Year')
    plt.ylabel('Percent of References')
    plt.gca().yaxis.set_major_formatter(StrMethodFormatter('{x:,.0%}'))    #formats y axis as %

    plt.plot(years, all_percent_by_provider_of_total_by_year[0], label='Elsevier')
    plt.plot(years, all_percent_by_provider_of_total_by_year[1], label='Sage')
    plt.plot(years, all_percent_by_provider_of_total_by_year[2], label='Springer')
    plt.plot(years, all_percent_by_provider_of_total_by_year[3], label='Taylor & Francis')
    plt.plot(years, all_percent_by_provider_of_total_by_year[4], label='Wiley')


def figure4b_all_uva_references():
    """UVA references by year, referencing Scopus data.
    Looks at columns under 'References to journal/provider by your institution's authors (as measured in Scopus)
    References are defined as: Number of References made by researchers of your institution to an article from a given journal
    
    Chart Type: Line graph
    Y-Axis: Number of References
    Y-Axis Data Source: Original 1Figr Dataset 
    
    X-Axis: Year
    X-Axis Data Source: Original 1Figr Dataset
    """
    

    data = pd.read_excel(filename, sheet_name='Journals per Provider', skiprows=8)
    
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
            
        ref_2008 = subset_by_provider['2008.1'].tolist()
        sum_2008 += ref_2008[0]
        ref_2009 = subset_by_provider['2009.1'].tolist()
        sum_2009 += ref_2009[0]
        ref_2010 = subset_by_provider['2010.1'].tolist()
        sum_2010 += ref_2010[0]
        ref_2011 = subset_by_provider['2011.1'].tolist()
        sum_2011 += ref_2011[0]
        ref_2012 = subset_by_provider['2012.1'].tolist()
        sum_2012 += ref_2012[0]
        ref_2013 = subset_by_provider['2013.1'].tolist()
        sum_2013 += ref_2013[0]
        ref_2014 = subset_by_provider['2014.1'].tolist()
        sum_2014 += ref_2014[0]
        ref_2015 = subset_by_provider['2015.1'].tolist()
        sum_2015 += ref_2015[0]
        ref_2016 = subset_by_provider['2016.1'].tolist()
        sum_2016 += ref_2016[0]
        ref_2017 = subset_by_provider['2017.1'].tolist()
        sum_2017 += ref_2017[0]
        
    totals_by_year = list((sum_2008, sum_2009, sum_2010, sum_2011, sum_2012, sum_2013, sum_2014, sum_2015, sum_2016, sum_2017))
    
    years = ['2008','2009','2010','2011','2012','2013','2014','2015','2016','2017']

    plt.figure(num=None, figsize=(10,10))
    plt.suptitle(f'Number of References Made by {your_institution} Researchers \n (across all providers)')
    plt.xlabel('Year')
    plt.ylabel('Number References')
    plt.ylim(0, 120000)
    
    plt.plot(years, totals_by_year)



def figure4b_references():
    """ Show references per year (2008-2017) by your institution's affiliated authors, separating Elsevier Freedom
    and Elsevier Subscribed titles out from Elsevier as a whole.
    
    Chart Type: Line Graph
    Y-Axis: Number of References
    Y-Axis Data Source: Original 1Figr Dataset, Journals Per Provider, References to journal/provider by your institution's authors (as measured in Scopus)
                        Elsevier_2019, Subscribed Journal List 2019
    X-Axis: Year
    X-Axis Data Source: Original 1Figr Dataset, Journals Per Provider, Provider
                        Elsevier_2019, Subscribed Journal List 2019 
    """
    
    original_1figr_dataset = pd.read_excel(filename, sheet_name='Journals per Provider', skiprows=8)   

    elsevier_freedom_collection = rf.make_freedom_collection_provider()
    elsevier_subscribed_titles = rf.make_elsevier_subscribed_titles_provider()
    elsevier_unmatched_titles = rf.make_elsevier_unmatched_provider()

    #this holds reference totals for all providers in the end, which is used to make final plot
    ref_by_provider = []

    #populate references totals for elsevier subset providers    
    elsevier_providers = [elsevier_freedom_collection, elsevier_subscribed_titles, elsevier_unmatched_titles]
    
    for provider_name in elsevier_providers:
        
        ref_by_year = []
        
        ref_2008 = provider_name['2008.1'].tolist()
        ref_by_year.append(sum(ref_2008))
        ref_2009 = provider_name['2009.1'].tolist()
        ref_by_year.append(sum(ref_2009))
        ref_2010 = provider_name['2010.1'].tolist()
        ref_by_year.append(sum(ref_2010))
        ref_2011 = provider_name['2011.1'].tolist()
        ref_by_year.append(sum(ref_2011))
        ref_2012 = provider_name['2012.1'].tolist()
        ref_by_year.append(sum(ref_2012))
        ref_2013 = provider_name['2013.1'].tolist()
        ref_by_year.append(sum(ref_2013))
        ref_2014 = provider_name['2014.1'].tolist()
        ref_by_year.append(sum(ref_2014))
        ref_2015 = provider_name['2015.1'].tolist()
        ref_by_year.append(sum(ref_2015))
        ref_2016 = provider_name['2016.1'].tolist()
        ref_by_year.append(sum(ref_2016))
        ref_2017 = provider_name['2017.1'].tolist()
        ref_by_year.append(sum(ref_2017))
        
        ref_by_provider.append(ref_by_year)
    
    #populate references totals for other providers    
    providers = ['Sage', 'Springer', 'Taylor & Francis', 'Wiley']
    
    for provider_name in providers:
        
        subset_by_provider = original_1figr_dataset.loc[original_1figr_dataset['Provider'] == provider_name]
    
        ref_by_year = []
    
        ref_2008 = subset_by_provider['2008.1'].tolist()
        ref_by_year.append(ref_2008[0])
        ref_2009 = subset_by_provider['2009.1'].tolist()
        ref_by_year.append(ref_2009[0])
        ref_2010 = subset_by_provider['2010.1'].tolist()
        ref_by_year.append(ref_2010[0])
        ref_2011 = subset_by_provider['2011.1'].tolist()
        ref_by_year.append(ref_2011[0])
        ref_2012 = subset_by_provider['2012.1'].tolist()
        ref_by_year.append(ref_2012[0])
        ref_2013 = subset_by_provider['2013.1'].tolist()
        ref_by_year.append(ref_2013[0])
        ref_2014 = subset_by_provider['2014.1'].tolist()
        ref_by_year.append(ref_2014[0])
        ref_2015 = subset_by_provider['2015.1'].tolist()
        ref_by_year.append(ref_2015[0])
        ref_2016 = subset_by_provider['2016.1'].tolist()
        ref_by_year.append(ref_2016[0])
        ref_2017 = subset_by_provider['2017.1'].tolist()
        ref_by_year.append(ref_2017[0])
        
        ref_by_provider.append(ref_by_year)
    
    years = ['2008','2009','2010','2011','2012','2013','2014','2015','2016','2017']

    plt.figure(num=None, figsize=(10,10))
    plt.suptitle(f'Number of References Made by {your_institution} Researchers by Provider')
    plt.xlabel('Year')
    plt.ylabel('Number References')
    plt.ylim(0, 12000)

    plt.plot(years, ref_by_provider[0], label='Elsevier Freedom', color='red', linestyle='dashed')
    plt.plot(years, ref_by_provider[1], label='Elsevier Subscribed', color='red')
    plt.plot(years, ref_by_provider[2], label='Elsevier Unmatched', color='black')
    plt.plot(years, ref_by_provider[3], label='Sage', color='blue')
    plt.plot(years, ref_by_provider[4], label='Springer', color='green')
    plt.plot(years, ref_by_provider[5], label='Taylor & Francis', color='purple')
    plt.plot(years, ref_by_provider[6], label='Wiley', color='orange')

    plt.legend()
  


def figure4b_percentage():
    """ Show percent references per year as a part of all references for each provider, separating Elsevier Freedom
    and Elsevier Subscribed titles out from Elsevier as a whole.
    
    Chart Type: Line Graph
    Y-Axis: Number of References
    Y-Axis Data Source: Original 1Figr Dataset, Journals Per Provider, References to journal/provider by your institution's authors (as measured in Scopus)
                        Elsevier_2019, Subscribed Journal List 2019
    X-Axis: Year
    X-Axis Data Source: Original 1Figr Dataset, Journals Per Provider, Provider
                        Elsevier_2019, Subscribed Journal List 2019 
    """
    
    
    
    original_1figr_dataset = pd.read_excel(filename, sheet_name='Journals per Provider', skiprows=8)   

    all_providers = original_1figr_dataset['Provider'].unique()     #makes list of unique providers


    #build total references for all providers by year
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
    
    for provider_name in all_providers:
        
        subset_by_provider = original_1figr_dataset.loc[original_1figr_dataset['Provider'] == provider_name]
    
        ref_2008 = subset_by_provider['2008.1'].tolist()
        sum_2008 += ref_2008[0]
        ref_2009 = subset_by_provider['2009.1'].tolist()
        sum_2009 += ref_2009[0]
        ref_2010 = subset_by_provider['2010.1'].tolist()
        sum_2010 += ref_2010[0]
        ref_2011 = subset_by_provider['2011.1'].tolist()
        sum_2011 += ref_2011[0]
        ref_2012 = subset_by_provider['2012.1'].tolist()
        sum_2012 += ref_2012[0]
        ref_2013 = subset_by_provider['2013.1'].tolist()
        sum_2013 += ref_2013[0]
        ref_2014 = subset_by_provider['2014.1'].tolist()
        sum_2014 += ref_2014[0]
        ref_2015 = subset_by_provider['2015.1'].tolist()
        sum_2015 += ref_2015[0]
        ref_2016 = subset_by_provider['2016.1'].tolist()
        sum_2016 += ref_2016[0]
        ref_2017 = subset_by_provider['2017.1'].tolist()
        sum_2017 += ref_2017[0]


    #build references by provider for each year
    providers = ['Sage', 'Springer', 'Taylor & Francis', 'Wiley']

    ref_by_provider = []    #this holds percentage of total references for each year by provider, which is later plotted
    
    for provider_name in providers:
        
        subset_by_provider = original_1figr_dataset.loc[original_1figr_dataset['Provider'] == provider_name]
    
        ref_by_year = []
    
        ref_2008 = subset_by_provider['2008.1'].tolist()
        ref_by_year.append(ref_2008[0]/sum_2008)
        ref_2009 = subset_by_provider['2009.1'].tolist()
        ref_by_year.append(ref_2009[0]/sum_2009)
        ref_2010 = subset_by_provider['2010.1'].tolist()
        ref_by_year.append(ref_2010[0]/sum_2010)
        ref_2011 = subset_by_provider['2011.1'].tolist()
        ref_by_year.append(ref_2011[0]/sum_2011)
        ref_2012 = subset_by_provider['2012.1'].tolist()
        ref_by_year.append(ref_2012[0]/sum_2012)
        ref_2013 = subset_by_provider['2013.1'].tolist()
        ref_by_year.append(ref_2013[0]/sum_2013)
        ref_2014 = subset_by_provider['2014.1'].tolist()
        ref_by_year.append(ref_2014[0]/sum_2014)
        ref_2015 = subset_by_provider['2015.1'].tolist()
        ref_by_year.append(ref_2015[0]/sum_2015)
        ref_2016 = subset_by_provider['2016.1'].tolist()
        ref_by_year.append(ref_2016[0]/sum_2016)
        ref_2017 = subset_by_provider['2017.1'].tolist()
        ref_by_year.append(ref_2017[0]/sum_2017)
        
        ref_by_provider.append(ref_by_year)


    #Calculate number of references for Elsevier Freedom and Elsevier Subscribed titles
    elsevier_freedom_collection = rf.make_freedom_collection_provider()
    elsevier_subscribed_titles = rf.make_elsevier_subscribed_titles_provider()
    elsevier_unmatched_titles = rf.make_elsevier_unmatched_provider()
    
    elsevier_providers = [elsevier_freedom_collection, elsevier_subscribed_titles, elsevier_unmatched_titles]
    
    for provider_name in elsevier_providers:
        
        ref_by_year = []
        
        ref_2008 = provider_name['2008.1'].tolist()
        ref_by_year.append((sum(ref_2008))/sum_2008)
        ref_2009 = provider_name['2009.1'].tolist()
        ref_by_year.append((sum(ref_2009))/sum_2009)
        ref_2010 = provider_name['2010.1'].tolist()
        ref_by_year.append((sum(ref_2010))/sum_2010)
        ref_2011 = provider_name['2011.1'].tolist()
        ref_by_year.append((sum(ref_2011))/sum_2011)
        ref_2012 = provider_name['2012.1'].tolist()
        ref_by_year.append((sum(ref_2012))/sum_2012)
        ref_2013 = provider_name['2013.1'].tolist()
        ref_by_year.append((sum(ref_2013))/sum_2013)
        ref_2014 = provider_name['2014.1'].tolist()
        ref_by_year.append((sum(ref_2014))/sum_2014)
        ref_2015 = provider_name['2015.1'].tolist()
        ref_by_year.append((sum(ref_2015))/sum_2015)
        ref_2016 = provider_name['2016.1'].tolist()
        ref_by_year.append((sum(ref_2016))/sum_2016)
        ref_2017 = provider_name['2017.1'].tolist()
        ref_by_year.append((sum(ref_2017))/sum_2017)

        ref_by_provider.append(ref_by_year)
        
        
    years = ['2008','2009','2010','2011','2012','2013','2014','2015','2016','2017']

    plt.figure(num=None, figsize=(10,10))
    plt.suptitle(f'Percent of All References Made by {your_institution} Authors')
    plt.xlabel('Year')
    plt.ylabel('Percentage')

    plt.gca().yaxis.set_major_formatter(StrMethodFormatter('{x:,.0%}'))    #formats y axis as %


    plt.plot(years, ref_by_provider[0], label='Sage', color='blue')
    plt.plot(years, ref_by_provider[1], label='Springer', color='green')
    plt.plot(years, ref_by_provider[2], label='Taylor & Francis', color='purple')
    plt.plot(years, ref_by_provider[3], label='Wiley', color='orange')
    plt.plot(years, ref_by_provider[4], label='Elsevier Freedom', color='red', linestyle='dashed')
    plt.plot(years, ref_by_provider[5], label='Elsevier Subscribed', color='red')
    plt.plot(years, ref_by_provider[6], label='Elsevier Unmatched', color='black')


    plt.legend(loc='center left', bbox_to_anchor=(1, 0.8))
        

