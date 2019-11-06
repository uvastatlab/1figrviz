# Figure 3: Cost per Downloads
# mpc


# SETUP ----
# ----------------------------------------------
# Libraries, data, data prep
library(tidyverse)
library(RColorBrewer)
library(scales)
library(readxl)

journal <- readRDS("1science/journal.rds")

# read in supplemental cost data
cost <- read_excel("1science/1figr_U_Virginia_edit_Supp_Data.xlsx")
names(cost) <- c("provider", "type", "source", "cost", "subcost")


  
# COST PER DOWNLOAD ----
# ----------------------------------------------
journal_big5 <- journal %>% 
  filter(type == "Package" & provider %in% c("Springer", "Elsevier", "Wiley", "Sage", "Taylor & Francis")) %>% 
  mutate(els = if_else(provider == "Elsevier", "Yes", "No"),
         jr1 = as.integer(jr1),
         jr5 = as.integer(jr5)) %>% 
  select(provider, jr1, jr5, els) %>% 
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


# Need to derive package level numbers for Elsevier Freedom and Subscribed
tmp <- journal %>% 
  filter(provider == "Elsevier" & type == "Journal") %>% 
  group_by(provider2) %>% 
  summarise(jr1 = sum(as.integer(jr1), na.rm = T),
            jr5 = sum(as.integer(jr5), na.rm = T)) %>% 
  rename(provider = provider2) %>% 
  mutate(els = "Yes") %>% 
  left_join(cost, by = "provider") %>% 
  mutate(cpd_jr1 = cost/jr1,
         cpd_jr5 = cost/jr5)

# bind rows to journal_big5
journal_big6 <- journal_big5 %>% bind_rows(tmp) %>% 
  filter(provider != "Elsevier")


# CPD-JR1 for Big 6
journal_big6 %>% 
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

# CPD-JR5 for Big 6
journal_big6 %>% 
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

# Figure with just Els Free and Subscribed
journal_big6 %>% 
  mutate(provider = factor(provider),
         provider = fct_reorder(provider, desc(cpd_jr5))) %>% 
  filter(str_detect(provider, "Elsevier")) %>% 
  ggplot(aes(x = provider, y = cpd_jr5)) + 
  geom_segment(aes(x = provider, xend = provider, y = 0, yend = cpd_jr5), color = "grey", size = 1) +
  geom_point(size = 5, color = "blue") +
  scale_y_continuous(labels = scales::dollar) +
  scale_color_manual(values = c("orange", "blue")) +
  labs(title = "2017 Cost Per Download, Current Year Downloads/JR5",
       subtitle = "(Package Cost / # JR5 Downloads)",
       x = "", y = "Dollars") +
  geom_text(aes(label = dollar(round(cpd_jr5, 2))), nudge_x = -.3, color = "black", size = 3) +
  theme(legend.position = "none") +
  coord_flip() 

