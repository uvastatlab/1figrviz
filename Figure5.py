#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 13:29:33 2019

@author: ep9k
"""

import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter
import matplotlib.patches as mpatches

import reusable_functions as rf


filename = '1figr_U_Virginia_Original (1) (1).xlsx'
your_institution = 'UVA'


def figure5b_papers():
    """Show papers per year by your institution's affiliated authors, separating Elsevier Freedom
    and Elsevier Subscribed titles out from Elsevier as a whole.  Papers are publications
    by you institution's affiliated authors"""
    
#    original_1figr_dataset = pd.read_excel(filename, sheet_name='Journals per Provider', skiprows=8)   
    original_1figr_dataset = pd.read_excel('JournalsPerProvider.xls', skiprows=8)
    elsevier_freedom_collection = rf.make_freedom_collection_provider()
    elsevier_subscribed_titles = rf.make_elsevier_subscribed_titles_provider()



    #this holds papers totals for all providers in the end, which is used to make final plot
    papers_by_provider = []
    
    #populate references totals for elsevier subset providers    
    elsevier_providers = [elsevier_freedom_collection, elsevier_subscribed_titles]
    
    
    for provider_name in elsevier_providers:
        
        papers_by_year = []
        
        papers_2008 = provider_name[2008].tolist()
        papers_by_year.append(sum(papers_2008))
        papers_2009 = provider_name[2009].tolist()
        papers_by_year.append(sum(papers_2009))
        papers_2010 = provider_name[2010].tolist()
        papers_by_year.append(sum(papers_2010))
        papers_2011 = provider_name[2011].tolist()
        papers_by_year.append(sum(papers_2011))
        papers_2012 = provider_name[2012].tolist()
        papers_by_year.append(sum(papers_2012))
        papers_2013 = provider_name[2013].tolist()
        papers_by_year.append(sum(papers_2013))
        papers_2014 = provider_name[2014].tolist()
        papers_by_year.append(sum(papers_2014))
        papers_2015 = provider_name[2015].tolist()
        papers_by_year.append(sum(papers_2015))
        papers_2016 = provider_name[2016].tolist()
        papers_by_year.append(sum(papers_2016))
        papers_2017 = provider_name[2017].tolist()
        papers_by_year.append(sum(papers_2017))
        
        
        
        papers_by_provider.append(papers_by_year)
        
    
    #populate references totals for other providers    
    providers = ['Sage', 'Springer', 'Taylor & Francis', 'Wiley']

    for provider_name in providers:
        
        subset_by_provider = original_1figr_dataset.loc[original_1figr_dataset['Provider'] == provider_name]
    
        papers_by_year = []

        papers_2008 = subset_by_provider[2008].tolist()
        papers_by_year.append(papers_2008[0])
        papers_2009 = subset_by_provider[2009].tolist()
        papers_by_year.append(papers_2009[0])
        papers_2010 = subset_by_provider[2010].tolist()
        papers_by_year.append(papers_2010[0])
        papers_2011 = subset_by_provider[2011].tolist()
        papers_by_year.append(papers_2011[0])
        papers_2012 = subset_by_provider[2012].tolist()
        papers_by_year.append(papers_2012[0])
        papers_2013 = subset_by_provider[2013].tolist()
        papers_by_year.append(papers_2013[0])
        papers_2014 = subset_by_provider[2014].tolist()
        papers_by_year.append(papers_2014[0])
        papers_2015 = subset_by_provider[2015].tolist()
        papers_by_year.append(papers_2015[0])
        papers_2016 = subset_by_provider[2016].tolist()
        papers_by_year.append(papers_2016[0])
        papers_2017 = subset_by_provider[2017].tolist()
        papers_by_year.append(papers_2017[0])
        
        papers_by_provider.append(papers_by_year)
        
        
    years = ['2008','2009','2010','2011','2012','2013','2014','2015','2016','2017']

    plt.figure(num=None, figsize=(10,10))
    plt.suptitle(f'Number of Articles by {your_institution} Authors')
    plt.xlabel('Year')
    plt.ylabel('Number of Articles')


    plt.plot(years, papers_by_provider[0], label='Elsevier Freedom', color='red', linestyle='dashed')
    plt.plot(years, papers_by_provider[1], label='Elsevier Subscribed', color='red')
    plt.plot(years, papers_by_provider[2], label='Sage', color='blue')
    plt.plot(years, papers_by_provider[3], label='Springer', color='green')
    plt.plot(years, papers_by_provider[4], label='Taylor & Francis', color='purple')
    plt.plot(years, papers_by_provider[5], label='Wiley', color='orange')

    plt.legend(loc='center left', bbox_to_anchor=(1, 0.8))



#TODO: WHAT IS BEING COMPARED HERE?
def figure5b_percentage():
    """ Show percent papers per year published by UVA authors as a percentage of all papers for each provider, separating Elsevier Freedom
    and Elsevier Subscribed titles out from Elsevier as a whole."""
    
    #    original_1figr_dataset = pd.read_excel(filename, sheet_name='Journals per Provider', skiprows=8)   
    original_1figr_dataset = pd.read_excel('JournalsPerProvider.xls', skiprows=8)

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

        all_jr1_downloads_2008 = subset_by_provider['Downloads JR1 2017'].tolist()
        sum_2008 += all_jr1_downloads_2008[0]
        all_jr1_downloads_2009 = subset_by_provider['Downloads JR1 2017'].tolist()
        sum_2009 += all_jr1_downloads_2009[0]
        all_jr1_downloads_2010 = subset_by_provider['Downloads JR1 2017'].tolist()
        sum_2010 += all_jr1_downloads_2010[0]
        all_jr1_downloads_2011 = subset_by_provider['Downloads JR1 2017'].tolist()
        sum_2011 += all_jr1_downloads_2011[0]
        all_jr1_downloads_2012 = subset_by_provider['Downloads JR1 2017'].tolist()
        sum_2012 += all_jr1_downloads_2012[0]
        all_jr1_downloads_2013 = subset_by_provider['Downloads JR1 2017'].tolist()
        sum_2013 += all_jr1_downloads_2013[0]
        all_jr1_downloads_2014 = subset_by_provider['Downloads JR1 2017'].tolist()
        sum_2014 += all_jr1_downloads_2014[0]
        all_jr1_downloads_2015 = subset_by_provider['Downloads JR1 2017'].tolist()
        sum_2015 += all_jr1_downloads_2015[0]
        all_jr1_downloads_2016 = subset_by_provider['Downloads JR1 2017'].tolist()
        sum_2016 += all_jr1_downloads_2016[0]
        all_jr1_downloads_2017 = subset_by_provider['Downloads JR1 2017'].tolist()
        sum_2017 += all_jr1_downloads_2017[0]

    
#    for provider_name in all_providers:
#        
#        subset_by_provider = original_1figr_dataset.loc[original_1figr_dataset['Provider'] == provider_name]
#    
#        papers_2008 = subset_by_provider[2008].tolist()
#        sum_2008 += papers_2008[0]
#        papers_2009 = subset_by_provider[2009].tolist()
#        sum_2009 += papers_2009[0]
#        papers_2010 = subset_by_provider[2010].tolist()
#        sum_2010 += papers_2010[0]
#        papers_2011 = subset_by_provider[2011].tolist()
#        sum_2011 += papers_2011[0]
#        papers_2012 = subset_by_provider[2012].tolist()
#        sum_2012 += papers_2012[0]
#        papers_2013 = subset_by_provider[2013].tolist()
#        sum_2013 += papers_2013[0]
#        papers_2014 = subset_by_provider[2014].tolist()
#        sum_2014 += papers_2014[0]
#        papers_2015 = subset_by_provider[2015].tolist()
#        sum_2015 += papers_2015[0]
#        papers_2016 = subset_by_provider[2016].tolist()
#        sum_2016 += papers_2016[0]
#        papers_2017 = subset_by_provider[2017].tolist()
#        sum_2017 += papers_2017[0]
        

        
    #build references by provider for each year
    providers = ['Sage', 'Springer', 'Taylor & Francis', 'Wiley']

    papers_by_provider = []    #this holds percentage of total references for each year by provider, which is later plotted
    
    for provider_name in providers:
        
        subset_by_provider = original_1figr_dataset.loc[original_1figr_dataset['Provider'] == provider_name]

        papers_by_year = []
    
        papers_2008 = subset_by_provider[2008].tolist()
        papers_by_year.append(papers_2008[0]/sum_2008)
        papers_2009 = subset_by_provider[2009].tolist()
        papers_by_year.append(papers_2009[0]/sum_2009)
        papers_2010 = subset_by_provider[2010].tolist()
        papers_by_year.append(papers_2010[0]/sum_2010)
        papers_2011 = subset_by_provider[2011].tolist()
        papers_by_year.append(papers_2011[0]/sum_2011)
        papers_2012 = subset_by_provider[2012].tolist()
        papers_by_year.append(papers_2012[0]/sum_2012)
        papers_2013 = subset_by_provider[2013].tolist()
        papers_by_year.append(papers_2013[0]/sum_2013)
        papers_2014 = subset_by_provider[2014].tolist()
        papers_by_year.append(papers_2014[0]/sum_2014)
        papers_2015 = subset_by_provider[2015].tolist()
        papers_by_year.append(papers_2015[0]/sum_2015)
        papers_2016 = subset_by_provider[2016].tolist()
        papers_by_year.append(papers_2016[0]/sum_2016)
        papers_2017 = subset_by_provider[2017].tolist()
        papers_by_year.append(papers_2017[0]/sum_2017)   
        
        papers_by_provider.append(papers_by_year)


    #Calculate number of references for Elsevier Freedom and Elsevier Subscribed titles        
    elsevier_freedom_collection = rf.make_freedom_collection_provider()
    elsevier_subscribed_titles = rf.make_elsevier_subscribed_titles_provider()
    
    elsevier_providers = [elsevier_freedom_collection, elsevier_subscribed_titles]
    
    for provider_name in elsevier_providers:

        papers_by_year = []
        
        papers_2008 = provider_name[2008].tolist()
        papers_by_year.append((sum(papers_2008))/sum_2008)
        papers_2009 = provider_name[2009].tolist()
        papers_by_year.append((sum(papers_2009))/sum_2009)
        papers_2010 = provider_name[2010].tolist()
        papers_by_year.append((sum(papers_2010))/sum_2010)
        papers_2011 = provider_name[2011].tolist()
        papers_by_year.append((sum(papers_2011))/sum_2011)
        papers_2012 = provider_name[2012].tolist()
        papers_by_year.append((sum(papers_2012))/sum_2012)
        papers_2013 = provider_name[2013].tolist()
        papers_by_year.append((sum(papers_2013))/sum_2013)
        papers_2014 = provider_name[2014].tolist()
        papers_by_year.append((sum(papers_2014))/sum_2014)
        papers_2015 = provider_name[2015].tolist()
        papers_by_year.append((sum(papers_2015))/sum_2015)
        papers_2016 = provider_name[2016].tolist()
        papers_by_year.append((sum(papers_2016))/sum_2016)
        papers_2017 = provider_name[2017].tolist()
        papers_by_year.append((sum(papers_2017))/sum_2017)
        
        papers_by_provider.append(papers_by_year)

        
    years = ['2008','2009','2010','2011','2012','2013','2014','2015','2016','2017']

    plt.figure(num=None, figsize=(10,10))
    plt.suptitle(f'Percent of All Articles by {your_institution} Authors')
    plt.xlabel('Year')
    plt.ylabel('Percentage')
        
#    plt.gca().yaxis.set_major_formatter(StrMethodFormatter('{x:,.0%}'))    #formats y axis as %

    plt.plot(years, papers_by_provider[0], label='Sage', color='blue')
    plt.plot(years, papers_by_provider[1], label='Springer', color='green')
    plt.plot(years, papers_by_provider[2], label='Taylor & Francis', color='purple')
    plt.plot(years, papers_by_provider[3], label='Wiley', color='orange')
    plt.plot(years, papers_by_provider[4], label='Elsevier Freedom', color='red', linestyle='dashed')
    plt.plot(years, papers_by_provider[5], label='Elsevier Subscribed', color='red')
        
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.8))
    
figure5b_percentage()  
