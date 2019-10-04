# Figure 7: Use of Elsevier by Domain
# mpc


# SETUP ----
# ----------------------------------------------
# Libraries, data, data prep

library(tidyverse)
library(scales)
library(readxl)
library(RColorBrewer)

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

