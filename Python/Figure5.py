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


def figure5a_total_papers():
    """Plots # of papers published by all big 5 providers per year
    
    Chart Type: Line graph
    Y-Axis: Number of Papers
    Y-Axis Data Source: Original 1Figr Dataset 
    
    X-Axis: Year
    X-Axis Data Source: Original 1Figr Dataset
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
    
    
def figure5a_papers():
    """Plots # of UVA authored publications in each of the big 5 providers over time (2008-2017)
    Looks at columns under 'Papers per journal/provider by your institution's authors
    
    Chart Type: Line graph
    Y-Axis: Number of Papers
    Y-Axis Data Source: Original 1Figr Dataset 
    
    X-Axis: Year
    X-Axis Data Source: Original 1Figr Dataset
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
    plt.suptitle(f'Number of UVA Authored Papers by Year')
    plt.xlabel('Year')
    plt.ylabel('Paper Count')

    #change this to be dynamic instead of hard coded
    plt.plot(years, publications_by_provider[0], label='Elsevier')
    plt.plot(years, publications_by_provider[1], label='Sage')
    plt.plot(years, publications_by_provider[2], label='Springer')
    plt.plot(years, publications_by_provider[3], label='Taylor & Francis')
    plt.plot(years, publications_by_provider[4], label='Wiley')


def figure5a_percentage():
    """Plots percentage of UVA authored papers in each of the big 5 providers over time (2008-2017)
    Divides # UVA authored papers for current year by total number of papers in that journal.
    For example, this is 'papers_2008' / total_2008
    
    Chart Type: Line graph
    Y-Axis: Number of Papers
    Y-Axis Data Source: Original 1Figr Dataset 
    
    X-Axis: Year
    X-Axis Data Source: Original 1Figr Dataset
    """
    
    data = pd.read_csv('JournalsPerProvider.csv', skiprows=8)
    
    big5 = ['Elsevier', 'Sage', 'Springer', 'Taylor & Francis', 'Wiley']

    percentage_by_provider = []
    
    for provider_name in big5:

        subset_by_provider = data.loc[data['Provider'] == provider_name]
        
        percentage_per_year = []
        
        uva_2008 = subset_by_provider.papers_2008.tolist()
        total_2008 = subset_by_provider.total_2008.tolist()
        percentage_per_year.append(uva_2008[0] / total_2008[0])
        
        uva_2009 = subset_by_provider.papers_2009.tolist()
        total_2009 = subset_by_provider.total_2009.tolist()
        percentage_per_year.append(uva_2009[0] / total_2009[0])
        
        uva_2010 = subset_by_provider.papers_2010.tolist()
        total_2010 = subset_by_provider.total_2010.tolist()
        percentage_per_year.append(uva_2010[0] / total_2010[0])
        
        uva_2011 = subset_by_provider.papers_2011.tolist()
        total_2011 = subset_by_provider.total_2011.tolist()
        percentage_per_year.append(uva_2011[0] / total_2011[0])
        
        uva_2012 = subset_by_provider.papers_2012.tolist()
        total_2012 = subset_by_provider.total_2012.tolist()
        percentage_per_year.append(uva_2012[0] / total_2012[0])
        
        uva_2013 = subset_by_provider.papers_2013.tolist()
        total_2013 = subset_by_provider.total_2013.tolist()
        percentage_per_year.append(uva_2013[0] / total_2013[0])
        
        uva_2014 = subset_by_provider.papers_2014.tolist()
        total_2014 = subset_by_provider.total_2014.tolist()
        percentage_per_year.append(uva_2014[0] / total_2014[0])
        
        uva_2015 = subset_by_provider.papers_2015.tolist()
        total_2015 = subset_by_provider.total_2015.tolist()
        percentage_per_year.append(uva_2015[0] / total_2015[0])
        
        uva_2016 = subset_by_provider.papers_2016.tolist()
        total_2016 = subset_by_provider.total_2016.tolist()
        percentage_per_year.append(uva_2016[0] / total_2016[0])
        
        uva_2017 = subset_by_provider.papers_2017.tolist()
        total_2017 = subset_by_provider.total_2017.tolist()
        percentage_per_year.append(uva_2017[0] / total_2017[0])
        
        percentage_by_provider.append(percentage_per_year)
        
    years = ['2008','2009','2010','2011','2012','2013','2014','2015','2016','2017']
       
    
    #build plot
    plt.figure(num=None, figsize=(10, 10))

    plt.suptitle(f'Percentage of UVA Authored Papers of All Papers by Year by Provider')
    plt.xlabel('Year')
    plt.ylabel('Percent of Total Papers')
    plt.ylim(0, 0.004)

    plt.gca().yaxis.set_major_formatter(StrMethodFormatter('{x:,.3%}'))    #formats y axis as %

#    plt.plot(years, percentage_by_provider[0])
    plt.plot(years, percentage_by_provider[0], label='Elsevier')
    plt.plot(years, percentage_by_provider[1], label='Sage')
    plt.plot(years, percentage_by_provider[2], label='Springer')
    plt.plot(years, percentage_by_provider[3], label='Taylor & Francis')
    plt.plot(years, percentage_by_provider[4], label='Wiley')

    
    

def figure5b_papers():
    """Show papers per year (2008-2017) by your institution's affiliated authors, separating Elsevier Freedom
    and Elsevier Subscribed titles out from Elsevier as a whole.  Papers are publications
    by you institution's affiliated authors.
    
    Chart Type: Line Graph
    Y-Axis: Number of Papers
    Y-Axis Data Source: Original 1Figr Dataset, Journals Per Provider, Total papers in Scopus per journal/provider
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


    #this holds papers totals for all providers in the end, which is used to make final plot
    papers_by_provider = []
    
    #populate papers totals for elsevier subset providers    
    elsevier_providers = [elsevier_freedom_collection, elsevier_subscribed_titles, elsevier_unmatched_titles]
    
    
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
        
    
    #populate papers totals for other providers    
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
    plt.suptitle(f'Number of Articles (papers) by {your_institution} Authors')
    plt.xlabel('Year')
    plt.ylabel('Number of Articles')


    plt.plot(years, papers_by_provider[0], label='Elsevier Freedom', color='red', linestyle='dashed')
    plt.plot(years, papers_by_provider[1], label='Elsevier Subscribed', color='red')
    plt.plot(years, papers_by_provider[2], label='Elsevier Unmatched Titles', color='black')
    plt.plot(years, papers_by_provider[3], label='Sage', color='blue')
    plt.plot(years, papers_by_provider[4], label='Springer', color='green')
    plt.plot(years, papers_by_provider[5], label='Taylor & Francis', color='purple')
    plt.plot(years, papers_by_provider[6], label='Wiley', color='orange')

    plt.legend(loc='center left', bbox_to_anchor=(1, 0.8))



def figure5b_percentage():
    """ Show percent papers per year published by UVA authors as a percentage of all papers for each provider, separating Elsevier Freedom
    and Elsevier Subscribed titles out from Elsevier as a whole. All papers are the 'total papers in scopus' columns
    
    Chart Type: Line Graph
    Y-Axis: Number of Papers
    Y-Axis Data Source: Original 1Figr Dataset, Journals Per Provider, Total papers in Scopus per journal/provider
                        Elsevier_2019, Subscribed Journal List 2019
    X-Axis: Year
    X-Axis Data Source: Original 1Figr Dataset, Journals Per Provider, Provider
                        Elsevier_2019, Subscribed Journal List 2019 
    """
    
    #    original_1figr_dataset = pd.read_excel(filename, sheet_name='Journals per Provider', skiprows=8)   
    original_1figr_dataset = pd.read_excel('JournalsPerProvider.xls', skiprows=8)

    #holds percent papers per year published by UVA authors of total papers per provider
    percent_papers_by_provider = []


    #populate papers totals for other providers    
    providers = ['Sage', 'Springer', 'Taylor & Francis', 'Wiley']

    for provider_name in providers:

        percent_papers_by_year = []
        
        subset_by_provider = original_1figr_dataset.loc[original_1figr_dataset['Provider'] == provider_name]
    
        papers_2008 = subset_by_provider[2008].tolist()
        total_2008 = subset_by_provider['2008.4'].tolist()
        percent_papers_by_year.append(sum(papers_2008)/sum(total_2008))
        papers_2009 = subset_by_provider[2009].tolist()
        total_2009 = subset_by_provider['2009.4'].tolist()
        percent_papers_by_year.append(sum(papers_2009)/sum(total_2009))
        papers_2010 = subset_by_provider[2010].tolist()
        total_2010 = subset_by_provider['2010.4'].tolist()
        percent_papers_by_year.append(sum(papers_2010)/sum(total_2010))
        papers_2011 = subset_by_provider[2011].tolist()
        total_2011 = subset_by_provider['2011.4'].tolist()
        percent_papers_by_year.append(sum(papers_2011)/sum(total_2011)) 
        papers_2012 = subset_by_provider[2012].tolist()
        total_2012 = subset_by_provider['2012.4'].tolist()
        percent_papers_by_year.append(sum(papers_2012)/sum(total_2012))
        papers_2013 = subset_by_provider[2013].tolist()
        total_2013 = subset_by_provider['2013.4'].tolist()
        percent_papers_by_year.append(sum(papers_2013)/sum(total_2013)) 
        papers_2014 = subset_by_provider[2014].tolist()
        total_2014 = subset_by_provider['2014.4'].tolist()
        percent_papers_by_year.append(sum(papers_2014)/sum(total_2014))
        papers_2015 = subset_by_provider[2015].tolist()
        total_2015 = subset_by_provider['2015.4'].tolist()
        percent_papers_by_year.append(sum(papers_2015)/sum(total_2015))        
        papers_2016 = subset_by_provider[2016].tolist()
        total_2016 = subset_by_provider['2016.4'].tolist()
        percent_papers_by_year.append(sum(papers_2016)/sum(total_2016)) 
        papers_2017 = subset_by_provider[2017].tolist()
        total_2017 = subset_by_provider['2017.4'].tolist()
        percent_papers_by_year.append(sum(papers_2017)/sum(total_2017))
        
        percent_papers_by_provider.append(percent_papers_by_year)
        
        
    #populate papers totals for elsevier freedom and elsevier subscribed providers
    elsevier_freedom_collection = rf.make_freedom_collection_provider()
    elsevier_subscribed_titles = rf.make_elsevier_subscribed_titles_provider()
    elsevier_unmatched_titles = rf.make_elsevier_unmatched_provider()
    
    elsevier_providers = [elsevier_freedom_collection, elsevier_subscribed_titles, elsevier_unmatched_titles]
    
    for provider_name in elsevier_providers:

        percent_papers_by_year = []
        
        papers_2008 = provider_name[2008].tolist()
        total_2008 = provider_name['2008.4'].tolist()
        percent_papers_by_year.append(sum(papers_2008)/sum(total_2008))
        papers_2009 = provider_name[2009].tolist()
        total_2009 = provider_name['2009.4'].tolist()
        percent_papers_by_year.append(sum(papers_2009)/sum(total_2009))
        papers_2010 = provider_name[2010].tolist()
        total_2010 = provider_name['2010.4'].tolist()
        percent_papers_by_year.append(sum(papers_2010)/sum(total_2010))
        papers_2011 = provider_name[2011].tolist()
        total_2011 = provider_name['2011.4'].tolist()
        percent_papers_by_year.append(sum(papers_2011)/sum(total_2011)) 
        papers_2012 = provider_name[2012].tolist()
        total_2012 = provider_name['2012.4'].tolist()
        percent_papers_by_year.append(sum(papers_2012)/sum(total_2012))
        papers_2013 = provider_name[2013].tolist()
        total_2013 = provider_name['2013.4'].tolist()
        percent_papers_by_year.append(sum(papers_2013)/sum(total_2013)) 
        papers_2014 = provider_name[2014].tolist()
        total_2014 = provider_name['2014.4'].tolist()
        percent_papers_by_year.append(sum(papers_2014)/sum(total_2014))
        papers_2015 = provider_name[2015].tolist()
        total_2015 = provider_name['2015.4'].tolist()
        percent_papers_by_year.append(sum(papers_2015)/sum(total_2015))        
        papers_2016 = provider_name[2016].tolist()
        total_2016 = provider_name['2016.4'].tolist()
        percent_papers_by_year.append(sum(papers_2016)/sum(total_2016)) 
        papers_2017 = provider_name[2017].tolist()
        total_2017 = provider_name['2017.4'].tolist()
        percent_papers_by_year.append(sum(papers_2017)/sum(total_2017))

        
        percent_papers_by_provider.append(percent_papers_by_year)
        
        
    years = ['2008','2009','2010','2011','2012','2013','2014','2015','2016','2017']

    plt.figure(num=None, figsize=(10,10))
    plt.suptitle(f'Percent of All Articles published by {your_institution} Authors')
    plt.xlabel('Year')
    plt.ylabel('Percentage')
        
    plt.gca().yaxis.set_major_formatter(StrMethodFormatter('{x:,.2%}'))    #formats y axis as %

    plt.plot(years, percent_papers_by_provider[0], label='Sage', color='blue')
    plt.plot(years, percent_papers_by_provider[1], label='Springer', color='green')
    plt.plot(years, percent_papers_by_provider[2], label='Taylor & Francis', color='purple')
    plt.plot(years, percent_papers_by_provider[3], label='Wiley', color='orange')
    plt.plot(years, percent_papers_by_provider[4], label='Elsevier Freedom', color='red', linestyle='dashed')
    plt.plot(years, percent_papers_by_provider[5], label='Elsevier Subscribed', color='red')
    plt.plot(years, percent_papers_by_provider[6], label='Elsevier Unmatched', color='black')
        
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.8))
    

