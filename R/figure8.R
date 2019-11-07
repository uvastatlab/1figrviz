# Figure 8
# same as figure 7 but grouped by discipline instead of domain

library(tidyverse)
library(RColorBrewer)
library(scales)
library(readxl)

journal <- readRDS("1science/journal.rds")
discipline <- read_excel("1science/New_Disciplines_-_1figr.xlsx")
names(discipline) <- tolower(names(discipline))

# journal has "N/A" as a field and subfield category; otherwise same as discipline

journal <- left_join(journal, discipline, by = c("domain", "field", "subfield")) 

# USE OF ELSEVIER BY DOMAIN ----
# ----------------------------------------------
# keep only elsevier
els <- journal %>% 
  select(journal, provider, provider2, type, jr1, jr5, cites, pubs, discipline) %>% 
  filter(type == "Journal" & provider == "Elsevier") %>% 
  mutate(jr1 = as.integer(jr1), jr5 = as.integer(jr5))

# group/summarize by domain
els_group <- els %>% 
  group_by(discipline) %>% 
  summarize(jr1 = sum(jr1, na.rm = TRUE),
            jr5 = sum(jr5, na.rm = TRUE),
            refs = sum(cites, na.rm = TRUE),
            pubs = sum(pubs, na.rm = TRUE)) %>% 
  mutate(domain = factor(discipline))


# plot function
plot_fn <- function(x, title){
  x <- enquo(x)
  
  ymax <- els_group %>% summarise(ymax = max(!! x)) %>% pull() * 1.1
  els_group %>% 
    mutate(domain = fct_reorder(domain, !! x)) %>% 
    ggplot(aes(x = !! x, y = domain)) + 
    geom_segment(aes(y = domain, yend = domain, x = 0, xend = !! x), color = "grey", size = 1) +
    geom_point(size = 2) +
    scale_x_continuous(labels = scales::comma, limits = c(0, ymax)) +
    labs(title = title,
         subtitle = "By Article Discipline",
         y = "", x = "Number of Downloads") +
    geom_text(aes(label = comma(!! x)), hjust = -0.4, color = "black", size = 3) +
    theme(legend.position = "none") 
}

# plot jr1 by domain
plot_fn(jr1, title = "All 2017 Downloads from Elsevier Journals")
# plot jr5 by domain
plot_fn(jr5, title = "Current Year 2017 Downloads from Elsevier Journals")
# plot refs by domain
plot_fn(refs, title = "UVA References in Elsevier Journals")
# plot pubs by domain
plot_fn(pubs, title = "UVA-Authored Publications in Elsevier Journals")



# adding Cleveland dot plots for Els sub vs free
# source: https://uc-r.github.io/cleveland-dot-plots

# group/summarize by domain and provider2 (Els free and subs)
# Note: General domain has no data for Elsevier subscribed
els_group2 <- els %>% 
  group_by(discipline, provider2) %>% 
  summarize(jr1 = sum(jr1, na.rm = TRUE),
            jr5 = sum(jr5, na.rm = TRUE),
            refs = sum(cites, na.rm = TRUE),
            pubs = sum(pubs, na.rm = TRUE)) %>% 
  ungroup() %>% 
  mutate(domain = factor(discipline))

# Two colors taken from brewer.pal(n = 7, name = "BuPu")
pal <- c("#8C96C6", "#6E016B")


plot_fn2 <- function(x, title){
  x <- enquo(x)
  
  # get lables for plot
  right_label <- els_group2 %>%
    select(domain, provider2, !! x) %>% 
    group_by(domain) %>%
    arrange(desc(!! x)) %>%
    top_n(1, wt = !! x)
  left_label <- els_group2 %>%
    select(domain, provider2, !! x) %>% 
    group_by(domain) %>%
    arrange(desc(!! x)) %>%
    slice(2) %>% 
    arrange(desc(!! x))
  
  # set x-axis plot limits  
  ymax <- els_group2 %>% summarise(ymax = max(!! x)) %>% pull() * 1.2
  ymin <- els_group2 %>% summarise(ymin = max(!! x)) %>% pull() * -0.15
  
  # generate the plot
  els_group2 %>% 
    mutate(domain = fct_reorder(domain, !! x)) %>% 
    ggplot(aes(x = !! x, y = domain)) +
    geom_line(aes(group = domain)) +
    geom_point(aes(color = provider2), size = 2) +
    geom_text(data = right_label, aes(color = provider2, label = scales::comma(!! x)),
              size = 3, hjust = -.5, show.legend = F) +
    geom_text(data = left_label, aes(color = provider2, label = scales::comma(!! x)),
              size = 3, hjust = 1.5, show.legend = F) +
    scale_x_continuous(labels = scales::comma, limits = c(ymin, ymax)) +
    scale_color_manual("", values = pal) +
    labs(title = title,
         subtitle = "By Article Domain",
         x = "Number of Downloads", y = "") 
}


plot_fn2(jr1, title = "All 2017 Downloads from Elsevier Journals")
plot_fn2(jr5, title = "Current Year 2017 Downloads from Elsevier Journals")
plot_fn2(refs, title = "UVA References in Elsevier Journals")
plot_fn2(pubs, title = "UVA-Authored Publications in Elsevier Journals")

