# 1figr data prep
library(tidyverse)
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

# add Elsevier grouping to journal

################################################################################
# If not affiliated with the Univ of Virginia, comment out the following lines;
################################################################################

# Here is the spreadsheet with the ISSN’s for the Subscribed and Freedom
# Collections
#
# The two worksheets to use are "All Subscribed Journals" and "All Freedom
# Journals" which are the 6th and 7th tabs. The column to use is the second one
# “ISSN”. Anything which isn’t in either of these two lists, but is in the 1figr
# Elsevier list, goes into the "Elsevier Unmatched" category for the figures.

# “All Subscribed Journals”
elsevier_subscribed <- read_excel("1science/Elsevier_2019_Dec_05.xlsx", 
                                  sheet = "All Subscribed Journals")
elsevier_subscribed <- elsevier_subscribed %>% filter(!is.na(ISSN)) %>% 
  select(ISSN, Product)
nrow(elsevier_subscribed)

# "All Freedom Journals"
elsevier_freedom <- read_excel("1science/Elsevier_2019_Dec_05.xlsx", 
                                  sheet = "All Freedom Journals")
elsevier_freedom <- elsevier_freedom %>% filter(!is.na(ISSN)) %>% 
  select(ISSN, Product)
nrow(elsevier_freedom)

# all 1figr Elsevier journals
elsevier_1figr <- journal %>% 
  filter(provider == "Elsevier" & !is.na(issn)) %>% 
  select(issn, journal)
nrow(elsevier_1figr)

# split ISSN by ||, for 1figr Elsevier journals
journal_issn <- str_split(elsevier_1figr$issn, pattern = "\\|\\|") %>% map(str_trim)

# find 1figr ISSN not in elsevier_subscribed
# TRUE = not in elsevier_subscribed
# FALSE = in elsevier_subscribed
lst.out <- sapply(journal_issn, function(x)all(is.na(match(x, elsevier_subscribed$ISSN))))

# find 1figr ISSN not in elsevier_freedom;
# TRUE = not in elsevier_freedom
# FALSE = in elsevier_freedom
lst.out2 <- sapply(journal_issn, function(x)all(is.na(match(x, elsevier_freedom$ISSN))))

# create unmatched indicator
table(lst.out)
table(lst.out2)
table(lst.out,lst.out2)
which(lst.out == FALSE & lst.out2 == FALSE)

unmatched <- lst.out & lst.out2
sum(unmatched)

# create variable to indicate unmatched, subscribed, freedom;
# unmatched == 1
elsevier_1figr$subscription <- as.numeric(unmatched)

# freedom
elsevier_1figr$subscription <- if_else(!lst.out2, 2, elsevier_1figr$subscription)

# subscribed
elsevier_1figr$subscription <- if_else(!lst.out, 3, elsevier_1figr$subscription)

# recode the numbers
elsevier_1figr$subscription <- recode(elsevier_1figr$subscription, 
                                      `1` = "Elsevier Unmatched",
                                      `2` = "Elsevier Freedom",
                                      `3` = "Elsevier Subscribed")

# Check EP's results
# cf_unmatched <- filter(elsevier_1figr, unmatched)
# ep_unmatched <- read_csv("Elsevier_Unmatched_Titles.csv") %>% select(Journal, `ISSN/eISSN`)
# 
# anti_join(ep_unmatched, cf_unmatched, by = c("Journal" = "journal"))

# merge freedom indicator back into data
journal <- elsevier_1figr %>% 
  left_join(journal, ., by = c("issn", "journal"))

# create second provider column that distinguishes between elsevier unmatched,
# freedom and subscribed
journal$provider2 <- journal$provider
journal$provider2 <- if_else(journal$provider == "Elsevier", 
                             true = journal$subscription, 
                             false = journal$provider)
journal <- journal %>% select(sort, journal, issn, provider, provider2, everything(), -subscription)

################################################################################
# End Univ of Virginia specific work
################################################################################



saveRDS(journal, file = "1science/journal.rds")

# 12/6/2019

# send me the list of the journals in the Elsevier_2019_Dec_05 “All Subscribed”
# and “All Freedom” tabs that don’t match anything in 1figr.

all_1figr_issn <- str_split(journal$issn, pattern = "\\|\\|") %>% 
  map(str_trim)
which(sapply(all_1figr_issn, length) == 6)

# reshape
journal2 <- journal %>% select(issn, journal) %>% 
  separate(issn, into = paste0("issn",1:6), sep = "\\|\\|") %>% 
  gather(key = which_issn, value = issn, -journal) %>% 
  filter(!is.na(issn)) %>% 
  str_trim(issn)

journal2$issn <- str_remove_all(journal2$issn, pattern = "[[:space:]]")

# remove duplicates
journal2 <- journal2[!duplicated(journal2$issn),]

# all Elsevier_2019_Dec_05
free_and_sub <- bind_rows(elsevier_freedom, elsevier_subscribed)

# journals in the Elsevier_2019_Dec_05 "All Subscribed" # and "All Freedom" tabs
# that don’t match anything in 1figr.
reverse_unmatched <- free_and_sub[!free_and_sub$ISSN %in% journal2$issn,]
write.csv(reverse_unmatched, file = "reverse_unmatched.csv", row.names = FALSE)
