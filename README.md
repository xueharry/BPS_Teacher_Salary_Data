`BPShighschool.csv` is a dataset containing the 2014 salaries of full-time teachers from 27 Boston public high schools. The data was gathered from the publically available City of Boston Employee Earnings Report from 2014 and was cleaned using python.

#Preprocessing Methodology

1. https://data.cityofboston.gov/Finance/Employee-Earnings-Report-2014/4swk-wcg8
is the source of raw data of the salaries of Boston city employees from 2014.

2. "Teacher" was entered as a search term to narrow the results to teachers. However, this data still included results for elementary, middle, adult education and substitute teachers. This data was downloaded in csv format and renamed to `raw.csv`.

3. The script `preprocessing.py` further narrows the data down to employees with the title "Teacher" (thus discounting substitute teachers) from 27 of Boston's 29 high schools. For the purposes of this dataset, "high school" was defined to include all the non-alternative and non-special education schools that serve grades 9-12 within the Boston Public Schools. Two schools (Dearborn and Henderson) are not included because the data in raw.csv does not distinguish which teachers at these schools teach at the high school level. However, the 3 exam schools (BLS, BLA and O'Bryant) were included despite the fact that they also serve grades 7 and 8.  Additionally, all dollar signs were removed from data figures to help facilitate future analysis.





