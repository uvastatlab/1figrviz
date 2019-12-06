#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 15:05:10 2019

@author: ep9k
"""

import pandas as pd


filename = 'JournalsPerProvider.xls'

def make_elsevier_subscribed_titles_provider():
    """ Checks subscribed title list from 'Elsevier_2019' file, subscribed journals list tab, (637 subscribed titles). Uses ISSN of each title and checks that against the
    UVA_1figr_original_dataset to see if ISSN is in any Elsevier title. 
    
    Creates elsevier subscribed titles provider as pandas dataframe, which is used to create various figures in other files."""
    
    
    subscribed_journal_list = pd.read_excel('/Users/ep9k/Desktop/UVA Big Deal/Elsevier_2019_Dec_05.xlsx', sheet_name='All Subscribed Journals')
#    original_1figr_dataset = pd.read_excel(filename, sheet_name='Journals per Provider', skiprows=8)
    original_1figr_dataset = pd.read_excel('JournalsPerProvider.xls', skiprows=8)

    subscribed_journal_list = subscribed_journal_list[pd.notnull(subscribed_journal_list['ISSN'])]   #removes null values
    subscribed_journal_list_issns = subscribed_journal_list['ISSN'].tolist()
        
    provider_name = 'Elsevier'
    subset_by_provider = original_1figr_dataset.loc[original_1figr_dataset['Provider'] == provider_name]     #2803 journals

    #logic to match the ISSN string from the subscribed_titles_issns list to any of the ISSN/eISSN numbers for elsevier titles
    subscribed_titles_subset = subset_by_provider[subset_by_provider['ISSN/eISSN'].str.split(expand=True).isin(subscribed_journal_list_issns).any(1)]    #678 titles matched with Original 1Figr Data
    subscribed_titles_subset = subscribed_titles_subset.iloc[1:]            #first column is an aggregator for entire elsevier provider and must be dropped

    return subscribed_titles_subset
    


def make_elsevier_subscribed_titles_with_disciplines(input_dataframe):
    """First, you must run the make_disciplines_column function to add the disciplines column to the original 1figr data. That result is used as input to this function.
    Then, checks subscribed title list from 'Elsevier_2019' file, subscribed journals list tab, (637 subscribed titles). Uses ISSN of each title and checks that against the
    UVA_1figr_original_dataset to see if ISSN is in any Elsevier title. 
    
    Creates elsevier subscribed titles provider as pandas dataframe, including the discipline column, which is used to create various figures 8e through 8h."""

#    subscribed_journal_list = pd.read_excel('/Users/ep9k/Desktop/UVA Big Deal/Elsevier_2019.xlsx', sheet_name='Subscribed Journal List 2019')
    subscribed_journal_list = pd.read_excel('/Users/ep9k/Desktop/UVA Big Deal/Elsevier_2019_Dec_05.xlsx', sheet_name='All Subscribed Journals')

    subscribed_journal_list = subscribed_journal_list[pd.notnull(subscribed_journal_list['ISSN'])]   #removes null values    
    subscribed_journal_list_issns = subscribed_journal_list['ISSN'].tolist()     
        
#    subscribed_journals_subset = elsevier_journal_list[elsevier_journal_list['ISSN'].isin(subscribed_journal_list_issns)]  
    
    provider_name = 'Elsevier'
    subset_by_provider = input_dataframe.loc[input_dataframe['Provider'] == provider_name]     #2803 journals

#    #logic to match the ISSN string from the subscribed_titles_issns list to any of the ISSN/eISSN numbers for elsevier titles
    subscribed_titles_subset = subset_by_provider[subset_by_provider['ISSN/eISSN'].str.split(expand=True).isin(subscribed_journal_list_issns).any(1)]    #678 titles
    subscribed_titles_subset = subscribed_titles_subset.iloc[1:]            #first column is an aggregator for entire elsevier provider and must be dropped

    return subscribed_titles_subset



def make_freedom_collection_provider():
    """Checks freedom title list from 'Elsevier_2019' file, All Freedom Journals tab, (1162 titles). Uses ISSN of each title and checks that against the
    UVA_1figr_original_dataset to see if ISSN is in any Elsevier title.
    
    Creates elsevier freedom collection provider as pandas dataframe, which is used to create various figures in other files."""
    
    freedom_journal_list = pd.read_excel('/Users/ep9k/Desktop/UVA Big Deal/Elsevier_2019_Dec_05.xlsx', sheet_name='All Freedom Journals')
#    original_1figr_dataset = pd.read_excel(filename, sheet_name='Journals per Provider', skiprows=8)
    original_1figr_dataset = pd.read_excel('JournalsPerProvider.xls', skiprows=8)

    freedom_journal_list = freedom_journal_list[pd.notnull(freedom_journal_list['ISSN'])]   #removes null values
    freedom_journal_list_issns = freedom_journal_list['ISSN'].tolist()      #1162 issn #s in list

    provider_name = 'Elsevier'
    subset_by_provider = original_1figr_dataset.loc[original_1figr_dataset['Provider'] == provider_name]     #2803 journals

    #logic to get the 'freedom collection' providers from the Elsevier Journal List   
    freedom_collection_subset = subset_by_provider[subset_by_provider['ISSN/eISSN'].str.split(expand=True).isin(freedom_journal_list_issns).any(1)]   #1084 titles 

    return freedom_collection_subset



def make_freedom_collection_provider_with_disciplines(input_dataframe):
    """First, you must run the make_disciplines_column function to add the disciplines column to the original 1figr data. That result is used as input to this function.

    Checks freedom title list from 'Elsevier_2019' file, All Freedom Journals tab, (1162 titles). Uses ISSN of each title and checks that against the
    UVA_1figr_original_dataset to see if ISSN is in any Elsevier title. Then uses those ISSNs to check against UVA_1figr_original_dataset
    to see if ISSN is in any Elsevier title.
    
    Creates elsevier freedom collection provider as pandas dataframe, which is used to create various figures in other files."""
   
    freedom_journal_list = pd.read_excel('/Users/ep9k/Desktop/UVA Big Deal/Elsevier_2019_Dec_05.xlsx', sheet_name='All Freedom Journals')

    freedom_journal_list = freedom_journal_list[pd.notnull(freedom_journal_list['ISSN'])]   #removes null values
    freedom_journal_list_issns = freedom_journal_list['ISSN'].tolist()
        
    provider_name = 'Elsevier'
    subset_by_provider = input_dataframe.loc[input_dataframe['Provider'] == provider_name]     #2803 journals
    
    #logic to get the 'freedom collection' providers from the Elsevier Journal List   
    freedom_collection_subset = subset_by_provider[subset_by_provider['ISSN/eISSN'].str.split(expand=True).isin(freedom_journal_list_issns).any(1)]    #1084 titles

    return freedom_collection_subset


def make_elsevier_unmatched_provider():
    """Elsevier unmatched titles are those which have an ISSN number that is not present in either the Elsevier Subscribed titles list or the elsevier freedom
    collection list. We are unsure what is going on here, so we have separated them into a third category.
    
    Checks subscribed titles list from 'elsevier_2019' All Subscribed Titles tab and freedom titles list from the All Freedom Journals tab to build list of
    all known ISSN numbers. Then takes that list and compares it to Original 1Figr Dataset's (ISSN/eISSN) column. If there is NOT a match, the journal is assumed
    to be an elsevier unmatched journal.
    """

#    original_1figr_dataset = pd.read_excel(filename, sheet_name='Journals per Provider', skiprows=8)
    original_1figr_dataset = pd.read_excel('JournalsPerProvider.xls', skiprows=8)
    
    subscribed_journal_list = pd.read_excel('/Users/ep9k/Desktop/UVA Big Deal/Elsevier_2019_Dec_05.xlsx', sheet_name='All Subscribed Journals')
    freedom_journal_list = pd.read_excel('/Users/ep9k/Desktop/UVA Big Deal/Elsevier_2019_Dec_05.xlsx', sheet_name='All Freedom Journals')

    subscribed_journal_list = subscribed_journal_list[pd.notnull(subscribed_journal_list['ISSN'])]   #removes null values
    subscribed_journal_list_issns = subscribed_journal_list['ISSN'].tolist()                #681 Journals
    
    freedom_journal_list = freedom_journal_list[pd.notnull(freedom_journal_list['ISSN'])]   #removes null values
    freedom_journal_list_issns = freedom_journal_list['ISSN'].tolist()              #1162 Journals
    
    combined_issn_list = subscribed_journal_list_issns + freedom_journal_list_issns  #1843 journals
    
    provider_name = 'Elsevier'
    subset_by_provider = original_1figr_dataset.loc[original_1figr_dataset['Provider'] == provider_name]     #2803 journals
    
    #matches combined_issn_list to subscribed_titles_subset
    unmatched_titles_subset = subset_by_provider[subset_by_provider['ISSN/eISSN'].str.split(expand=True).isin(combined_issn_list).any(1) == False]     #1041 titles

    unmatched_titles_subset.to_csv('/Users/ep9k/Desktop/UVA Big Deal/Elsevier_Unmatched_Titles.csv')
    
    return unmatched_titles_subset


def make_elsevier_unmatched_provider_with_disciplines(input_dataframe):
    """First, you must run the make_disciplines_column function to add the disciplines column to the original 1figr data. That result is used as input to this function.

    Checks freedom title list from 'Elsevier_2019' file, All Subscribed Journals and All Freedom Journals tab. Uses ISSN of each title and checks that against the
    UVA_1figr_original_dataset to see if ISSN is in any Elsevier title. If there is NOT a match, the journals is assumed to be a part of the 'elsevier unmatched' provicer.
    Then assigns values in discipline column to each journal.
    
    Creates elsevier freedom collection provider as pandas dataframe, which is used to create various figures in other files."""
    
#    original_1figr_dataset = pd.read_excel(filename, sheet_name='Journals per Provider', skiprows=8)
    original_1figr_dataset = pd.read_excel('JournalsPerProvider.xls', skiprows=8)
    
    subscribed_journal_list = pd.read_excel('/Users/ep9k/Desktop/UVA Big Deal/Elsevier_2019_Dec_05.xlsx', sheet_name='All Subscribed Journals')
    freedom_journal_list = pd.read_excel('/Users/ep9k/Desktop/UVA Big Deal/Elsevier_2019_Dec_05.xlsx', sheet_name='All Freedom Journals')

    subscribed_journal_list = subscribed_journal_list[pd.notnull(subscribed_journal_list['ISSN'])]   #removes null values
    subscribed_journal_list_issns = subscribed_journal_list['ISSN'].tolist()                #681 Journals
    
    freedom_journal_list = freedom_journal_list[pd.notnull(freedom_journal_list['ISSN'])]   #removes null values
    freedom_journal_list_issns = freedom_journal_list['ISSN'].tolist()              #1162 Journals
    
    combined_issn_list = subscribed_journal_list_issns + freedom_journal_list_issns  #1843 journals

    provider_name = 'Elsevier'
    subset_by_provider = input_dataframe.loc[input_dataframe['Provider'] == provider_name]     #2803 journals

    #logic to get the 'elsevier unmatched' providers from the Elsevier Journal List   
    elsevier_unmatched_subset = subset_by_provider[subset_by_provider['ISSN/eISSN'].str.split(expand=True).isin(combined_issn_list).any(1) == False]    #1084 titles
   
    return elsevier_unmatched_subset
    
    
def make_disciplines_column():
    """This generates the disciplines column on the fly for each journal. The disciplines column in a combination of various permutations of each journal's
    domain, field, subfield columns. The discipline column is meant to be something more analagous to departments at the university. The disciplines column does
    not currently exist in the original 1figr dataset and therefore must be generated upon running this function."""

#    original_1figr_dataset = pd.read_excel(filename, sheet_name='Journals per Provider', skiprows=8)
    original_1figr_dataset = pd.read_excel('JournalsPerProvider.xls', skiprows=8)

    #logic for every permutation of domain, field, subfield column with the end result defined in the "disciplines" column    

    #Applied Sciences Domain
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Applied Sciences') & (original_1figr_dataset['Field'] == 'Agriculture, Fisheries & Forestry') & (original_1figr_dataset['Subfield'] == 'Agronomy & Agriculture'), 'Discipline'] = 'Earth & Environmental Sciences'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Applied Sciences') & (original_1figr_dataset['Field'] == 'Agriculture, Fisheries & Forestry') & (original_1figr_dataset['Subfield'] == 'Dairy & Animal Science'), 'Discipline'] = 'Earth & Environmental Sciences'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Applied Sciences') & (original_1figr_dataset['Field'] == 'Agriculture, Fisheries & Forestry') & (original_1figr_dataset['Subfield'] == 'Fisheries'), 'Discipline'] = 'Earth & Environmental Sciences'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Applied Sciences') & (original_1figr_dataset['Field'] == 'Agriculture, Fisheries & Forestry') & (original_1figr_dataset['Subfield'] == 'Food Science'), 'Discipline'] = 'Earth & Environmental Sciences'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Applied Sciences') & (original_1figr_dataset['Field'] == 'Agriculture, Fisheries & Forestry') & (original_1figr_dataset['Subfield'] == 'Forestry'), 'Discipline'] = 'Earth & Environmental Sciences'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Applied Sciences') & (original_1figr_dataset['Field'] == 'Agriculture, Fisheries & Forestry') & (original_1figr_dataset['Subfield'] == 'Horticulture'), 'Discipline'] = 'Earth & Environmental Sciences'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Applied Sciences') & (original_1figr_dataset['Field'] == 'Agriculture, Fisheries & Forestry') & (original_1figr_dataset['Subfield'] == 'Veterinary Sciences'), 'Discipline'] = 'Earth & Environmental Sciences'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Applied Sciences') & (original_1figr_dataset['Field'] == 'Built Environment & Design') & (original_1figr_dataset['Subfield'] == 'Architecture'), 'Discipline'] = 'Architecture'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Applied Sciences') & (original_1figr_dataset['Field'] == 'Built Environment & Design') & (original_1figr_dataset['Subfield'] == 'Building & Construction'), 'Discipline'] = 'Architecture'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Applied Sciences') & (original_1figr_dataset['Field'] == 'Built Environment & Design') & (original_1figr_dataset['Subfield'] == 'Design Practice & Management'), 'Discipline'] = 'Architecture'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Applied Sciences') & (original_1figr_dataset['Field'] == 'Built Environment & Design') & (original_1figr_dataset['Subfield'] == 'Urban & Regional Planning'), 'Discipline'] = 'Architecture'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Applied Sciences') & (original_1figr_dataset['Field'] == 'Enabling & Strategic Technologies') & (original_1figr_dataset['Subfield'] == 'Bioinformatics'), 'Discipline'] = 'Health Sciences'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Applied Sciences') & (original_1figr_dataset['Field'] == 'Enabling & Strategic Technologies') & (original_1figr_dataset['Subfield'] == 'Biotechnology'), 'Discipline'] = 'Engineering'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Applied Sciences') & (original_1figr_dataset['Field'] == 'Enabling & Strategic Technologies') & (original_1figr_dataset['Subfield'] == 'Energy'), 'Discipline'] = 'Engineering'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Applied Sciences') & (original_1figr_dataset['Field'] == 'Enabling & Strategic Technologies') & (original_1figr_dataset['Subfield'] == 'Materials'), 'Discipline'] = 'Engineering'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Applied Sciences') & (original_1figr_dataset['Field'] == 'Enabling & Strategic Technologies') & (original_1figr_dataset['Subfield'] == 'Nanoscience & Nanotechnology'), 'Discipline'] = 'Engineering'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Applied Sciences') & (original_1figr_dataset['Field'] == 'Enabling & Strategic Technologies') & (original_1figr_dataset['Subfield'] == 'Optoelectronics & Photonics'), 'Discipline'] = 'Engineering'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Applied Sciences') & (original_1figr_dataset['Field'] == 'Enabling & Strategic Technologies') & (original_1figr_dataset['Subfield'] == 'Strategic, Defence & Security Studies'), 'Discipline'] = 'Engineering'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Applied Sciences') & (original_1figr_dataset['Field'] == 'Engineering') & (original_1figr_dataset['Subfield'] == 'Aerospace & Aeronautics'), 'Discipline'] = 'Engineering'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Applied Sciences') & (original_1figr_dataset['Field'] == 'Engineering') & (original_1figr_dataset['Subfield'] == 'Automobile Design & Engineering'), 'Discipline'] = 'Engineering'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Applied Sciences') & (original_1figr_dataset['Field'] == 'Engineering') & (original_1figr_dataset['Subfield'] == 'Biomedical Engineering'), 'Discipline'] = 'Engineering'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Applied Sciences') & (original_1figr_dataset['Field'] == 'Engineering') & (original_1figr_dataset['Subfield'] == 'Chemical Engineering'), 'Discipline'] = 'Engineering'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Applied Sciences') & (original_1figr_dataset['Field'] == 'Engineering') & (original_1figr_dataset['Subfield'] == 'Civil Engineering'), 'Discipline'] = 'Engineering'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Applied Sciences') & (original_1figr_dataset['Field'] == 'Engineering') & (original_1figr_dataset['Subfield'] == 'Electrical & Electronic Engineering'), 'Discipline'] = 'Engineering'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Applied Sciences') & (original_1figr_dataset['Field'] == 'Engineering') & (original_1figr_dataset['Subfield'] == 'Environmental Engineering'), 'Discipline'] = 'Engineering'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Applied Sciences') & (original_1figr_dataset['Field'] == 'Engineering') & (original_1figr_dataset['Subfield'] == 'Geological & Geomatics Engineering'), 'Discipline'] = 'Engineering'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Applied Sciences') & (original_1figr_dataset['Field'] == 'Engineering') & (original_1figr_dataset['Subfield'] == 'Industrial Engineering & Automation'), 'Discipline'] = 'Engineering'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Applied Sciences') & (original_1figr_dataset['Field'] == 'Engineering') & (original_1figr_dataset['Subfield'] == 'Mechanical Engineering & Transports'), 'Discipline'] = 'Engineering'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Applied Sciences') & (original_1figr_dataset['Field'] == 'Engineering') & (original_1figr_dataset['Subfield'] == 'Mining & Metallurgy'), 'Discipline'] = 'Engineering'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Applied Sciences') & (original_1figr_dataset['Field'] == 'Engineering') & (original_1figr_dataset['Subfield'] == 'Operations Research'), 'Discipline'] = 'Engineering'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Applied Sciences') & (original_1figr_dataset['Field'] == 'Information & Communication Technologies') & (original_1figr_dataset['Subfield'] == 'Artificial Intelligence & Image Processing'), 'Discipline'] = 'Engineering'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Applied Sciences') & (original_1figr_dataset['Field'] == 'Information & Communication Technologies') & (original_1figr_dataset['Subfield'] == 'Computation Theory & Mathematics'), 'Discipline'] = 'Engineering'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Applied Sciences') & (original_1figr_dataset['Field'] == 'Information & Communication Technologies') & (original_1figr_dataset['Subfield'] == 'Computer Hardware & Architecture'), 'Discipline'] = 'Engineering'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Applied Sciences') & (original_1figr_dataset['Field'] == 'Information & Communication Technologies') & (original_1figr_dataset['Subfield'] == 'Distributed Computing'), 'Discipline'] = 'Engineering'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Applied Sciences') & (original_1figr_dataset['Field'] == 'Information & Communication Technologies') & (original_1figr_dataset['Subfield'] == 'Information Systems'), 'Discipline'] = 'Engineering'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Applied Sciences') & (original_1figr_dataset['Field'] == 'Information & Communication Technologies') & (original_1figr_dataset['Subfield'] == 'Medical Informatics'), 'Discipline'] = 'Health Sciences'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Applied Sciences') & (original_1figr_dataset['Field'] == 'Information & Communication Technologies') & (original_1figr_dataset['Subfield'] == 'Networking & Telecommunications'), 'Discipline'] = 'Engineering'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Applied Sciences') & (original_1figr_dataset['Field'] == 'Information & Communication Technologies') & (original_1figr_dataset['Subfield'] == 'Software Engineering'), 'Discipline'] = 'Engineering'

    #Arts & Humanities Domain
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Arts & Humanities') & (original_1figr_dataset['Field'] == 'Communication & Textual Studies') & (original_1figr_dataset['Subfield'] == 'Communication & Media Studies'), 'Discipline'] = 'Communication & Textual Studies'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Arts & Humanities') & (original_1figr_dataset['Field'] == 'Communication & Textual Studies') & (original_1figr_dataset['Subfield'] == 'Languages & Linguistics'), 'Discipline'] = 'Communication & Textual Studies'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Arts & Humanities') & (original_1figr_dataset['Field'] == 'Communication & Textual Studies') & (original_1figr_dataset['Subfield'] == 'Literary Studies'), 'Discipline'] = 'Communication & Textual Studies'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Arts & Humanities') & (original_1figr_dataset['Field'] == 'Historical Studies') & (original_1figr_dataset['Subfield'] == 'Anthropology'), 'Discipline'] = 'Historical Studies'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Arts & Humanities') & (original_1figr_dataset['Field'] == 'Historical Studies') & (original_1figr_dataset['Subfield'] == 'Archaeology'), 'Discipline'] = 'Historical Studies'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Arts & Humanities') & (original_1figr_dataset['Field'] == 'Historical Studies') & (original_1figr_dataset['Subfield'] == 'Classics'), 'Discipline'] = 'Historical Studies'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Arts & Humanities') & (original_1figr_dataset['Field'] == 'Historical Studies') & (original_1figr_dataset['Subfield'] == 'History'), 'Discipline'] = 'Historical Studies'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Arts & Humanities') & (original_1figr_dataset['Field'] == 'Historical Studies') & (original_1figr_dataset['Subfield'] == 'History of Science, Technology & Medicine'), 'Discipline'] = 'Historical Studies'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Arts & Humanities') & (original_1figr_dataset['Field'] == 'Historical Studies') & (original_1figr_dataset['Subfield'] == 'History of Social Sciences'), 'Discipline'] = 'Historical Studies'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Arts & Humanities') & (original_1figr_dataset['Field'] == 'Philosophy & Theology') & (original_1figr_dataset['Subfield'] == 'Applied Ethics'), 'Discipline'] = 'Philosophy & Theology'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Arts & Humanities') & (original_1figr_dataset['Field'] == 'Philosophy & Theology') & (original_1figr_dataset['Subfield'] == 'Philosophy'), 'Discipline'] = 'Philosophy & Theology'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Arts & Humanities') & (original_1figr_dataset['Field'] == 'Philosophy & Theology') & (original_1figr_dataset['Subfield'] == 'Religions & Theology'), 'Discipline'] = 'Philosophy & Theology'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Arts & Humanities') & (original_1figr_dataset['Field'] == 'Visual & Performing Arts') & (original_1figr_dataset['Subfield'] == 'Art Practice, History & Theory'), 'Discipline'] = 'Visual & Performing Arts'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Arts & Humanities') & (original_1figr_dataset['Field'] == 'Visual & Performing Arts') & (original_1figr_dataset['Subfield'] == 'Drama & Theater'), 'Discipline'] = 'Visual & Performing Arts'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Arts & Humanities') & (original_1figr_dataset['Field'] == 'Visual & Performing Arts') & (original_1figr_dataset['Subfield'] == 'Folklore'), 'Discipline'] = 'Visual & Performing Arts'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Arts & Humanities') & (original_1figr_dataset['Field'] == 'Visual & Performing Arts') & (original_1figr_dataset['Subfield'] == 'Music'), 'Discipline'] = 'Visual & Performing Arts'
    
    #Economic & Social Sciences Domain
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Economic & Social Sciences') & (original_1figr_dataset['Field'] == 'Economics & Business') & (original_1figr_dataset['Subfield'] == 'Accounting'), 'Discipline'] = 'Economics & Business'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Economic & Social Sciences') & (original_1figr_dataset['Field'] == 'Economics & Business') & (original_1figr_dataset['Subfield'] == 'Agricultural Economics & Policy'), 'Discipline'] = 'Economics & Business'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Economic & Social Sciences') & (original_1figr_dataset['Field'] == 'Economics & Business') & (original_1figr_dataset['Subfield'] == 'Business & Management'), 'Discipline'] = 'Economics & Business'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Economic & Social Sciences') & (original_1figr_dataset['Field'] == 'Economics & Business') & (original_1figr_dataset['Subfield'] == 'Development Studies'), 'Discipline'] = 'Economics & Business'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Economic & Social Sciences') & (original_1figr_dataset['Field'] == 'Economics & Business') & (original_1figr_dataset['Subfield'] == 'Econometrics'), 'Discipline'] = 'Economics & Business'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Economic & Social Sciences') & (original_1figr_dataset['Field'] == 'Economics & Business') & (original_1figr_dataset['Subfield'] == 'Economic Theory'), 'Discipline'] = 'Economics & Business'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Economic & Social Sciences') & (original_1figr_dataset['Field'] == 'Economics & Business') & (original_1figr_dataset['Subfield'] == 'Economics'), 'Discipline'] = 'Economics & Business'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Economic & Social Sciences') & (original_1figr_dataset['Field'] == 'Economics & Business') & (original_1figr_dataset['Subfield'] == 'Finance'), 'Discipline'] = 'Economics & Business'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Economic & Social Sciences') & (original_1figr_dataset['Field'] == 'Economics & Business') & (original_1figr_dataset['Subfield'] == 'Industrial Relations'), 'Discipline'] = 'Economics & Business'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Economic & Social Sciences') & (original_1figr_dataset['Field'] == 'Economics & Business') & (original_1figr_dataset['Subfield'] == 'Logistics & Transportation'), 'Discipline'] = 'Economics & Business'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Economic & Social Sciences') & (original_1figr_dataset['Field'] == 'Economics & Business') & (original_1figr_dataset['Subfield'] == 'Marketing'), 'Discipline'] = 'Economics & Business'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Economic & Social Sciences') & (original_1figr_dataset['Field'] == 'Economics & Business') & (original_1figr_dataset['Subfield'] == 'Sport, Leisure & Tourism'), 'Discipline'] = 'Economics & Business'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Economic & Social Sciences') & (original_1figr_dataset['Field'] == 'Social Sciences') & (original_1figr_dataset['Subfield'] == 'Criminology'), 'Discipline'] = 'Social Sciences'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Economic & Social Sciences') & (original_1figr_dataset['Field'] == 'Social Sciences') & (original_1figr_dataset['Subfield'] == 'Cultural Studies'), 'Discipline'] = 'Social Sciences'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Economic & Social Sciences') & (original_1figr_dataset['Field'] == 'Social Sciences') & (original_1figr_dataset['Subfield'] == 'Demography'), 'Discipline'] = 'Social Sciences'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Economic & Social Sciences') & (original_1figr_dataset['Field'] == 'Social Sciences') & (original_1figr_dataset['Subfield'] == 'Education'), 'Discipline'] = 'Education'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Economic & Social Sciences') & (original_1figr_dataset['Field'] == 'Social Sciences') & (original_1figr_dataset['Subfield'] == 'Family Studies'), 'Discipline'] = 'Social Sciences'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Economic & Social Sciences') & (original_1figr_dataset['Field'] == 'Social Sciences') & (original_1figr_dataset['Subfield'] == 'Gender Studies'), 'Discipline'] = 'Social Sciences'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Economic & Social Sciences') & (original_1figr_dataset['Field'] == 'Social Sciences') & (original_1figr_dataset['Subfield'] == 'Geography'), 'Discipline'] = 'Social Sciences'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Economic & Social Sciences') & (original_1figr_dataset['Field'] == 'Social Sciences') & (original_1figr_dataset['Subfield'] == 'Information & Library Sciences'), 'Discipline'] = 'Social Sciences'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Economic & Social Sciences') & (original_1figr_dataset['Field'] == 'Social Sciences') & (original_1figr_dataset['Subfield'] == 'International Relations'), 'Discipline'] = 'Social Sciences'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Economic & Social Sciences') & (original_1figr_dataset['Field'] == 'Social Sciences') & (original_1figr_dataset['Subfield'] == 'Law'), 'Discipline'] = 'Law'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Economic & Social Sciences') & (original_1figr_dataset['Field'] == 'Social Sciences') & (original_1figr_dataset['Subfield'] == 'Political Science & Public Administration'), 'Discipline'] = 'Social Sciences'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Economic & Social Sciences') & (original_1figr_dataset['Field'] == 'Social Sciences') & (original_1figr_dataset['Subfield'] == 'Science Studies'), 'Discipline'] = 'Social Sciences'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Economic & Social Sciences') & (original_1figr_dataset['Field'] == 'Social Sciences') & (original_1figr_dataset['Subfield'] == 'Social Sciences Methods'), 'Discipline'] = 'Social Sciences'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Economic & Social Sciences') & (original_1figr_dataset['Field'] == 'Social Sciences') & (original_1figr_dataset['Subfield'] == 'Social Work'), 'Discipline'] = 'Social Sciences'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Economic & Social Sciences') & (original_1figr_dataset['Field'] == 'Social Sciences') & (original_1figr_dataset['Subfield'] == 'Sociology'), 'Discipline'] = 'Social Sciences'

    #General Domain
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'General') & (original_1figr_dataset['Field'] == 'General Arts, Humanities & Social Sciences') & (original_1figr_dataset['Subfield'] == 'General Arts, Humanities & Social Sciences'), 'Discipline'] = 'General Arts, Humanities & Social Sciences'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'General') & (original_1figr_dataset['Field'] == 'General Science & Technology') & (original_1figr_dataset['Subfield'] == 'General Science & Technology'), 'Discipline'] = 'General Science & Technology'

    #Health Sciences Domain
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Health Sciences') & (original_1figr_dataset['Field'] == 'Biomedical Research') & (original_1figr_dataset['Subfield'] == 'Anatomy & Morphology'), 'Discipline'] = 'Biomedical Research'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Health Sciences') & (original_1figr_dataset['Field'] == 'Biomedical Research') & (original_1figr_dataset['Subfield'] == 'Biochemistry & Molecular Biology'), 'Discipline'] = 'Biomedical Research'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Health Sciences') & (original_1figr_dataset['Field'] == 'Biomedical Research') & (original_1figr_dataset['Subfield'] == 'Biophysics'), 'Discipline'] = 'Biomedical Research'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Health Sciences') & (original_1figr_dataset['Field'] == 'Biomedical Research') & (original_1figr_dataset['Subfield'] == 'Developmental Biology'), 'Discipline'] = 'Biomedical Research'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Health Sciences') & (original_1figr_dataset['Field'] == 'Biomedical Research') & (original_1figr_dataset['Subfield'] == 'Genetics & Heredity'), 'Discipline'] = 'Biomedical Research'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Health Sciences') & (original_1figr_dataset['Field'] == 'Biomedical Research') & (original_1figr_dataset['Subfield'] == 'Microbiology'), 'Discipline'] = 'Biomedical Research'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Health Sciences') & (original_1figr_dataset['Field'] == 'Biomedical Research') & (original_1figr_dataset['Subfield'] == 'Microscopy'), 'Discipline'] = 'Biomedical Research'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Health Sciences') & (original_1figr_dataset['Field'] == 'Biomedical Research') & (original_1figr_dataset['Subfield'] == 'Mycology & Parasitology'), 'Discipline'] = 'Biomedical Research'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Health Sciences') & (original_1figr_dataset['Field'] == 'Biomedical Research') & (original_1figr_dataset['Subfield'] == 'Nutrition & Dietetics'), 'Discipline'] = 'Biomedical Research'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Health Sciences') & (original_1figr_dataset['Field'] == 'Biomedical Research') & (original_1figr_dataset['Subfield'] == 'Physiology'), 'Discipline'] = 'Biomedical Research'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Health Sciences') & (original_1figr_dataset['Field'] == 'Biomedical Research') & (original_1figr_dataset['Subfield'] == 'Toxicology'), 'Discipline'] = 'Biomedical Research'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Health Sciences') & (original_1figr_dataset['Field'] == 'Biomedical Research') & (original_1figr_dataset['Subfield'] == 'Virology'), 'Discipline'] = 'Biomedical Research'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Health Sciences') & (original_1figr_dataset['Field'] == 'Clinical Medicine') & (original_1figr_dataset['Subfield'] == 'Allergy'), 'Discipline'] = 'Health Sciences'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Health Sciences') & (original_1figr_dataset['Field'] == 'Clinical Medicine') & (original_1figr_dataset['Subfield'] == 'Anesthesiology'), 'Discipline'] = 'Health Sciences'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Health Sciences') & (original_1figr_dataset['Field'] == 'Clinical Medicine') & (original_1figr_dataset['Subfield'] == 'Arthritis & Rheumatology'), 'Discipline'] = 'Health Sciences'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Health Sciences') & (original_1figr_dataset['Field'] == 'Clinical Medicine') & (original_1figr_dataset['Subfield'] == 'Cardiovascular System & Hematology'), 'Discipline'] = 'Health Sciences'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Health Sciences') & (original_1figr_dataset['Field'] == 'Clinical Medicine') & (original_1figr_dataset['Subfield'] == 'Complementary & Alternative Medicine'), 'Discipline'] = 'Health Sciences'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Health Sciences') & (original_1figr_dataset['Field'] == 'Clinical Medicine') & (original_1figr_dataset['Subfield'] == 'Dentistry'), 'Discipline'] = 'Health Sciences'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Health Sciences') & (original_1figr_dataset['Field'] == 'Clinical Medicine') & (original_1figr_dataset['Subfield'] == 'Dermatology & Venereal Diseases'), 'Discipline'] = 'Health Sciences'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Health Sciences') & (original_1figr_dataset['Field'] == 'Clinical Medicine') & (original_1figr_dataset['Subfield'] == 'Emergency & Critical Care Medicine'), 'Discipline'] = 'Health Sciences'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Health Sciences') & (original_1figr_dataset['Field'] == 'Clinical Medicine') & (original_1figr_dataset['Subfield'] == 'Endocrinology & Metabolism'), 'Discipline'] = 'Health Sciences'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Health Sciences') & (original_1figr_dataset['Field'] == 'Clinical Medicine') & (original_1figr_dataset['Subfield'] == 'Environmental & Occupational Health'), 'Discipline'] = 'Health Sciences'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Health Sciences') & (original_1figr_dataset['Field'] == 'Clinical Medicine') & (original_1figr_dataset['Subfield'] == 'Gastroenterology & Hepatology'), 'Discipline'] = 'Health Sciences'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Health Sciences') & (original_1figr_dataset['Field'] == 'Clinical Medicine') & (original_1figr_dataset['Subfield'] == 'General & Internal Medicine'), 'Discipline'] = 'Health Sciences'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Health Sciences') & (original_1figr_dataset['Field'] == 'Clinical Medicine') & (original_1figr_dataset['Subfield'] == 'General Clinical Medicine'), 'Discipline'] = 'Health Sciences'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Health Sciences') & (original_1figr_dataset['Field'] == 'Clinical Medicine') & (original_1figr_dataset['Subfield'] == 'Geriatrics'), 'Discipline'] = 'Health Sciences'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Health Sciences') & (original_1figr_dataset['Field'] == 'Clinical Medicine') & (original_1figr_dataset['Subfield'] == 'Immunology'), 'Discipline'] = 'Health Sciences'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Health Sciences') & (original_1figr_dataset['Field'] == 'Clinical Medicine') & (original_1figr_dataset['Subfield'] == 'Legal & Forensic Medicine'), 'Discipline'] = 'Health Sciences'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Health Sciences') & (original_1figr_dataset['Field'] == 'Clinical Medicine') & (original_1figr_dataset['Subfield'] == 'Neurology & Neurosurgery'), 'Discipline'] = 'Health Sciences'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Health Sciences') & (original_1figr_dataset['Field'] == 'Clinical Medicine') & (original_1figr_dataset['Subfield'] == 'Nuclear Medicine & Medical Imaging'), 'Discipline'] = 'Health Sciences'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Health Sciences') & (original_1figr_dataset['Field'] == 'Clinical Medicine') & (original_1figr_dataset['Subfield'] == 'Obstetrics & Reproductive Medicine'), 'Discipline'] = 'Health Sciences'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Health Sciences') & (original_1figr_dataset['Field'] == 'Clinical Medicine') & (original_1figr_dataset['Subfield'] == 'Oncology & Carcinogenesis'), 'Discipline'] = 'Health Sciences'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Health Sciences') & (original_1figr_dataset['Field'] == 'Clinical Medicine') & (original_1figr_dataset['Subfield'] == 'Ophthalmology & Optometry'), 'Discipline'] = 'Health Sciences'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Health Sciences') & (original_1figr_dataset['Field'] == 'Clinical Medicine') & (original_1figr_dataset['Subfield'] == 'Orthopedics'), 'Discipline'] = 'Health Sciences'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Health Sciences') & (original_1figr_dataset['Field'] == 'Clinical Medicine') & (original_1figr_dataset['Subfield'] == 'Otorhinolaryngology'), 'Discipline'] = 'Health Sciences'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Health Sciences') & (original_1figr_dataset['Field'] == 'Clinical Medicine') & (original_1figr_dataset['Subfield'] == 'Pathology'), 'Discipline'] = 'Health Sciences'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Health Sciences') & (original_1figr_dataset['Field'] == 'Clinical Medicine') & (original_1figr_dataset['Subfield'] == 'Pediatrics'), 'Discipline'] = 'Health Sciences'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Health Sciences') & (original_1figr_dataset['Field'] == 'Clinical Medicine') & (original_1figr_dataset['Subfield'] == 'Pharmacology & Pharmacy'), 'Discipline'] = 'Health Sciences'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Health Sciences') & (original_1figr_dataset['Field'] == 'Clinical Medicine') & (original_1figr_dataset['Subfield'] == 'Psychiatry'), 'Discipline'] = 'Health Sciences'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Health Sciences') & (original_1figr_dataset['Field'] == 'Clinical Medicine') & (original_1figr_dataset['Subfield'] == 'Respiratory System'), 'Discipline'] = 'Health Sciences'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Health Sciences') & (original_1figr_dataset['Field'] == 'Clinical Medicine') & (original_1figr_dataset['Subfield'] == 'Sport Sciences'), 'Discipline'] = 'Education'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Health Sciences') & (original_1figr_dataset['Field'] == 'Clinical Medicine') & (original_1figr_dataset['Subfield'] == 'Surgery'), 'Discipline'] = 'Health Sciences'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Health Sciences') & (original_1figr_dataset['Field'] == 'Clinical Medicine') & (original_1figr_dataset['Subfield'] == 'Tropical Medicine'), 'Discipline'] = 'Health Sciences'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Health Sciences') & (original_1figr_dataset['Field'] == 'Clinical Medicine') & (original_1figr_dataset['Subfield'] == 'Urology & Nephrology'), 'Discipline'] = 'Health Sciences'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Health Sciences') & (original_1figr_dataset['Field'] == 'Psychology & Cognitive Sciences') & (original_1figr_dataset['Subfield'] == 'Behavioral Science & Comparative Psychology'), 'Discipline'] = 'Psychology & Cognitive Sciences'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Health Sciences') & (original_1figr_dataset['Field'] == 'Psychology & Cognitive Sciences') & (original_1figr_dataset['Subfield'] == 'Clinical Psychology'), 'Discipline'] = 'Psychology & Cognitive Sciences'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Health Sciences') & (original_1figr_dataset['Field'] == 'Psychology & Cognitive Sciences') & (original_1figr_dataset['Subfield'] == 'Developmental & Child Psychology'), 'Discipline'] = 'Psychology & Cognitive Sciences'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Health Sciences') & (original_1figr_dataset['Field'] == 'Psychology & Cognitive Sciences') & (original_1figr_dataset['Subfield'] == 'Experimental Psychology'), 'Discipline'] = 'Psychology & Cognitive Sciences'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Health Sciences') & (original_1figr_dataset['Field'] == 'Psychology & Cognitive Sciences') & (original_1figr_dataset['Subfield'] == 'General Psychology & Cognitive Sciences'), 'Discipline'] = 'Psychology & Cognitive Sciences'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Health Sciences') & (original_1figr_dataset['Field'] == 'Psychology & Cognitive Sciences') & (original_1figr_dataset['Subfield'] == 'Human Factors'), 'Discipline'] = 'Psychology & Cognitive Sciences'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Health Sciences') & (original_1figr_dataset['Field'] == 'Psychology & Cognitive Sciences') & (original_1figr_dataset['Subfield'] == 'Psychoanalysis'), 'Discipline'] = 'Psychology & Cognitive Sciences'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Health Sciences') & (original_1figr_dataset['Field'] == 'Psychology & Cognitive Sciences') & (original_1figr_dataset['Subfield'] == 'Social Psychology'), 'Discipline'] = 'Psychology & Cognitive Sciences'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Health Sciences') & (original_1figr_dataset['Field'] == 'Public Health & Health Services') & (original_1figr_dataset['Subfield'] == 'Epidemiology'), 'Discipline'] = 'Health Sciences'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Health Sciences') & (original_1figr_dataset['Field'] == 'Public Health & Health Services') & (original_1figr_dataset['Subfield'] == 'Gerontology'), 'Discipline'] = 'Health Sciences'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Health Sciences') & (original_1figr_dataset['Field'] == 'Public Health & Health Services') & (original_1figr_dataset['Subfield'] == 'Health Policy & Services'), 'Discipline'] = 'Health Sciences'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Health Sciences') & (original_1figr_dataset['Field'] == 'Public Health & Health Services') & (original_1figr_dataset['Subfield'] == 'Nursing'), 'Discipline'] = 'Health Sciences'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Health Sciences') & (original_1figr_dataset['Field'] == 'Public Health & Health Services') & (original_1figr_dataset['Subfield'] == 'Public Health'), 'Discipline'] = 'Health Sciences'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Health Sciences') & (original_1figr_dataset['Field'] == 'Public Health & Health Services') & (original_1figr_dataset['Subfield'] == 'Rehabilitation'), 'Discipline'] = 'Health Sciences'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Health Sciences') & (original_1figr_dataset['Field'] == 'Public Health & Health Services') & (original_1figr_dataset['Subfield'] == 'Speech-Language Pathology & Audiology'), 'Discipline'] = 'Education'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Health Sciences') & (original_1figr_dataset['Field'] == 'Public Health & Health Services') & (original_1figr_dataset['Subfield'] == 'Substance Abuse'), 'Discipline'] = 'Health Sciences'

    #Natural Sciences Domain
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Natural Sciences') & (original_1figr_dataset['Field'] == 'Biology') & (original_1figr_dataset['Subfield'] == 'Ecology'), 'Discipline'] = 'Biology'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Natural Sciences') & (original_1figr_dataset['Field'] == 'Biology') & (original_1figr_dataset['Subfield'] == 'Entomology'), 'Discipline'] = 'Biology'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Natural Sciences') & (original_1figr_dataset['Field'] == 'Biology') & (original_1figr_dataset['Subfield'] == 'Evolutionary Biology'), 'Discipline'] = 'Biology'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Natural Sciences') & (original_1figr_dataset['Field'] == 'Biology') & (original_1figr_dataset['Subfield'] == 'Marine Biology & Hydrobiology'), 'Discipline'] = 'Biology'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Natural Sciences') & (original_1figr_dataset['Field'] == 'Biology') & (original_1figr_dataset['Subfield'] == 'Ornithology'), 'Discipline'] = 'Biology'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Natural Sciences') & (original_1figr_dataset['Field'] == 'Biology') & (original_1figr_dataset['Subfield'] == 'Plant Biology & Botany'), 'Discipline'] = 'Biology'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Natural Sciences') & (original_1figr_dataset['Field'] == 'Biology') & (original_1figr_dataset['Subfield'] == 'Zoology'), 'Discipline'] = 'Biology'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Natural Sciences') & (original_1figr_dataset['Field'] == 'Chemistry') & (original_1figr_dataset['Subfield'] == 'Analytical Chemistry'), 'Discipline'] = 'Chemistry'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Natural Sciences') & (original_1figr_dataset['Field'] == 'Chemistry') & (original_1figr_dataset['Subfield'] == 'General Chemistry'), 'Discipline'] = 'Chemistry'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Natural Sciences') & (original_1figr_dataset['Field'] == 'Chemistry') & (original_1figr_dataset['Subfield'] == 'Inorganic & Nuclear Chemistry'), 'Discipline'] = 'Chemistry'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Natural Sciences') & (original_1figr_dataset['Field'] == 'Chemistry') & (original_1figr_dataset['Subfield'] == 'Medicinal & Biomolecular Chemistry'), 'Discipline'] = 'Chemistry'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Natural Sciences') & (original_1figr_dataset['Field'] == 'Chemistry') & (original_1figr_dataset['Subfield'] == 'Organic Chemistry'), 'Discipline'] = 'Chemistry'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Natural Sciences') & (original_1figr_dataset['Field'] == 'Chemistry') & (original_1figr_dataset['Subfield'] == 'Physical Chemistry'), 'Discipline'] = 'Chemistry'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Natural Sciences') & (original_1figr_dataset['Field'] == 'Chemistry') & (original_1figr_dataset['Subfield'] == 'Polymers'), 'Discipline'] = 'Chemistry'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Natural Sciences') & (original_1figr_dataset['Field'] == 'Earth & Environmental Sciences') & (original_1figr_dataset['Subfield'] == 'Environmental Sciences'), 'Discipline'] = 'Earth & Environmental Sciences'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Natural Sciences') & (original_1figr_dataset['Field'] == 'Earth & Environmental Sciences') & (original_1figr_dataset['Subfield'] == 'Geochemistry & Geophysics'), 'Discipline'] = 'Earth & Environmental Sciences'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Natural Sciences') & (original_1figr_dataset['Field'] == 'Earth & Environmental Sciences') & (original_1figr_dataset['Subfield'] == 'Geology'), 'Discipline'] = 'Earth & Environmental Sciences'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Natural Sciences') & (original_1figr_dataset['Field'] == 'Earth & Environmental Sciences') & (original_1figr_dataset['Subfield'] == 'Meteorology & Atmospheric Sciences'), 'Discipline'] = 'Earth & Environmental Sciences'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Natural Sciences') & (original_1figr_dataset['Field'] == 'Earth & Environmental Sciences') & (original_1figr_dataset['Subfield'] == 'Oceanography'), 'Discipline'] = 'Earth & Environmental Sciences'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Natural Sciences') & (original_1figr_dataset['Field'] == 'Earth & Environmental Sciences') & (original_1figr_dataset['Subfield'] == 'Paleontology'), 'Discipline'] = 'Earth & Environmental Sciences'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Natural Sciences') & (original_1figr_dataset['Field'] == 'Mathematics & Statistics') & (original_1figr_dataset['Subfield'] == 'Applied Mathematics'), 'Discipline'] = 'Mathematics & Statistics'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Natural Sciences') & (original_1figr_dataset['Field'] == 'Mathematics & Statistics') & (original_1figr_dataset['Subfield'] == 'General Mathematics'), 'Discipline'] = 'Mathematics & Statistics'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Natural Sciences') & (original_1figr_dataset['Field'] == 'Mathematics & Statistics') & (original_1figr_dataset['Subfield'] == 'Numerical & Computational Mathematics'), 'Discipline'] = 'Mathematics & Statistics'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Natural Sciences') & (original_1figr_dataset['Field'] == 'Mathematics & Statistics') & (original_1figr_dataset['Subfield'] == 'Statistics & Probability'), 'Discipline'] = 'Mathematics & Statistics'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Natural Sciences') & (original_1figr_dataset['Field'] == 'Physics & Astronomy') & (original_1figr_dataset['Subfield'] == 'Acoustics'), 'Discipline'] = 'Physics & Astronomy'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Natural Sciences') & (original_1figr_dataset['Field'] == 'Physics & Astronomy') & (original_1figr_dataset['Subfield'] == 'Applied Physics'), 'Discipline'] = 'Physics & Astronomy'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Natural Sciences') & (original_1figr_dataset['Field'] == 'Physics & Astronomy') & (original_1figr_dataset['Subfield'] == 'Astronomy & Astrophysics'), 'Discipline'] = 'Physics & Astronomy'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Natural Sciences') & (original_1figr_dataset['Field'] == 'Physics & Astronomy') & (original_1figr_dataset['Subfield'] == 'Chemical Physics'), 'Discipline'] = 'Physics & Astronomy'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Natural Sciences') & (original_1figr_dataset['Field'] == 'Physics & Astronomy') & (original_1figr_dataset['Subfield'] == 'Fluids & Plasmas'), 'Discipline'] = 'Physics & Astronomy'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Natural Sciences') & (original_1figr_dataset['Field'] == 'Physics & Astronomy') & (original_1figr_dataset['Subfield'] == 'General Physics'), 'Discipline'] = 'Physics & Astronomy'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Natural Sciences') & (original_1figr_dataset['Field'] == 'Physics & Astronomy') & (original_1figr_dataset['Subfield'] == 'Mathematical Physics'), 'Discipline'] = 'Physics & Astronomy'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Natural Sciences') & (original_1figr_dataset['Field'] == 'Physics & Astronomy') & (original_1figr_dataset['Subfield'] == 'Nuclear & Particle Physics'), 'Discipline'] = 'Physics & Astronomy'
    original_1figr_dataset.loc[(original_1figr_dataset['Domain'] == 'Natural Sciences') & (original_1figr_dataset['Field'] == 'Physics & Astronomy') & (original_1figr_dataset['Subfield'] == 'Optics'), 'Discipline'] = 'Physics & Astronomy'

#    print(original_1figr_dataset['Discipline'])




    #prints count of number of journals in each discipline
#    print(original_1figr_dataset['Discipline'].value_counts())  #23873 total
    
    return original_1figr_dataset


make_elsevier_unmatched_provider_with_disciplines(make_disciplines_column())
    