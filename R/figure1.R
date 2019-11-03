# Figure 1: Highly-Used Titles by Provider
# mpc


# SETUP ----
# ----------------------------------------------
# Libraries, data, data prep

library(tidyverse)
library(RColorBrewer)
library(scales)

journal <- readRDS("1science/journal.rds")

# USE MEASURES BY PROVIDER ----
# ----------------------------------------------

# Generate JR80, JR90, JR95 measures using jr1 (all 2017 downloads), jr5
# (current year 2017 downloads), references, publications


# Fig 1 functions ---------------------------------------------------------

# function to create highuse data frame for provider and provider2
# provider2 breaks Elsevier into Subscribed and Freedom

highuse_fn <- function(group_var){
  group_var <- enquo(group_var)
  
  journal %>% 
    select(journal, provider, provider2, type, jr1, jr5, cites, pubs, synth, scopus, domain, field, jid) %>% 
    filter(type == "Journal") %>% 
    mutate(provider = factor(provider),
           big5 = if_else(provider %in% c("Springer", "Elsevier", "Wiley", "Sage", "Taylor & Francis"), "Yes", "No"),
           els = if_else(provider == "Elsevier", "Yes", "No")) %>% 
    mutate(jr1 = as.integer(jr1), jr5 = as.integer(jr5)) %>% 
    group_by(!! group_var) %>% 
    arrange(!! group_var, desc(jr1)) %>% 
    mutate(cum_jr1 = cumsum(jr1),
           prov_jr1 = max(cum_jr1, na.rm=T),
           cum_jr1_per = (cum_jr1/prov_jr1)*100,
           use_jr1 = case_when(cum_jr1_per <= 80 ~ "JR80 Titles",
                               cum_jr1_per > 80 & cum_jr1_per <= 90 ~ "JR90 Titles",
                               cum_jr1_per > 90 & cum_jr1_per <= 95 ~ "JR95 Titles",
                               TRUE ~ "Remaining Titles")) %>% 
    arrange(!! group_var, desc(jr5)) %>%
    filter(!is.na(jr5)) %>%   ## stop the warnings about no non-missing arguments
    mutate(cum_jr5 = cumsum(jr5),
           prov_jr5 = max(cum_jr5, na.rm=T),
           cum_jr5_per = (cum_jr5/prov_jr5)*100,
           use_jr5 = case_when(cum_jr5_per <= 80 ~ "JR80 Titles",
                               cum_jr5_per > 80 & cum_jr5_per <= 90 ~ "JR90 Titles",
                               cum_jr5_per > 90 & cum_jr5_per <= 95 ~ "JR95 Titles",
                               TRUE ~ "Remaining Titles")) %>% 
    arrange(!! group_var, desc(cites)) %>% 
    mutate(cum_refs = cumsum(cites),
           prov_refs = max(cum_refs, na.rm=T),
           cum_refs_per = (cum_refs/prov_refs)*100,
           use_refs = case_when(cum_refs_per <= 80 ~ "JR80 Titles",
                                cum_refs_per > 80 & cum_refs_per <= 90 ~ "JR90 Titles",
                                cum_refs_per > 90 & cum_refs_per <= 95 ~ "JR95 Titles",
                                TRUE ~ "Remaining Titles")) %>% 
    arrange(!! group_var, desc(pubs)) %>% 
    mutate(cum_pubs = cumsum(pubs),
           prov_pubs = max(cum_pubs, na.rm=T),
           cum_pubs_per = (cum_pubs/prov_pubs)*100,
           use_pubs = case_when(cum_pubs_per <= 80 ~ "JR80 Titles",
                                cum_pubs_per > 80 & cum_pubs_per <= 90 ~ "JR90 Titles",
                                cum_pubs_per > 90 & cum_pubs_per <= 95 ~ "JR95 Titles",
                                TRUE ~ "Remaining Titles"))  
}

# Function to create figures

fig1 <- function(use, provider, title, subtitle){
  use <- enquo(use)
  provider <- enquo(provider)
  highuse_counts <- highuse %>%
    mutate(!! use := factor(!! use, levels = c("JR80 Titles", "JR90 Titles", "JR95 Titles", "Remaining Titles"))) %>% 
    filter(big5 == "Yes") %>% 
    count(!! provider, !! use) %>% 
    mutate(pct=n/sum(n), ypos = cumsum(pct))
  
  highuse_counts %>% 
    ggplot(aes(x = !! provider, y = pct, fill = fct_rev(!! use))) +
    geom_col() +
    scale_y_continuous(labels = scales::percent) +
    scale_fill_brewer(type = 'seq', palette = 'BuPu') +
    labs(title = title,
         subtitle = subtitle,
         x = "", y = "Percent") +
    geom_text(aes(label=paste0(n), y=ypos - 0.05)) +
    guides(fill = guide_legend(reverse=TRUE, title = NULL)) +
    theme(legend.position = "bottom") +
    coord_flip()
}


# Plots -------------------------------------------------------------------

# Big 5

highuse <- highuse_fn(group_var = provider)
fig1(use_jr1, 
     provider,
     title = "Percentage of Titles in High Use Journals",
     subtitle = "By All Downloads in 2017 (JR1)")
fig1(use_jr5, 
     provider,
     title = "Percentage of Titles in High Use Journals",
     subtitle = "By Current Year Downloads in 2017 (JR5)")
fig1(use_refs, 
     provider,
     title = "Percentage of Titles in High Use Journals",
     subtitle = "By References by UVA Authors")
fig1(use_pubs, 
     provider,
     title = "Percentage of Titles in High Use Journals",
     subtitle = "By UVA Authored Papers")

# Big 5 with Elsevier broken down by Subscribed and Freedom
highuse <- highuse_fn(group_var = provider2)
fig1(use_jr1, 
     provider2,
     title = "Percentage of Titles in High Use Journals",
     subtitle = "By All Downloads in 2017 (JR1)")
fig1(use_jr5, 
     provider2,
     title = "Percentage of Titles in High Use Journals",
     subtitle = "By Current Year Downloads in 2017 (JR5)")
fig1(use_refs, 
     provider2,
     title = "Percentage of Titles in High Use Journals",
     subtitle = "By References by UVA Authors")
fig1(use_pubs, 
     provider2,
     title = "Percentage of Titles in High Use Journals",
     subtitle = "By UVA Authored Papers")


