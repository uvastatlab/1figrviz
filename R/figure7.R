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
  select(journal, provider, provider2, type, jr1, jr5, cites, pubs, domain) %>% 
  filter(type == "Journal" & provider == "Elsevier") %>% 
  mutate(jr1 = as.integer(jr1), jr5 = as.integer(jr5))

# group/summarize by domain
els_group <- els %>% 
  group_by(domain) %>% 
  summarize(jr1 = sum(jr1, na.rm = TRUE),
            jr5 = sum(jr5, na.rm = TRUE),
            refs = sum(cites, na.rm = TRUE),
            pubs = sum(pubs, na.rm = TRUE)) %>% 
  mutate(domain = factor(domain))


# plot function
plot_fn <- function(y, title){
  y <- enquo(y)
  els_group %>% 
    mutate(domain = fct_reorder(domain, !! y)) %>% 
    ggplot(aes(x = domain, y = !! y, color = domain)) + 
    geom_segment(aes(x = domain, xend = domain, y = 0, yend = !! y), color = "grey", size = 1) +
    geom_point(size = 5) +
    scale_y_continuous(labels = scales::comma) +
    scale_color_brewer(palette = "BuPu", direction = 1) +
    labs(title = title,
         subtitle = "By Article Domain",
         x = "", y = "Number of Downloads") +
    geom_text(aes(label = comma(!! y)), nudge_x = -.25, color = "black", size = 3) +
    theme(legend.position = "none") +
    coord_flip() 
}


# plot jr1 by domain
plot_fn(jr1, title = "All 2017 Downloads from Elsevier Journals")
# plot jr5 by domain
plot_fn(jr5, title = "Current Year 2017 Downloads from Elsevier Journals")
# plot refs by domain
plot_fn(refs, title = "UVA References in Elsevier Journals")
# plot pubs by domain
plot_fn(pubs, title = "UVA-Authored Publications in Elsevier Journals")

# Percents
els_total <- els_group %>% 
  mutate(refs = as.integer(refs),
         pubs = as.integer(pubs)) %>% 
  summarize_if(is.integer, sum)

percents <- els_group$jr1/els_total$jr1
percents[5]


# adding Cleveland dot plots for Els sub vs free
# source: https://uc-r.github.io/cleveland-dot-plots

# group/summarize by domain and provider2 (Els free and subs)
# Note: General domain has no data for Elsevier subscribed
els_group2 <- els %>% 
  group_by(domain, provider2) %>% 
  summarize(jr1 = sum(jr1, na.rm = TRUE),
            jr5 = sum(jr5, na.rm = TRUE),
            refs = sum(cites, na.rm = TRUE),
            pubs = sum(pubs, na.rm = TRUE)) %>% 
  ungroup() %>% 
  mutate(domain = factor(domain))

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
  ymax <- els_group2 %>% summarise(ymax = max(!! x)) %>% pull() * 1.15
  ymin <- els_group2 %>% summarise(ymin = max(!! x)) %>% pull() * -0.1
  
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
