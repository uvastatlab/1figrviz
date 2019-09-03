# Figure 3: Cost per Downloads
# mpc


# SETUP ----
# ----------------------------------------------
# Libraries, data, data prep

library(tidyverse)
library(scales)
library(readxl)

# read in 1figr tab and supplemental cost data
journal <- read_excel("1science/1figr_U_Virginia_edit.xlsx", sheet = 4, skip = 8)
# read in supplemental cost data
cost <- read_excel("1science/1figr_U_Virginia_edit_Supp_Data.xlsx")

# rename variables in journal and cost
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

names(cost) <- c("provider", "type", "source", "cost", "subcost")
  
# COST PER DOWNLOAD ----
# ----------------------------------------------
journal_big5 <- journal %>% 
  filter(type == "Package" & provider %in% c("Springer", "Elsevier", "Wiley", "Sage", "Taylor & Francis")) %>% 
  mutate(els = if_else(provider == "Elsevier", "Yes", "No"),
         jr1 = as.integer(jr1),
         jr5 = as.integer(jr5)) %>% 
  select(journal, provider, jr1, jr5, els) %>% 
  left_join(cost, by = "provider") %>% 
  mutate(cpd_jr1 = cost/jr1,
         cpd_jr5 = cost/jr5)

# CPD-JR1 for Big 5
journal_big5 %>% 
  mutate(provider = factor(provider),
         provider = fct_reorder(provider, desc(cpd_jr1))) %>% 
  ggplot(aes(x = provider, y = cpd_jr1, color = els)) + 
  geom_segment(aes(x = provider, xend = provider, y = 0, yend = cpd_jr1), color = "grey", size = 1) +
  geom_point(size = 5) +
  scale_y_continuous(labels = scales::dollar) +
  scale_color_manual(values = c("orange", "blue")) +
  labs(title = "2017 Cost Per Download, All Downloads/JR1",
       subtitle = "(Package Cost / # JR1 Downloads)",
       x = "", y = "Dollars") +
  geom_text(aes(label = dollar(round(cpd_jr1, 2))), nudge_x = -.3, color = "black", size = 3) +
  theme(legend.position = "none") +
  coord_flip() 

# CPD-JR5 for Big 5
journal_big5 %>% 
  mutate(provider = factor(provider),
         provider = fct_reorder(provider, desc(cpd_jr5))) %>% 
  ggplot(aes(x = provider, y = cpd_jr5, color = els)) + 
  geom_segment(aes(x = provider, xend = provider, y = 0, yend = cpd_jr5), color = "grey", size = 1) +
  geom_point(size = 5) +
  scale_y_continuous(labels = scales::dollar) +
  scale_color_manual(values = c("orange", "blue")) +
  labs(title = "2017 Cost Per Download, Current Year Downloads/JR5",
       subtitle = "(Package Cost / # JR5 Downloads)",
       x = "", y = "Dollars") +
  geom_text(aes(label = dollar(round(cpd_jr5, 2))), nudge_x = -.3, color = "black", size = 3) +
  theme(legend.position = "none") +
  coord_flip() 

