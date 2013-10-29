aqoli
=====

Alexandria Quality of Life Indicators

AQOLI ERD.jpg => diagram of data warehouse design, based on star schema

warehouse_script.sql => sample code to generate data warehouse in SQL-based RDBMS (syntax for PostgreSQL)

/data directory contains individual and bundled indicator files, in CSV format with consistent column headers:

* all\_annual_indic.csv => All annual indicators
* all_indic.csv => All annual and monthly indicators
* ind2\_1\_income_housing.csv => Data for indicator 2.1--housing costs as a percentage of income
* and similar for the rest of the indicators in themes 2 through 11 (no data available yet for indicators in theme 1)
* theme2\_annual_indic.csv => All annual indicators for theme 2 (Basic Needs)
* theme2\_monthly_indic.csv => All monthly indicators for theme 2
* theme4\_annual\_indic.csv - theme11\_annual\_indic.csv => All indicators for themes 4 through 11 (Theme 3 only has one indicator, contained in ind3\_1\_youthencourage.csv)

/data/metadata directory contains Excel metadata files describing the bundled indicator files:

* AQOLI\_indicator\_metadata.xls => Metadata file for all\_indic.csv
* theme2\_annual\_metadata.xls => Metadata file for theme2\_annual\_indic.csv
* theme2\_monthly\_metadata.xls => Metadata file for theme2\_monthly\_indic.csv
* theme3\_metadata.xls - theme11\_metadata.xls => Metadata files for each theme's indicators