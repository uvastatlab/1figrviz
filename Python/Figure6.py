#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 10:10:04 2019

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


def figure6b_oa_available_articles():
    """Show number Open Access (OA) available articles per provider over time for provider,
    separating our Elsevier subscribed and Elsevier Freedom collection from Elsevier as a whole"""
    
#    original_1figr_dataset = pd.read_excel(filename, sheet_name='Journals per Provider', skiprows=8)   
    original_1figr_dataset = pd.read_excel('JournalsPerProvider.xls', skiprows=8)
    elsevier_freedom_collection = rf.make_freedom_collection_provider()
    elsevier_subscribed_titles = rf.make_elsevier_subscribed_titles_provider()


    oa_articles_by_provider = []
    
    elsevier_providers = [elsevier_freedom_collection, elsevier_subscribed_titles]    


    for provider_name in elsevier_providers:
        
        oa_articles_by_year = []
        
        oa_articles_2008 = provider_name['2008.2'].tolist()
        oa_articles_by_year.append(sum(oa_articles_2008))
        oa_articles_2009 = provider_name['2009.2'].tolist()
        oa_articles_by_year.append(sum(oa_articles_2009))
        oa_articles_2010 = provider_name['2010.2'].tolist()
        oa_articles_by_year.append(sum(oa_articles_2010))
        oa_articles_2011 = provider_name['2011.2'].tolist()
        oa_articles_by_year.append(sum(oa_articles_2011))
        oa_articles_2012 = provider_name['2012.2'].tolist()
        oa_articles_by_year.append(sum(oa_articles_2012))
        oa_articles_2013 = provider_name['2013.2'].tolist()
        oa_articles_by_year.append(sum(oa_articles_2013))
        oa_articles_2014 = provider_name['2014.2'].tolist()
        oa_articles_by_year.append(sum(oa_articles_2014))
        oa_articles_2015 = provider_name['2015.2'].tolist()
        oa_articles_by_year.append(sum(oa_articles_2015))
        oa_articles_2016 = provider_name['2016.2'].tolist()
        oa_articles_by_year.append(sum(oa_articles_2016))
        oa_articles_2017 = provider_name['2017.2'].tolist()
        oa_articles_by_year.append(sum(oa_articles_2017))
        
        oa_articles_by_provider.append(oa_articles_by_year)
        

    providers = ['Sage', 'Springer', 'Taylor & Francis', 'Wiley']
    
    for provider_name in providers:
        
        subset_by_provider = original_1figr_dataset.loc[original_1figr_dataset['Provider'] == provider_name]

        oa_articles_by_year = []
        
        oa_articles_2008 = subset_by_provider['2008.2'].tolist()
        oa_articles_by_year.append(oa_articles_2008[0])  
        oa_articles_2009 = subset_by_provider['2009.2'].tolist()
        oa_articles_by_year.append(oa_articles_2009[0])  
        oa_articles_2010 = subset_by_provider['2010.2'].tolist()
        oa_articles_by_year.append(oa_articles_2010[0])  
        oa_articles_2011 = subset_by_provider['2011.2'].tolist()
        oa_articles_by_year.append(oa_articles_2011[0])  
        oa_articles_2012 = subset_by_provider['2012.2'].tolist()
        oa_articles_by_year.append(oa_articles_2012[0])  
        oa_articles_2013 = subset_by_provider['2013.2'].tolist()
        oa_articles_by_year.append(oa_articles_2013[0])  
        oa_articles_2014 = subset_by_provider['2014.2'].tolist()
        oa_articles_by_year.append(oa_articles_2014[0])  
        oa_articles_2015 = subset_by_provider['2015.2'].tolist()
        oa_articles_by_year.append(oa_articles_2015[0])  
        oa_articles_2016 = subset_by_provider['2016.2'].tolist()
        oa_articles_by_year.append(oa_articles_2016[0])  
        oa_articles_2017 = subset_by_provider['2017.2'].tolist()
        oa_articles_by_year.append(oa_articles_2017[0])
        
        oa_articles_by_provider.append(oa_articles_by_year)
        
    years = ['2008','2009','2010','2011','2012','2013','2014','2015','2016','2017']

    plt.figure(num=None, figsize=(10,10))
    plt.suptitle(f'Number of OA-Available Articles')
    plt.xlabel('Year')
    plt.ylabel('Number of Articles')


    plt.plot(years, oa_articles_by_provider[0], label='Elsevier Freedom', color='red', linestyle='dashed')
    plt.plot(years, oa_articles_by_provider[1], label='Elsevier Subscribed', color='red')
    plt.plot(years, oa_articles_by_provider[2], label='Sage', color='blue')
    plt.plot(years, oa_articles_by_provider[3], label='Springer', color='green')
    plt.plot(years, oa_articles_by_provider[4], label='Taylor & Francis', color='purple')
    plt.plot(years, oa_articles_by_provider[5], label='Wiley', color='orange')

    plt.legend(loc='center left', bbox_to_anchor=(1, 0.8))

    

#TODO: WHAT ARE WE COMPARING HERE???
def figure_6b_percent_oa_available_articles():
    """Percent of All articles that are open access by provider by year. Separating elsevier subscribed and
    elsevier freedom collection from elsevier as a whole"""
    
#    original_1figr_dataset = pd.read_excel(filename, sheet_name='Journals per Provider', skiprows=8)   
    original_1figr_dataset = pd.read_excel('JournalsPerProvider.xls', skiprows=8)
    elsevier_freedom_collection = rf.make_freedom_collection_provider()
    elsevier_subscribed_titles = rf.make_elsevier_subscribed_titles_provider()


    all_providers = original_1figr_dataset['Provider'].unique()     #makes list of unique providers

    #build total articles for all providers by year
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

        all_oa_articles_2008 = subset_by_provider['2008.2'].tolist()
        sum_2008 += all_oa_articles_2008[0]
        all_oa_articles_2009 = subset_by_provider['2009.2'].tolist()
        sum_2009 += all_oa_articles_2009[0]
        all_oa_articles_2010 = subset_by_provider['2010.2'].tolist()
        sum_2010 += all_oa_articles_2010[0]
        all_oa_articles_2011 = subset_by_provider['2011.2'].tolist()
        sum_2011 += all_oa_articles_2011[0]
        all_oa_articles_2012 = subset_by_provider['2012.2'].tolist()
        sum_2012 += all_oa_articles_2012[0]
        all_oa_articles_2013 = subset_by_provider['2013.2'].tolist()
        sum_2013 += all_oa_articles_2013[0]
        all_oa_articles_2014 = subset_by_provider['2014.2'].tolist()
        sum_2014 += all_oa_articles_2014[0]
        all_oa_articles_2015 = subset_by_provider['2015.2'].tolist()
        sum_2015 += all_oa_articles_2015[0]
        all_oa_articles_2016 = subset_by_provider['2016.2'].tolist()
        sum_2016 += all_oa_articles_2016[0]
        all_oa_articles_2017 = subset_by_provider['2017.2'].tolist()
        sum_2017 += all_oa_articles_2017[0]


        
    oa_articles_by_provider = []  #this holds percentage of OA articles by provider

    #Calculate number of references for Elsevier Freedom and Elsevier Subscribed titles            
    elsevier_providers = [elsevier_freedom_collection, elsevier_subscribed_titles]    

    for provider_name in elsevier_providers:
        
        oa_articles_by_year = []
        
        oa_articles_2008 = provider_name['2008.2'].tolist()
        oa_articles_by_year.append(sum(oa_articles_2008)/sum_2008)
        oa_articles_2009 = provider_name['2009.2'].tolist()
        oa_articles_by_year.append(sum(oa_articles_2009)/sum_2009)
        oa_articles_2010 = provider_name['2010.2'].tolist()
        oa_articles_by_year.append(sum(oa_articles_2010)/sum_2010)
        oa_articles_2011 = provider_name['2011.2'].tolist()
        oa_articles_by_year.append(sum(oa_articles_2011)/sum_2011)
        oa_articles_2012 = provider_name['2012.2'].tolist()
        oa_articles_by_year.append(sum(oa_articles_2012)/sum_2012)
        oa_articles_2013 = provider_name['2013.2'].tolist()
        oa_articles_by_year.append(sum(oa_articles_2013)/sum_2013)
        oa_articles_2014 = provider_name['2014.2'].tolist()
        oa_articles_by_year.append(sum(oa_articles_2014)/sum_2014)
        oa_articles_2015 = provider_name['2015.2'].tolist()
        oa_articles_by_year.append(sum(oa_articles_2015)/sum_2015)
        oa_articles_2016 = provider_name['2016.2'].tolist()
        oa_articles_by_year.append(sum(oa_articles_2016)/sum_2016)
        oa_articles_2017 = provider_name['2017.2'].tolist()
        oa_articles_by_year.append(sum(oa_articles_2017)/sum_2017)
        
        oa_articles_by_provider.append(oa_articles_by_year)
        
    #build percentage of open access articles by provider for each year
    providers = ['Sage', 'Springer', 'Taylor & Francis', 'Wiley']
    
    for provider_name in providers:
        
        subset_by_provider = original_1figr_dataset.loc[original_1figr_dataset['Provider'] == provider_name]

        oa_articles_by_year = []
        
        oa_articles_2008 = subset_by_provider['2008.2'].tolist()
        oa_articles_by_year.append(oa_articles_2008[0]/sum_2008)  
        oa_articles_2009 = subset_by_provider['2009.2'].tolist()
        oa_articles_by_year.append(oa_articles_2009[0]/sum_2009)  
        oa_articles_2010 = subset_by_provider['2010.2'].tolist()
        oa_articles_by_year.append(oa_articles_2010[0]/sum_2010)  
        oa_articles_2011 = subset_by_provider['2011.2'].tolist()
        oa_articles_by_year.append(oa_articles_2011[0]/sum_2011)  
        oa_articles_2012 = subset_by_provider['2012.2'].tolist()
        oa_articles_by_year.append(oa_articles_2012[0]/sum_2012)  
        oa_articles_2013 = subset_by_provider['2013.2'].tolist()
        oa_articles_by_year.append(oa_articles_2013[0]/sum_2013)  
        oa_articles_2014 = subset_by_provider['2014.2'].tolist()
        oa_articles_by_year.append(oa_articles_2014[0]/sum_2014)  
        oa_articles_2015 = subset_by_provider['2015.2'].tolist()
        oa_articles_by_year.append(oa_articles_2015[0]/sum_2015)  
        oa_articles_2016 = subset_by_provider['2016.2'].tolist()
        oa_articles_by_year.append(oa_articles_2016[0]/sum_2016)  
        oa_articles_2017 = subset_by_provider['2017.2'].tolist()
        oa_articles_by_year.append(oa_articles_2017[0]/sum_2017)
        
        oa_articles_by_provider.append(oa_articles_by_year)


    years = ['2008','2009','2010','2011','2012','2013','2014','2015','2016','2017']

    plt.figure(num=None, figsize=(10,10))
    plt.suptitle(f'Percent of OA-Available Articles')
    plt.xlabel('Year')
    plt.ylabel('Percentage')


    plt.plot(years, oa_articles_by_provider[0], label='Elsevier Freedom', color='red', linestyle='dashed')
    plt.plot(years, oa_articles_by_provider[1], label='Elsevier Subscribed', color='red')
    plt.plot(years, oa_articles_by_provider[2], label='Sage', color='blue')
    plt.plot(years, oa_articles_by_provider[3], label='Springer', color='green')
    plt.plot(years, oa_articles_by_provider[4], label='Taylor & Francis', color='purple')
    plt.plot(years, oa_articles_by_provider[5], label='Wiley', color='orange')

    plt.legend(loc='center left', bbox_to_anchor=(1, 0.8))


    
figure_6b_percent_oa_available_articles()    






