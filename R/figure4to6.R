# Figure 4: UVA References over time and as Percent in Big 5
# Figure 5: UVA Publications over time and as Percent in Big 5
# Figure 6: OA-Available Publications over time and as Percent in Big 5
# mpc


# SETUP ----
# ----------------------------------------------
# Libraries, data, data prep

library(tidyverse)
library(RColorBrewer)
library(scales)
library(gridExtra)

journal <- readRDS("1science/journal.rds")

# keep only package data for big 5
big5 <- journal %>% 
  # select(provider, type, pub2008:jr12018) %>% 
  select(provider, type, pub2008:oa2017, scopus2008:scopus2017) %>% 
  filter(type == "Package" & provider %in% c("Springer", "Elsevier", "Wiley", "Sage", "Taylor & Francis")) %>% 
  select(-type)

# create a big 6 data frame (two Elseviers: Freedom and Subscribed)
els2 <- journal %>% 
  # select(provider, type, pub2008:jr12018) %>% 
  select(provider2, type, pub2008:oa2017, scopus2008:scopus2017) %>% 
  filter(type == "Journal" & provider2 %in% c("Elsevier Freedom", "Elsevier Subscribed")) %>% 
  group_by(provider2) %>% 
  summarise_if(is.double, sum, na.rm = TRUE) %>% 
  rename(provider = provider2)

big6 <- bind_rows(big5, els2) %>% 
  filter(provider != "Elsevier") %>% 
  mutate(elsevier = if_else(str_detect(provider, "Elsevier"), 1, 0)) %>% 
  select(provider, elsevier, everything())

rm(els2)


# function to grab legend to use in common
get_legend<-function(myggplot){
  tmp <- ggplot_gtable(ggplot_build(myggplot))
  leg <- which(sapply(tmp$grobs, function(x) x$name) == "guide-box")
  legend <- tmp$grobs[[leg]]
  return(legend)
}

# function to generate 3 plots + legend
plot_grid <- function(p1, p2, p3){
  legend <- get_legend(p2)
  p1 <- p1 + theme(legend.position="none")
  p2 <- p2 + theme(legend.position="none")
  p3 <- p3 + theme(legend.position="none")
  grid.arrange(p1, p2, p3, legend, ncol = 2)
}

# color palette with 2 reds for Elsevier Free and Sub
# #E41A1C - red for Elsevier
pal <- c("#E41A1C", brewer.pal(n = 5, name = "Set1"))




# 4. UVA REFERENCES OVER TIME  --------------------------------------------

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
  mutate(uvaper = (cite/tot)*100)


# plot uva percent
p1 <- ggplot(totalref, aes(x = year, y = tot, group = 1)) + 
  geom_line() +
  scale_y_continuous(labels = scales::comma) + 
  labs(title = "References by UVA Authors",
       subtitle = "Across All Providers",
       x = "Year", y = "Number of References")

p2 <- ggplot(big5ref, aes(x = year, y = cite, group = provider)) +
  geom_line(aes(color = provider)) +
  scale_color_brewer("Provider", type = "qual", palette = "Set1") +
  labs(title = "References by UVA Authors",
       subtitle = "In Big 5 Providers",
       x = "Year", y = "Number of References")

p3 <- ggplot(big5ref, aes(x = year, y = uvaper, group = provider)) +
  geom_line(aes(color = provider)) +
  scale_color_brewer("Provider", type = "qual", palette = "Set1") +
  labs(title = "Percent of All References by UVA Authors",
       subtitle = "In Big 5 Providers",
       x = "Year", y = "Percent of References")

# create plot
plot_grid(p1, p2, p3)

# Big 6 (Elsevier Free and Elsevier Subscribed)
big6ref <- big6 %>% 
  select(provider, cite2008:cite2017) %>% 
  pivot_longer(-provider, 
               names_to = c(".value", "year"),
               names_sep = -4) %>% 
  full_join(totalref, by = "year") %>% 
  mutate(uvaper = (cite/tot)*100,
         els = if_else(str_detect(provider,"Freedom"), "Yes", "No"))


# plot uva percent
p2 <- ggplot(big6ref, aes(x = year, y = cite, group = provider)) +
  geom_line(aes(color = provider, linetype = provider)) +
  scale_color_manual("Provider", values = pal) +
  scale_linetype_manual("Provider", values = c(2,1,1,1,1,1)) +
  labs(title = "References by UVA Authors",
       subtitle = "In Big 5 Providers",
       x = "Year", y = "Number of References")

p3 <- ggplot(big6ref, aes(x = year, y = uvaper, group = provider)) +
  geom_line(aes(color = provider, linetype = provider)) +
  scale_color_manual("Provider", values = pal) +
  scale_linetype_manual("Provider", values = c(2,1,1,1,1,1)) +
  labs(title = "Percent of All References by UVA Authors",
       subtitle = "In Big 5 Providers",
       x = "Year", y = "Percent of References")

# create plot
plot_grid(p1, p2, p3)



# 5. UVA PUBLICATIONS OVER TIME -------------------------------------------

# Number of uva-authored publications and percent of uva-authored
# publications in Big 5 over time

# reshape time data to long format: pub2008-pub2017, scopus2008-scopus2017

big5pub <- big5 %>% 
  select(provider, pub2008:pub2017, scopus2008:scopus2017) %>% 
  pivot_longer(-provider, 
               names_to = c(".value", "year"),
               names_sep = -4) %>% 
  mutate(uvaper = (pub/scopus)*100)

# Big 6 (Elsevier Free and Elsevier Subscribed)
big6pub <- big6 %>% 
  select(provider, pub2008:pub2017, scopus2008:scopus2017) %>% 
  pivot_longer(-provider, 
               names_to = c(".value", "year"),
               names_sep = -4) %>%  
  mutate(uvaper = (pub/scopus)*100,
         els = if_else(str_detect(provider,"Freedom"), "Yes", "No"))



# define plot function
plot_fn <- function(data, y, title, ylab, big6 = FALSE){
  y <- enquo(y)
  p <- ggplot(data, aes(x = year, y = !! y, group = provider))
    if(!big6) {
      p <- p + geom_line(aes(color = provider)) +
        scale_color_brewer(type = "qual", palette = "Set1")
    } else {
      p <- p + geom_line(aes(color = provider, linetype = provider)) +
        scale_color_manual("Provider", values = pal) +
        scale_linetype_manual("Provider", values = c(2,1,1,1,1,1))
    } 
  p + labs(title = title,
           subtitle = "In Big 5 Providers",
           x = "Year", y = ylab, color = "Provider")
}
  
p1 <- plot_fn(big5pub, y = scopus, ylab = "Number of Articles",
             title = "Total Number of Articles Published") + 
  scale_y_continuous(labels = scales::comma) 
p2 <- plot_fn(big5pub, y = pub, ylab = "Number of Articles",
             title = "Number of Articles by UVA Authors")
p3 <- plot_fn(big5pub, y = uvaper, ylab = "Percent of Articles",
             title = "Percent of All Articles by UVA Authors")

# create big 5 plot
plot_grid(p1, p2, p3)

# big 6 plots
p1 <- plot_fn(big6pub, y = scopus, ylab = "Number of Articles",
             title = "Total Number of Articles Published", 
             big6 = TRUE) + 
  scale_y_continuous(labels = scales::comma) 
p2 <- plot_fn(big6pub, y = pub, ylab = "Number of Articles",
             title = "Number of Articles by UVA Authors", 
             big6 = TRUE)
p3 <- plot_fn(big6pub, y = uvaper, ylab = "Percent of Articles",
             title = "Percent of All Articles by UVA Authors", 
             big6 = TRUE)

# create big 6 plot
plot_grid(p1, p2, p3)



# 6. OA AVAILABLE PUBLICATIONS OVER TIME ----------------------------------

# Number of oa-available publications and percent of oa-available
# publications in Big 5 over time

# reshape time data to long format: oa2008-ao2017, scopus2008-scopus2017

big5oa <- big5 %>% 
  select(provider, oa2008:oa2017, scopus2008:scopus2017) %>% 
  pivot_longer(-provider, 
               names_to = c(".value", "year"),
               names_sep = -4) %>% 
  mutate(oaper = (oa/scopus)*100)

big6oa <- big6 %>% 
  select(provider, oa2008:oa2017, scopus2008:scopus2017) %>% 
  pivot_longer(-provider, 
               names_to = c(".value", "year"),
               names_sep = -4) %>% 
  mutate(oaper = (oa/scopus)*100,
         els = if_else(str_detect(provider,"Freedom"), "Yes", "No"))


# labels to add 2017 values at end of lines - big 5
p3_labels <- big5oa %>% 
  group_by(provider) %>% 
  filter(year == "2017") %>% 
  mutate(oaper = round(oaper))

# labels to add 2017 values at end of lines - big 6
p3_labels2 <- big6oa %>% 
  group_by(provider) %>% 
  filter(year == "2017") %>% 
  mutate(oaper = round(oaper))


p1 <- plot_fn(big5oa, y = scopus, ylab = "Number of Articles",
              title = "Number of Articles Published") + 
  scale_y_continuous(labels = scales::comma) 
p2 <- plot_fn(big5oa, y = oa, ylab = "Number of Articles",
              title = "Number of OA-Available Articles")
p3 <- plot_fn(big5oa, y = oaper, ylab = "Percent of Articles",
              title = "Percent of OA-Available Articles") +
  geom_text(aes(x = year, y = oaper, label = oaper), p3_labels, nudge_x = 0.2)

# create big 5 plot
plot_grid(p1, p2, p3)

# big 6 plots
p1 <- plot_fn(big6oa, y = scopus, ylab = "Number of Articles",
              title = "Total Number of Articles Published", 
              big6 = TRUE) + 
  scale_y_continuous(labels = scales::comma) 
p2 <- plot_fn(big6oa, y = oa, ylab = "Number of Articles",
              title = "Number of Articles by UVA Authors", 
              big6 = TRUE)
p3 <- plot_fn(big6oa, y = oaper, ylab = "Percent of Articles",
              title = "Percent of All Articles by UVA Authors", 
              big6 = TRUE) +
  geom_text(aes(x = year, y = oaper, label = oaper), p3_labels2, nudge_x = 0.2)

# create big 6 plot
plot_grid(p1, p2, p3)


