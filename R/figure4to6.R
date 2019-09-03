# Figure 4: UVA References over time and as Percent in Big 5
# Figure 5: UVA Publications over time and as Percent in Big 5
# Figure 6: OA-Available Publications over time and as Percent in Big 5
# mpc


# SETUP ----
# ----------------------------------------------
# Libraries, data, data prep

library(tidyverse)
library(scales)
library(readxl)
library(RColorBrewer)
library(gridExtra)

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

# keep only package data for big 5
big5 <- journal %>% 
  select(provider, type, pub2008:jr12018) %>% 
  filter(type == "Package" & provider %in% c("Springer", "Elsevier", "Wiley", "Sage", "Taylor & Francis"))

# function to grab legend to use in common
get_legend<-function(myggplot){
  tmp <- ggplot_gtable(ggplot_build(myggplot))
  leg <- which(sapply(tmp$grobs, function(x) x$name) == "guide-box")
  legend <- tmp$grobs[[leg]]
  return(legend)
}


# UVA REFERENCES OVER TIME ----
# ----------------------------------------------
# 4. Number of uva citations in Big 5 as percent of citations over time
# reshape time data to long format: pub2008-pub2017, tot2008-tot2017
big5ref <- big5 %>% 
  select(provider, cite2008:cite2017) %>% 
  pivot_longer(-provider, 
               names_to = c(".value", "year"),
               names_sep = -4)

# create total citations
totalref <- journal %>% 
  filter(type == "Package") %>% 
  mutate(tot2008 = sum(cite2008), tot2009 = sum(cite2009),
         tot2010 = sum(cite2010), tot2011 = sum(cite2011),
         tot2012 = sum(cite2012), tot2013 = sum(cite2013),
         tot2014 = sum(cite2014), tot2015 = sum(cite2015),
         tot2016 = sum(cite2016), tot2017 = sum(cite2017)) %>% 
  filter(provider == "Elsevier") %>% 
  select(tot2008:tot2017) %>% 
  pivot_longer(tot2008:tot2017, 
               names_to = c(".value", "year"),
               names_sep = -4)

# join totalref and create uva percent and indicator for Elsevier
big5ref <- full_join(big5ref, totalref, by = "year") %>% 
  mutate(uvaper = (cite/tot)*100,
         els = if_else(provider == "Elsevier", "Yes", "No"))

# plot uva percent
p1 <- ggplot(totalref, aes(x = year, y = tot, group = 1)) + 
  geom_line() +
  labs(title = "References by UVA Authors",
       subtitle = "Across All Providers",
       x = "Year", y = "Number of References")

p2 <- ggplot(big5ref, aes(x = year, y = cite, group = provider)) +
  geom_line(aes(color = provider)) +
  scale_color_brewer(type = "qual", palette = "Set1") +
  labs(title = "References by UVA Authors",
       subtitle = "In Big 5 Providers",
       x = "Year", y = "Number of References", color = "Provider")

p3 <- ggplot(big5ref, aes(x = year, y = uvaper, group = provider)) +
  geom_line(aes(color = provider)) +
  scale_color_brewer(type = "qual", palette = "Set1") +
  labs(title = "Percent of All References by UVA Authors",
       subtitle = "In Big 5 Providers",
       x = "Year", y = "Percent of References", color = "Provider")

# use the get_legend function
legend <- get_legend(p2)
p1 <- p1 + theme(legend.position="none")
p2 <- p2 + theme(legend.position="none")
p3 <- p3 + theme(legend.position="none")

grid.arrange(p1, p2, p3, legend, ncol = 2)


# UVA PUBLICATIONS OVER TIME ----
# ----------------------------------------------
# 5. Number of uva-authored publications and percent of uva-authored publications in Big 5 over time
# reshape time data to long format: pub2008-pub2017, scopus2008-scopus2017
big5pub <- big5 %>% 
  select(provider, pub2008:pub2017, scopus2008:scopus2017) %>% 
  pivot_longer(-provider, 
               names_to = c(".value", "year"),
               names_sep = -4)

# create uva percent and indicator for Elsevier
big5pub <- big5pub %>% 
  mutate(uvaper = (pub/scopus)*100,
         els = if_else(provider == "Elsevier", "Yes", "No"))

# plot uva percent
p1 <- ggplot(big5pub, aes(x = year, y = scopus, group = provider)) + 
  geom_line(aes(color = provider)) +
  scale_linetype_manual(values=c("longdash", "solid"), guide=F) +
  labs(title = "Total Number of Articles Published",
       subtitle = "In Big 5 Providers",
       x = "Year", y = "Number of Articles", color = "Provider")

p2 <- ggplot(big5pub, aes(x = year, y = pub, group = provider)) +
  geom_line(aes(color = provider)) +
  scale_color_brewer(type = "qual", palette = "Set1") +
  labs(title = "Number of Articles by UVA Authors",
       subtitle = "In Big 5 Providers",
       x = "Year", y = "Number of Articles", color = "Provider")

p3 <- ggplot(big5pub, aes(x = year, y = uvaper, group = provider)) +
  geom_line(aes(color = provider)) +
  scale_color_brewer(type = "qual", palette = "Set1") +
  labs(title = "Percent of All Articles by UVA Authors",
       subtitle = "In Big 5 Providers",
       x = "Year", y = "Percent of Articles", color = "Provider")

# use the get_legend function
legend <- get_legend(p1)
p1 <- p1 + theme(legend.position="none")
p2 <- p2 + theme(legend.position="none")
p3 <- p3 + theme(legend.position="none")

grid.arrange(p1, p2, p3, legend, ncol = 2)


# OA AVAILABLE PUBLICATIONS OVER TIME ----
# ----------------------------------------------
# 6. Number of oa-available publications and percent of oa-available publications in Big 5 over time
# reshape time data to long format: oa2008-ao2017, scopus2008-scopus2017
big5oa <- big5 %>% 
  select(provider, oa2008:oa2017, scopus2008:scopus2017) %>% 
  pivot_longer(-provider, 
               names_to = c(".value", "year"),
               names_sep = -4)

# create oa percent
big5oa <- big5oa %>% 
  mutate(oaper = (oa/scopus)*100,
         els = if_else(provider == "Elsevier", "Yes", "No"))

# plot
# plot uva percent
p1 <- ggplot(big5oa, aes(x = year, y = scopus, group = provider)) + 
  geom_line(aes(color = provider)) +
  scale_color_brewer(type = "qual", palette = "Set1") +
  labs(title = "Number of Articles Published",
       subtitle = "In Big 5 Providers",
       x = "Year", y = "Number of Articlest", color = "Provider")

p2 <- ggplot(big5oa, aes(x = year, y = oa, group = provider)) +
  geom_line(aes(color = provider)) +
  scale_color_brewer(type = "qual", palette = "Set1") +
  labs(title = "Number of OA-Available Articles",
       subtitle = "In Big 5 Providers",
       x = "Year", y = "Number of Articles", color = "Provider")

p3 <- ggplot(big5oa, aes(x = year, y = oaper, group = provider)) +
  geom_line(aes(color = provider)) +
  scale_color_brewer(type = "qual", palette = "Set1") +
  labs(title = "Percent of OA-Available Articles",
       subtitle = "In Big 5 Providers",
       x = "Year", y = "Percent of Articles", color = "Provider")

# use the function
legend <- get_legend(p1)
p1 <- p1 + theme(legend.position="none")
p2 <- p2 + theme(legend.position="none")
p3 <- p3 + theme(legend.position="none")

grid.arrange(p1, p2, p3, legend, ncol = 2)
