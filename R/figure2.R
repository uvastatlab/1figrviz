# Figure 2: Ratio of Current Year Use by Provider
# mpc


# SETUP ----
# ----------------------------------------------
# Libraries, data, data prep

library(tidyverse)
library(scales)
library(readxl)

# read in 1figr tab
journal <- read_excel("1science/1figr_U_Virginia_edit.xlsx", sheet = 4, skip = 8)


# rename variables in journal
names(journal) <- c("sort", "journal", "issn", "provider", "type", "fig1", "jr1", "jr5", "currentper",
                    "cites", "citeper", "pubs", "pubsper", "synth", "jtier", "subtier", "dupes",
                    "oa", "oaper", "fig2", "scopus", "arif", "domain", "field", "subfield", 
                    "pub2008", "pub2009", "pub2010", "pub2011", "pub2012", "pub2013", "pub2014",
                    "pub2015", "pub2016", "pub2017", "cite2008", "cite2009", "cite2010", "cite2011",
                    "cite2012", "cite2013", "cite2014", "cite2015", "cite2016", "cite2017", 
                    "oa2008", "oa2009", "oa2010", "oa2011", "oa2012", "oa2013", "oa2014", "oa2015", 
                    "oa2016", "oa2017", "oaper2008", "oaper2009", "oaper2010", "oaper2011", "oaper2012",
                    "oaper2013", "oaper2014", "oaper2015", "oaper2016", "oaper2017", "scopus2008",
                    "scopus2009", "scopus2010", "scopus2011", "scopus2012", "scopus2013", "scopus2014",
                    "scopus2015", "scopus2016", "scopus2017", "jr12015", "jr12016", "jr12017", "jr12018",
                    "jr12015_2018", "jid", "journalname")

# PROVIDER JR5/JR1 RATIO ----
# ----------------------------------------------
journal_jr5ratio <- journal %>% 
  select(journal, provider, type, jr1, jr5, cites, pubs, synth, scopus, domain, field, jid) %>% 
  filter(type == "Package" & provider != "Modern Language Association") %>% 
  mutate(jr1 = as.integer(jr1),
         jr5 = as.integer(jr5),
         jr5per = (jr5/jr1)*100,
         provider = factor(provider),
         provider = fct_reorder(provider, desc(jr5per)),
         big5 = if_else(provider %in% c("Springer", "Elsevier", "Wiley", "Sage", "Taylor & Francis"), "Yes", "No"),
         els = if_else(provider == "Elsevier", "Yes", "No")) 

# JR5 ratio for big 5
journal_jr5ratio %>% filter(big5 == "Yes") %>% 
  ggplot(aes(x = provider, y = jr5per, color = els)) + 
  geom_segment(aes(x = provider, xend = provider, y = 0, yend = jr5per), color = "grey", size = 1) +
  geom_point(size = 5) +
  scale_color_manual(values = c("orange", "blue")) +
  labs(title = "Percent of Articles Downloaded in 2017 from Current Year",
       subtitle = "By Provider",
       x = "", y = "Percent") +
  theme(legend.position = "none") +
  coord_flip() 

