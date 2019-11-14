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

import sandbox as sb


filename = '1figr_U_Virginia_Original (1) (1).xlsx'
your_institution = 'UVA'


def figure4b_references():
    """ Show references per year by UVA authors, separating Elsevier Freedom
    and Elsevier Subscribed titles out from Elsevier as a whole."""
    
    original_1figr_dataset = pd.read_excel(filename, sheet_name='Journals per Provider', skiprows=8)   
    elsevier_freedom_collection = sb.make_freedom_collection_provider()
    elsevier_subscribed_titles = sb.make_elsevier_subscribed_titles_provider()

    #this holds reference totals for all providers in the end, which is used to make final plot
    ref_by_provider = []

    #populate references totals for elsevier subset providers    
    elsevier_providers = [elsevier_freedom_collection, elsevier_subscribed_titles]
    
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
    plt.ylim(0, 10000)

    plt.plot(years, ref_by_provider[0], label='Elsevier Freedom')
    plt.plot(years, ref_by_provider[1], label='Elsevier Subscrbibed')
    plt.plot(years, ref_by_provider[2], label='Sage')
    plt.plot(years, ref_by_provider[3], label='Springer')
    plt.plot(years, ref_by_provider[4], label='Taylor & Francis')
    plt.plot(years, ref_by_provider[5], label='Wiley')

    plt.legend()
    
    
figure4b_references()


def figure4b_percent():
    pass
    