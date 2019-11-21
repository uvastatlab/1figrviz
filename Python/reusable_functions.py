#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 15:05:10 2019

@author: ep9k
"""

def make_elsevier_subscribed_titles_provider():
    """ Checks subscribed title list from 'Elsevier_2019' file, subscribed journals list tab, (637 subscribed titles). Uses ISSN of each title and checks that against the
    UVA_1figr_original_dataset to see if ISSN is in any Elsevier title. 
    
    Creates elsevier subscribed titles provider as pandas dataframe, which is used to create various figures in other files."""
    
    
    subscribed_journal_list = pd.read_excel('/Users/ep9k/Desktop/UVA Big Deal/Elsevier_2019.xlsx', sheet_name='Subscribed Journal List 2019')
#    original_1figr_dataset = pd.read_excel(filename, sheet_name='Journals per Provider', skiprows=8)
    original_1figr_dataset = pd.read_excel('JournalsPerProvider.xls', skiprows=8)

    subscribed_journal_list_issns = subscribed_journal_list['ISSN'].tolist()  #637 issn #s in list   
    
#    subscribed_journals_subset = elsevier_journal_list[elsevier_journal_list['ISSN'].isin(subscribed_journal_list_issns)]  #634 journals
    
    provider_name = 'Elsevier'
    subset_by_provider = original_1figr_dataset.loc[original_1figr_dataset['Provider'] == provider_name]     #2803 journals

#    #logic to match the ISSN string from the subscribed_titles_issns list to any of the ISSN/eISSN numbers for elsevier titles
    subscribed_titles_subset = subset_by_provider[subset_by_provider['ISSN/eISSN'].str.split(expand=True).isin(subscribed_journal_list_issns).any(1)]    #610 titles matched with Original 1Figr Data
    subscribed_titles_subset = subscribed_titles_subset.iloc[1:]            #first column is an aggregator for entire elsevier provider and must be dropped

    
    return subscribed_titles_subset
    




def make_freedom_collection_provider():
    """These will be the Elsevier tiles which we do not subscribe to, the Freedom Collection titles, from the 'Elsevier_2019' dataset. First, uses
    ISSN of each title from 'Elsevier 2019' dataset, subscribed journals list tab, (638 titles). Uses ISSN of each title to extract the ones that do not
    match from the Elsevier Journal List 2019 tab and gets the ISSNs of the freedom collection. Then uses those ISSNs to check against UVA_1figr_original_dataset
    to see if ISSN is in any Elsevier title.
    
    Creates elsevier freedom collection provider as pandas dataframe, which is used to create various figures in other files."""
    
    subscribed_journal_list = pd.read_excel('/Users/ep9k/Desktop/UVA Big Deal/Elsevier_2019.xlsx', sheet_name='Subscribed Journal List 2019')
    elsevier_journal_list = pd.read_excel('/Users/ep9k/Desktop/UVA Big Deal/Elsevier_2019.xlsx', sheet_name='Elsevier Journal List 2019')
#    original_1figr_dataset = pd.read_excel(filename, sheet_name='Journals per Provider', skiprows=8)
    original_1figr_dataset = pd.read_excel('JournalsPerProvider.xls', skiprows=8)


    subscribed_journal_list_issns = subscribed_journal_list['ISSN'].tolist()
    
    freedom_collection_subset = elsevier_journal_list[elsevier_journal_list['ISSN'].isin(subscribed_journal_list_issns) == False]
    
    freedom_collection_subset_issns = freedom_collection_subset['ISSN'].tolist()   #1328 titles
    
    provider_name = 'Elsevier'
    subset_by_provider = original_1figr_dataset.loc[original_1figr_dataset['Provider'] == provider_name]     #2803 journals
    

    #logic to get the 'freedom collection' providers from the Elsevier Journal List   
    freedom_collection_subset = subset_by_provider[subset_by_provider['ISSN/eISSN'].str.split(expand=True).isin(freedom_collection_subset_issns).any(1)]    #1122 titles


    return freedom_collection_subset