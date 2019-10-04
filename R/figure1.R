# Figure 1: Highly-Used Titles by Provider
# mpc


# SETUP ----
# ----------------------------------------------
# Libraries, data, data prep

library(tidyverse)
library(RColorBrewer)
library(scales)
library(readxl)

# read in original unedited data
journal <- read_excel("1science/1figr_U_Virginia_Original.xlsx", 
                      sheet = 4, 
                      skip = 8)

# rename variables in journal
names(journal) <- c("sort", "journal", "issn", "provider", "type", "fig1", "jr1", "jr5", 
                         "cites", "pubs", "synth", "jtier", "subtier", "dupes",
                         "oa", "oaper", "fig2", "scopus", "arif", "domain", "field", "subfield", 
                         "pub2008", "pub2009", "pub2010", "pub2011", "pub2012", "pub2013", "pub2014",
                         "pub2015", "pub2016", "pub2017", "cite2008", "cite2009", "cite2010", "cite2011",
                         "cite2012", "cite2013", "cite2014", "cite2015", "cite2016", "cite2017", 
                         "oa2008", "oa2009", "oa2010", "oa2011", "oa2012", "oa2013", "oa2014", "oa2015", 
                         "oa2016", "oa2017", "oaper2008", "oaper2009", "oaper2010", "oaper2011", "oaper2012",
                         "oaper2013", "oaper2014", "oaper2015", "oaper2016", "oaper2017", "scopus2008",
                         "scopus2009", "scopus2010", "scopus2011", "scopus2012", "scopus2013", "scopus2014",
                         "scopus2015", "scopus2016", "scopus2017", "jr12015", "jr12016", "jr12017", "jr12018",
                         "jid", "journalname")


# derive Current Year Use Percentage - currentper
# derive % of papers referenced by UVA - citeper
# derive UVA Papers % of total - pubsper

journal <- journal %>% 
  mutate(jr5 = if_else(jr5 == "N/A", NA_character_, jr5),
         jr1 = if_else(jr1 == "N/A", NA_character_, jr1),
         currentper = as.numeric(jr5)/as.numeric(jr1),
         citeper = if_else(!is.finite(cites/scopus),0,cites/scopus),
         pubsper = if_else(!is.finite(pubs/scopus),0,pubs/scopus)) 

# derive Downloads JR1 2015-2018
journal <- journal %>% 
  mutate_if(str_detect(names(journal), pattern = "^jr120"), 
            ~as.numeric(if_else(. == "N/A", "0", .))) %>% 
  mutate(jr12015_2018 = jr12015 + jr12016 + jr12017 + jr12018) %>% 
  select(sort:jr5, currentper, cites, citeper, pubs, pubsper,
         synth:jr12018,jr12015_2018,jid, journalname)
  


# USE MEASURES BY PROVIDER ----
# ----------------------------------------------
# Generate JR80, JR90, JR95 measures using jr1 (all 2017 downloads), jr5 (current year 2017 downloads), references, publications
highuse <- journal %>% 
  select(journal, provider, type, jr1, jr5, cites, pubs, synth, scopus, domain, field, jid) %>% 
  filter(type == "Journal") %>% 
  mutate(provider = factor(provider),
         big5 = if_else(provider %in% c("Springer", "Elsevier", "Wiley", "Sage", "Taylor & Francis"), "Yes", "No"),
         els = if_else(provider == "Elsevier", "Yes", "No")) %>% 
  mutate(jr1 = as.integer(jr1), jr5 = as.integer(jr5)) %>% 
  group_by(provider) %>% 
  arrange(provider, desc(jr1)) %>% 
  mutate(cum_jr1 = cumsum(jr1),
         prov_jr1 = max(cum_jr1, na.rm=T),
         cum_jr1_per = (cum_jr1/prov_jr1)*100,
         use_jr1 = case_when(cum_jr1_per <= 80 ~ "JR80 Titles",
                             cum_jr1_per > 80 & cum_jr1_per <= 90 ~ "JR90 Titles",
                             cum_jr1_per > 90 & cum_jr1_per <= 95 ~ "JR95 Titles",
                             TRUE ~ "Remaining Titles")) %>% 
  arrange(provider, desc(jr5)) %>% 
  mutate(cum_jr5 = cumsum(jr5),
         prov_jr5 = max(cum_jr5, na.rm=T),
         cum_jr5_per = (cum_jr5/prov_jr5)*100,
         use_jr5 = case_when(cum_jr5_per <= 80 ~ "JR80 Titles",
                             cum_jr5_per > 80 & cum_jr5_per <= 90 ~ "JR90 Titles",
                             cum_jr5_per > 90 & cum_jr5_per <= 95 ~ "JR95 Titles",
                             TRUE ~ "Remaining Titles")) %>% 
  arrange(provider, desc(cites)) %>% 
  mutate(cum_refs = cumsum(cites),
         prov_refs = max(cum_refs, na.rm=T),
         cum_refs_per = (cum_refs/prov_refs)*100,
         use_refs = case_when(cum_refs_per <= 80 ~ "JR80 Titles",
                             cum_refs_per > 80 & cum_refs_per <= 90 ~ "JR90 Titles",
                             cum_refs_per > 90 & cum_refs_per <= 95 ~ "JR95 Titles",
                             TRUE ~ "Remaining Titles")) %>% 
  arrange(provider, desc(pubs)) %>% 
  mutate(cum_pubs = cumsum(pubs),
         prov_pubs = max(cum_pubs, na.rm=T),
         cum_pubs_per = (cum_pubs/prov_pubs)*100,
         use_pubs = case_when(cum_pubs_per <= 80 ~ "JR80 Titles",
                             cum_pubs_per > 80 & cum_pubs_per <= 90 ~ "JR90 Titles",
                             cum_pubs_per > 90 & cum_pubs_per <= 95 ~ "JR95 Titles",
                             TRUE ~ "Remaining Titles"))  
  

# plot use_jr1 for big 5
highuse_counts <- highuse %>%
  mutate(use_jr1 = factor(use_jr1, levels = c("JR80 Titles", "JR90 Titles", "JR95 Titles", "Remaining Titles"))) %>% 
  filter(big5 == "Yes") %>% count(provider, use_jr1) %>% 
  mutate(pct=n/sum(n), ypos = cumsum(pct))
  
highuse_counts %>% 
  ggplot(aes(x = provider, y = pct, fill = fct_rev(use_jr1))) +
  geom_col() +
  scale_y_continuous(labels = scales::percent) +
  scale_fill_brewer(type = 'seq', palette = 'BuPu') +
  labs(title = "Percentage of Titles in High Use Journals",
       subtitle = "By All Downloads in 2017 (JR1)",
       x = "", y = "Percent") +
  geom_text(aes(label=paste0(n), y=ypos - 0.05)) +
  guides(fill = guide_legend(reverse=TRUE, title = NULL)) +
  theme(legend.position = "bottom") +
  coord_flip()


# plot use_jr5 for big 5
highuse_counts <- highuse %>%
  mutate(use_jr5 = factor(use_jr5, levels = c("JR80 Titles", "JR90 Titles", "JR95 Titles", "Remaining Titles"))) %>% 
  filter(big5 == "Yes") %>% count(provider, use_jr5) %>% 
  mutate(pct=n/sum(n), ypos = cumsum(pct))

highuse_counts %>% 
  ggplot(aes(x = provider, y = pct, fill = fct_rev(use_jr5))) +
  geom_col() +
  scale_y_continuous(labels = scales::percent) +
  scale_fill_brewer(type = 'seq', palette = 'BuPu') +
  labs(title = "Percentage of Titles in High Use Journals",
       subtitle = "By Current Year Downloads in 2017 (JR5)",
       x = "", y = "Percent") +
  geom_text(aes(label=paste0(n), y=ypos - 0.05)) +
  guides(fill = guide_legend(reverse=TRUE, title = NULL)) +
  theme(legend.position = "bottom") +
  coord_flip()


# plot use_refs for big 5
highuse_counts <- highuse %>%
  mutate(use_refs = factor(use_refs, levels = c("JR80 Titles", "JR90 Titles", "JR95 Titles", "Remaining Titles"))) %>% 
  filter(big5 == "Yes") %>% count(provider, use_refs) %>% 
  mutate(pct=n/sum(n), ypos = cumsum(pct))

highuse_counts %>% 
  ggplot(aes(x = provider, y = pct, fill = fct_rev(use_refs))) +
  geom_col() +
  scale_y_continuous(labels = scales::percent) +
  scale_fill_brewer(type = 'seq', palette = 'BuPu') +
  labs(title = "Percentage of Titles in High Use Journals",
       subtitle = "By References by UVA Authors",
       x = "", y = "Percent") +
  geom_text(aes(label=paste0(n), y=ypos - 0.05)) +
  guides(fill = guide_legend(reverse=TRUE, title = NULL)) +
  theme(legend.position = "bottom") +
  coord_flip()


# plot use_pubs for big 5
highuse_counts <- highuse %>%
  mutate(use_pubs = factor(use_pubs, levels = c("JR80 Titles", "JR90 Titles", "JR95 Titles", "Remaining Titles"))) %>% 
  filter(big5 == "Yes") %>% count(provider, use_pubs) %>% 
  mutate(pct=n/sum(n), ypos = cumsum(pct))

highuse_counts %>% 
  ggplot(aes(x = provider, y = pct, fill = fct_rev(use_pubs))) +
  geom_col() +
  scale_y_continuous(labels = scales::percent) +
  scale_fill_brewer(type = 'seq', palette = 'BuPu') +
  labs(title = "Percentage of Titles in High Use Journals",
       subtitle = "By UVA Authored Papers",
       x = "", y = "Percent") +
  geom_text(aes(label=paste0(n), y=ypos - 0.05)) +
  guides(fill = guide_legend(reverse=TRUE, title = NULL)) +
  theme(legend.position = "bottom") +
  coord_flip()

