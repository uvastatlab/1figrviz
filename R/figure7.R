# Figure 7: Use of Elsevier by Domain
# mpc


# SETUP ----
# ----------------------------------------------
# Libraries, data, data prep

library(tidyverse)
library(RColorBrewer)
library(scales)
library(gridExtra)

journal <- readRDS("1science/journal.rds")


# USE OF ELSEVIER BY DOMAIN ----
# ----------------------------------------------
# keep only elsevier
els <- journal %>% 
  select(journal, provider, type, jr1, jr5, cites, pubs, synth, scopus, domain, field, jid) %>% 
  filter(type == "Journal" & provider == "Elsevier") %>% 
  mutate(jr1 = as.integer(jr1), jr5 = as.integer(jr5))

# group/summarize by domain
els_group <- els %>% 
  group_by(domain) %>% 
  summarize(titles = n(),
            titlesjr1 = sum(!is.na(jr1)),
            titlesjr5 = sum(!is.na(jr5)),
            jr1 = sum(jr1, na.rm = TRUE),
            jr5 = sum(jr5, na.rm = TRUE),
            refs = sum(cites, na.rm = TRUE),
            pubs = sum(pubs, na.rm = TRUE)) %>% 
  mutate(domain = factor(domain))


# plot jr1 by domain
els_group %>% 
  mutate(domain = fct_reorder(domain, jr1)) %>% 
  ggplot(aes(x = domain, y = jr1, color = domain)) + 
  geom_segment(aes(x = domain, xend = domain, y = 0, yend = jr1), color = "grey", size = 1) +
  geom_point(size = 5) +
  scale_color_brewer(palette = "BuPu", direction = 1) +
  labs(title = "All 2017 Downloads from Elsevier Journals",
       subtitle = "By Article Domain",
       x = "", y = "Number of Downloads") +
  geom_text(aes(label = comma(jr1)), nudge_x = -.25, color = "black", size = 3) +
  theme(legend.position = "none") +
  coord_flip() 

# plot jr5 by domain
els_group %>% 
  mutate(domain = fct_reorder(domain, jr5)) %>% 
  ggplot(aes(x = domain, y = jr5, color = domain)) + 
  geom_segment(aes(x = domain, xend = domain, y = 0, yend = jr5), color = "grey", size = 1) +
  geom_point(size = 5) +
  scale_color_brewer(palette = "BuPu", direction = 1) +
  labs(title = "Current Year 2017 Downloads from Elsevier Journals",
       subtitle = "By Article Domain",
       x = "", y = "Number of Downloads") +
  geom_text(aes(label = comma(jr5)), nudge_x = -.25, color = "black", size = 3) +
  theme(legend.position = "none") +
  coord_flip() 

# plot refs by domain
els_group %>% 
  mutate(domain = fct_reorder(domain, refs)) %>% 
  ggplot(aes(x = domain, y = refs, color = domain)) + 
  geom_segment(aes(x = domain, xend = domain, y = 0, yend = refs), color = "grey", size = 1) +
  geom_point(size = 5) +
  scale_color_brewer(palette = "BuPu", direction = 1) +
  labs(title = "UVA References by in Elsevier Journals",
       subtitle = "By Article Domain",
       x = "", y = "Number of Downloads") +
  geom_text(aes(label = comma(refs)), nudge_x = -.25, color = "black", size = 3) +
  theme(legend.position = "none") +
  coord_flip() 

# plot pubs by domain
els_group %>% 
  mutate(domain = fct_reorder(domain, pubs)) %>% 
  ggplot(aes(x = domain, y = pubs, color = domain)) + 
  geom_segment(aes(x = domain, xend = domain, y = 0, yend = pubs), color = "grey", size = 1) +
  geom_point(size = 5) +
  scale_color_brewer(palette = "BuPu", direction = 1) +
  labs(title = "UVA-Authored Publications in Elsevier Journals",
       subtitle = "By Article Domain",
       x = "", y = "Number of Downloads") +
  geom_text(aes(label = comma(pubs)), nudge_x = -.25, color = "black", size = 3) +
  theme(legend.position = "none") +
  coord_flip() 

# Percents
els_total <- els_group %>% 
  mutate(refs = as.integer(refs),
         pubs = as.integer(pubs)) %>% 
  summarize_if(is.integer, sum)

percents <- els_group$jr1/els_total$jr1
percents[5]

