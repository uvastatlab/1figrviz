# Figure 2: Ratio of Current Year Use by Provider
# mpc


# SETUP ----
# ----------------------------------------------
# Libraries, data, data prep

library(tidyverse)
library(RColorBrewer)
library(scales)

journal <- readRDS("1science/journal.rds")

# PROVIDER JR5/JR1 RATIO ----
# ----------------------------------------------

journal_jr5ratio <- journal %>% 
  select(provider, type, jr1, jr5) %>% 
  filter(type == "Package" & provider != "Modern Language Association") %>% 
  mutate(jr1 = as.integer(jr1),
         jr5 = as.integer(jr5),
         jr5per = (jr5/jr1)*100,
         provider = factor(provider),
         provider = fct_reorder(provider, desc(jr5per)),
         big5 = if_else(provider %in% c("Springer", "Elsevier", "Wiley", "Sage", "Taylor & Francis"), "Yes", "No"),
         els = if_else(provider == "Elsevier", "Yes", "No")) 

# JR5 ratio for big 5
journal_jr5ratio %>% 
  filter(big5 == "Yes") %>% 
  ggplot(aes(x = provider, y = jr5per, color = els)) + 
  geom_segment(aes(x = provider, xend = provider, y = 0, yend = jr5per), color = "grey", size = 1) +
  geom_point(size = 5) +
  scale_color_manual(values = c("orange", "blue")) +
  labs(title = "Percent of Articles Downloaded in 2017 from Current Year",
       subtitle = "By Provider",
       x = "", y = "Percent") +
  theme(legend.position = "none") +
  coord_flip() 


# Need to derive package level numbers for Elsevier Freedom and Subscribed
tmp <- journal %>% 
  filter(provider == "Elsevier" & type == "Journal") %>% 
  group_by(provider2) %>% 
  summarise(jr1 = sum(as.integer(jr1), na.rm = T),
            jr5 = sum(as.integer(jr5), na.rm = T),
            jr5per = (jr5/jr1)*100) %>% 
  rename(provider = provider2) %>% 
  mutate(big5 = "Yes", els = "Yes", type = "Package") %>% 
  select(provider, type, everything()) 

# Plot
journal_jr5ratio %>% 
  filter(big5 == "Yes") %>% 
  mutate(provider = as.character(provider)) %>% 
  filter(provider != "Elsevier") %>% 
  bind_rows(tmp) %>% 
  mutate(provider = factor(provider),
         provider = fct_reorder(provider, desc(jr5per))) %>% 
  ggplot(aes(x = provider, y = jr5per, color = els)) + 
  geom_segment(aes(x = provider, xend = provider, y = 0, yend = jr5per), color = "grey", size = 1) +
  geom_point(size = 5) +
  scale_color_manual(values = c("orange", "blue")) +
  labs(title = "Percent of Articles Downloaded in 2017 from Current Year",
       subtitle = "By Provider",
       x = "", y = "Percent") +
  theme(legend.position = "none") +
  coord_flip() 

