# 1figr data prep
library(tidyverse)
library(RColorBrewer)
library(scales)
library(readxl)

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

# add Elsevier "freedom" indicator to journal
freedom_row_nums <- readRDS(file = "1science/freedom_row_nums.Rds")
journal$freedom <- 0
journal$freedom[freedom_row_nums] <- 1

saveRDS(journal, file = "1science/journal.rds")
