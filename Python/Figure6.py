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

def figure6a_number_of_articles_published():
    pass

def figure6a_oa_available_articles():
    """Number of papers available Open Access (oa) for each of the big 5 providers over time (2008-2017)
    Looks at columns under 'OA papers in 1finder per journal/provider (Intersection with scopus)
    
    Chart Type: Line graph
    Y-Axis: Number of Open Access Articles
    Y-Axis Data Source: Original 1Figr Dataset 
    
    X-Axis: Year
    X-Axis Data Source: Original 1Figr Dataset
    """
    
    data = pd.read_csv('JournalsPerProvider.csv', skiprows=8)
    
    big5 = ['Elsevier', 'Taylor & Francis', 'Sage', 'Springer', 'Wiley']

    oa_by_provider = []
    
    for provider_name in big5:
        
        subset_by_provider = data.loc[data['Provider'] == provider_name]
    
        oa_by_year = []
    
        oa_2008 = subset_by_provider.oa_papers_2008.tolist()
        oa_by_year.append(oa_2008[0])
        oa_2009 = subset_by_provider.oa_papers_2009.tolist()
        oa_by_year.append(oa_2009[0])
        oa_2010 = subset_by_provider.oa_papers_2010.tolist()
        oa_by_year.append(oa_2010[0])
        oa_2011 = subset_by_provider.oa_papers_2011.tolist()
        oa_by_year.append(oa_2011[0])
        oa_2012 = subset_by_provider.oa_papers_2012.tolist()
        oa_by_year.append(oa_2012[0])
        oa_2013 = subset_by_provider.oa_papers_2013.tolist()
        oa_by_year.append(oa_2013[0])
        oa_2014 = subset_by_provider.oa_papers_2014.tolist()
        oa_by_year.append(oa_2014[0])
        oa_2015 = subset_by_provider.oa_papers_2015.tolist()
        oa_by_year.append(oa_2015[0])
        oa_2016 = subset_by_provider.oa_papers_2016.tolist()
        oa_by_year.append(oa_2016[0])
        oa_2017 = subset_by_provider.oa_papers_2017.tolist()
        oa_by_year.append(oa_2017[0])
        
        oa_by_provider.append(oa_by_year)
    
    years = ['2008','2009','2010','2011','2012','2013','2014','2015','2016','2017']

    plt.figure(num=None, figsize=(10,10))
    plt.suptitle(f'Number of OA-Available Papers by Year')
    plt.xlabel('Year')
    plt.ylabel('Number Papers Available')

    plt.plot(years, oa_by_provider[0], label='Elsevier')
    plt.plot(years, oa_by_provider[1], label='Taylor & Francis')
    plt.plot(years, oa_by_provider[2], label='Sage')
    plt.plot(years, oa_by_provider[3], label='Springer')
    plt.plot(years, oa_by_provider[4], label='Wiley')

    plt.legend()


def figure6a_percent_oa_articles():
    """Percent of papers available Open Access (oa) for each of the big 5 providers over time (2008-2017)
    Looks at columns under '% of OA papers in 1findr per journal/provider (intersection with Scopus)
    
    Chart Type: Line graph
    Y-Axis: Number of Open Access Articles
    Y-Axis Data Source: Original 1Figr Dataset 
    
    X-Axis: Year
    X-Axis Data Source: Original 1Figr Dataset
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
    



def figure6b_oa_available_articles():
    """Show number Open Access (OA) available articles per provider over time (2008-2017) for provider,
    separating our Elsevier subscribed and Elsevier Freedom collection from Elsevier as a whole
    
    Chart Type: Line Graph
    Y-Axis: Number of Open access Articles
    Y-Axis Data Source: Original 1Figr Dataset, Journals Per Provider, OA papers in 1findr per journal/provider (intersection with Scopus)
                        Elsevier_2019, Subscribed Journal List 2019
    X-Axis: Year
    X-Axis Data Source: Original 1Figr Dataset, Journals Per Provider, Provider
                        Elsevier_2019, Subscribed Journal List 2019 
    """
    
#    original_1figr_dataset = pd.read_excel(filename, sheet_name='Journals per Provider', skiprows=8)   
    original_1figr_dataset = pd.read_excel('JournalsPerProvider.xls', skiprows=8)

    elsevier_freedom_collection = rf.make_freedom_collection_provider()
    elsevier_subscribed_titles = rf.make_elsevier_subscribed_titles_provider()
    elsevier_unmatched_titles = rf.make_elsevier_unmatched_provider()

    oa_articles_by_provider = []
    
    elsevier_providers = [elsevier_freedom_collection, elsevier_subscribed_titles, elsevier_unmatched_titles]    


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
    plt.plot(years, oa_articles_by_provider[2], label='Elsevier Unmatched', color='black')
    plt.plot(years, oa_articles_by_provider[3], label='Sage', color='blue')
    plt.plot(years, oa_articles_by_provider[4], label='Springer', color='green')
    plt.plot(years, oa_articles_by_provider[5], label='Taylor & Francis', color='purple')
    plt.plot(years, oa_articles_by_provider[6], label='Wiley', color='orange')

    plt.legend(loc='center left', bbox_to_anchor=(1, 0.8))


def figure6b_percent_oa_articles():
    """ Show percent papers per year published open access per provider per year as a percentage of all papers
    published per provider per year. Separates elsevier freedom an elsevier subscribed titles out from the whole
    
    Chart Type: Line Graph
    Y-Axis: Number of Papers
    Y-Axis Data Source: Original 1Figr Dataset, Journals Per Provider, OA papers in 1findr per journal/provider (intersection with Scopus)
                        Elsevier_2019, Subscribed Journal List 2019
    X-Axis: Year
    X-Axis Data Source: Original 1Figr Dataset, Journals Per Provider, Provider
                        Elsevier_2019, Subscribed Journal List 2019 

    """

    #    original_1figr_dataset = pd.read_excel(filename, sheet_name='Journals per Provider', skiprows=8)   
    original_1figr_dataset = pd.read_excel('JournalsPerProvider.xls', skiprows=8)

    #holds percent papers published open access per year per provider
    percent_oa_papers_by_provider = []
    
    #populate % oa papers totals for other providers    
    providers = ['Sage', 'Springer', 'Taylor & Francis', 'Wiley']

    for provider_name in providers:

        percent_oa_papers_by_year = []
    
        subset_by_provider = original_1figr_dataset.loc[original_1figr_dataset['Provider'] == provider_name]

        oa_papers_2008 = subset_by_provider['2008.3'].tolist()
        percent_oa_papers_by_year.append(oa_papers_2008[0])
        oa_papers_2009 = subset_by_provider['2009.3'].tolist()
        percent_oa_papers_by_year.append(oa_papers_2009[0])
        oa_papers_2010 = subset_by_provider['2010.3'].tolist()
        percent_oa_papers_by_year.append(oa_papers_2010[0])
        oa_papers_2011 = subset_by_provider['2011.3'].tolist()
        percent_oa_papers_by_year.append(oa_papers_2011[0])
        oa_papers_2012 = subset_by_provider['2012.3'].tolist()
        percent_oa_papers_by_year.append(oa_papers_2012[0])
        oa_papers_2013 = subset_by_provider['2013.3'].tolist()
        percent_oa_papers_by_year.append(oa_papers_2013[0])
        oa_papers_2014 = subset_by_provider['2014.3'].tolist()
        percent_oa_papers_by_year.append(oa_papers_2014[0])
        oa_papers_2015 = subset_by_provider['2015.3'].tolist()
        percent_oa_papers_by_year.append(oa_papers_2015[0])
        oa_papers_2016 = subset_by_provider['2016.3'].tolist()
        percent_oa_papers_by_year.append(oa_papers_2016[0])
        oa_papers_2017 = subset_by_provider['2017.3'].tolist()
        percent_oa_papers_by_year.append(oa_papers_2017[0])

        percent_oa_papers_by_provider.append(percent_oa_papers_by_year)  
        

    #populate % oa papers totals for elsevier freedom and elsevier subscribed titles
    #this is # of OA papers divided by total papers        
    elsevier_freedom_collection = rf.make_freedom_collection_provider()
    elsevier_subscribed_titles = rf.make_elsevier_subscribed_titles_provider()
    elsevier_unmatched_titles = rf.make_elsevier_unmatched_provider()
    
    elsevier_providers = [elsevier_freedom_collection, elsevier_subscribed_titles, elsevier_unmatched_titles]
    
    for provider_name in elsevier_providers:

        percent_oa_papers_by_year = []
        
        oa_papers_2008 = provider_name['2008.2'].tolist()
        total_2008 = provider_name['2008.4'].tolist()
        percent_oa_papers_by_year.append(sum(oa_papers_2008)/sum(total_2008))
        oa_papers_2009 = provider_name['2009.2'].tolist()
        total_2009 = provider_name['2009.4'].tolist()
        percent_oa_papers_by_year.append(sum(oa_papers_2009)/sum(total_2009))
        oa_papers_2010 = provider_name['2010.2'].tolist()
        total_2010 = provider_name['2010.4'].tolist()
        percent_oa_papers_by_year.append(sum(oa_papers_2010)/sum(total_2010))
        oa_papers_2011 = provider_name['2010.2'].tolist()
        total_2011 = provider_name['2011.4'].tolist()
        percent_oa_papers_by_year.append(sum(oa_papers_2011)/sum(total_2011))
        oa_papers_2012 = provider_name['2012.2'].tolist()
        total_2012 = provider_name['2012.4'].tolist()
        percent_oa_papers_by_year.append(sum(oa_papers_2012)/sum(total_2012))
        oa_papers_2013 = provider_name['2013.2'].tolist()
        total_2013 = provider_name['2013.4'].tolist()
        percent_oa_papers_by_year.append(sum(oa_papers_2013)/sum(total_2013))
        oa_papers_2014 = provider_name['2014.2'].tolist()
        total_2014 = provider_name['2014.4'].tolist()
        percent_oa_papers_by_year.append(sum(oa_papers_2014)/sum(total_2014))
        oa_papers_2015 = provider_name['2015.2'].tolist()
        total_2015 = provider_name['2015.4'].tolist()
        percent_oa_papers_by_year.append(sum(oa_papers_2015)/sum(total_2015))
        oa_papers_2016 = provider_name['2016.2'].tolist()
        total_2016 = provider_name['2016.4'].tolist()
        percent_oa_papers_by_year.append(sum(oa_papers_2016)/sum(total_2016))
        oa_papers_2017 = provider_name['2017.2'].tolist()
        total_2017 = provider_name['2017.4'].tolist()
        percent_oa_papers_by_year.append(sum(oa_papers_2017)/sum(total_2017))
        
        percent_oa_papers_by_provider.append(percent_oa_papers_by_year)

    years = ['2008','2009','2010','2011','2012','2013','2014','2015','2016','2017']

    plt.figure(num=None, figsize=(10,10))
    plt.suptitle(f'Percent of all Open Access by provider')
    plt.xlabel('Year')
    plt.ylabel('Percentage')
        
    plt.gca().yaxis.set_major_formatter(StrMethodFormatter('{x:,.0%}'))    #formats y axis as %

    plt.plot(years, percent_oa_papers_by_provider[0], label='Sage', color='blue')
    plt.plot(years, percent_oa_papers_by_provider[1], label='Springer', color='green')
    plt.plot(years, percent_oa_papers_by_provider[2], label='Taylor & Francis', color='purple')
    plt.plot(years, percent_oa_papers_by_provider[3], label='Wiley', color='orange')
    plt.plot(years, percent_oa_papers_by_provider[4], label='Elsevier Freedom', color='red', linestyle='dashed')
    plt.plot(years, percent_oa_papers_by_provider[5], label='Elsevier Subscribed', color='red')
    plt.plot(years, percent_oa_papers_by_provider[6], label='Elsevier Unmatched', color='black')
        
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.8))




