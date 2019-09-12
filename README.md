# 1figrviz
Repository for code, visualizations from UVA Library's 1figr data

* R -- contains R code and Rmarkdown files for visualizations to date. Each .R file matches a .Rmd file that generate the same figures; the .Rmd file contains additional narrative to aid in interpretation.
   * R scripts are structured to call the 1figr excel spreadsheet from a subdirectory called 1science
   * Figure 3 assumes access to a supplementary spreadsheet, also in the 1science subdirectory, containing 5 fields: provider name, platform type, funding source, 2017 package cost, title level cost available. Only provider and 2017 cost are used for the big 5 providers so this could be reduced (the names(cost) command will need to be altered to match the available fields in a reduced file).
* Output of Rmarkdown files can be seen at [https://uvastatlab.github.io/1figrviz/](https://uvastatlab.github.io/1figrviz/)
* Python -- contain Python scripts for visualizations to date. Documentation will be improved on an ongoing basis!
