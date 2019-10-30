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

