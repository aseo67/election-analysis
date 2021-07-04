# PyPoll with Python
Module 3 Challenge Data Analysis File Links
- ![election_analysis.txt](https://github.com/aseo67/election-analysis/blob/main/analysis/election_analysis.txt)
- ![Python Code](https://github.com/aseo67/election-analysis/blob/main/PyPoll_Challenge.py)
- ![election_results.csv](https://github.com/aseo67/election-analysis/blob/main/Resources/election_results.csv)

## Overview of Election Audit
The Colorado Board of Elections is tasked to complete the election audit of a recent local congressional election. The analysis needed involves:

1. Calculating the number of votes cast.
2. Getting a complete list of candidates who received votes.
3. Calculating the total number of votes and percentage of votes each candidate received.
4. Determining the winner of the election based on popular vote.
5. Analyzing county-level statistics for: the total number of votes of each county, the percentage of votes of each county, and determining the county with the largest voter turnout. 

## Resources
- Data Source: election_result.csv (see above for link)
- Software: Python 3.7.6, Visual Studio Code 1.57.1

## Election Audit Results
The analysis of the election shows that: 
- There were **369,711** votes cast in the election.
- Results by county were as follows:
    - Jefferson county contributed **10.5%** of the vote, **38,855** votes total. 
    - Denver county contributed **82.8%** of the vote, **306,055** votes total. 
    - Arapahoe county contributed **6.7%** of the vote, **24,801** votes total. 
- **Denver** county had the largest number of votes.
- The candidates were:
    - Charles Casper Stockham
    - Diana DeGette
    - Raymon Anthony Doane
- The candidate results were: 
    - Charles Casper Stockham received **23.0%** of the vote and **85,213** total votes.
    - Diana DeGette received **73.8%** of the vote and **272,892** total votes.
    - Raymon Anthony Doane received **3.1%** of the vote and **11,606** total votes.
- The winner of the election was: 
    - **Diana DeGette**, who received **23.0%** of the vote and **85,213** total votes.

## Election Audit Summary
To execute this analysis, a Python script was created to help automate the tallying process and export of results. This script can be utilized in future elections as well to help expedite the analysis of future votes and compile the needed totals in an easy-to-read format. To adapt this script for future elections, only a few minor updates would be needed. 

1. Updating the file path for loading the ballot data (i.e. updating the .csv file to import, assigned to the "file_to_load" variable in the below screenshotted script). And updating the file path for saving the analysis results (i.e. locating where to save the .txt file, assigned to the "file_to_save" variable below).
    
    ![Screenshot](https://github.com/aseo67/election-analysis/blob/main/Resources/Screenshot_file%20load%20file%20save%20code.png)
2. Checking to make sure .csv data is also formatted in the following order (of columns of data): Ballot ID, County, Candidate. If this is not true, the proper positions would need to be reflected in the below code, when extracting county and candidate names from the data. Currently, the code reflects the county name as the second item of each row provided in the csv, and the candidate name as the third item. 
    
    ![Screenshot](https://github.com/aseo67/election-analysis/blob/main/Resources/Screenshot_get%20county%20candidate%20names.png)
3. If any formatting/wording would like to be updated for the export of results (.txt file), updates can be made to the following code as needed. Formatting of all the results are located within the f-strings written in this code. 
    
    ![Screenshot](https://github.com/aseo67/election-analysis/blob/main/Resources/Screenshot_total%20votes.png)
    ![Screenshot](https://github.com/aseo67/election-analysis/blob/main/Resources/Screenshot_county%20votes.png)
    ![Screenshot](https://github.com/aseo67/election-analysis/blob/main/Resources/Screenshot_largest%20county.png)
    ![Screenshot](https://github.com/aseo67/election-analysis/blob/main/Resources/Screenshot_winning%20votes.png)


