# Election-Analysis
## Overview of Election Audit: 
Colorado Election Commission requested and audit of a recent congressional election. The comprehensive audit will include summaries for the candidates and the counties. Below are the requirements for the audit. 

Audit for Counties: 
- Calculate total number of votes cast in the election 
- Provide a breakdown of total number of votes cast in each county
- Calculate percentage of the total votes for each county
- Identify the county with the highest turnout

Audit for Candidates: 
- Provide a list of candidates and their total vote count for the election
- Calculate the percentage of the total votes for each candidate
- Determine the winner of the election based on popular vote
- Provide the winning vote count
- Provide the winning percentage of votes 

## Election-Audit Results: 
A .csv file (election_results.csv) was provided. The file contained a unique ballot ID, County where the vote was cast and the candidate who received the vote. Summarizing the data provided the below outcomes.

There were a total of 369,711 votes cast in the election

The votes were cast in Jefferson County, Denver County and Arapahoe county. 
    
Vote count and percentage of votes per county:

1. Denver: 82.8% (306,055)
2. Jefferson: 10.5% (38,855)
3. Arapahoe: 6.7% (24,801)

Denver had the highest voter turnout.

There were three candidates who received votes in the election: Charles Casper Stockham, Diana DeGette and Raymon Anthony Doane. 

Vote count and percentage of votes per candidate:

1. Diana Degette: 73.08% (272, 892)
2. Charles Casper Stockham: 23.0% (85,213)
3. Raymon anthony Doane: 3.1% (11,606)
    
The winning candidate was Diana Degette.
        
Vote count and percentage of vote for winning candidate
- Winner: Diana Degette
- Vote Count: 272,892
- Percentage of vote: 73.8%

## Technical Overview:
The first step in the analysis was determining the total number of votes. The total provided a baseline count to ensure that the total number of votes are reflected in the breakdown by both county and candidate. 

After initializing the total vote count to zero, a FOR loop was used to iterate through the file adding 1 count for each row in the file.
```
# Initialize a total vote counter
total_votes = 0
    # For each row in the CSV file.
for row in reader:

    # Add to the total vote count
    total_votes = total_votes + 1
```
Calculate Votes: 
```
    if county_name not in county_options:

        # Add the existing county to the list of counties.   
        county_options.append(county_name)

        # Begin tracking the county's vote count.
        county_votes[county_name] = 0 
            
    # Add a vote to that county's vote count.
    county_votes[county_name] += 1
```
Total votes and percentages calculated: 
```
    for county_name in county_votes:
    # Retrieve the county vote count.
        votes1 = county_votes [county_name]
    # Calculate the percentage of votes for the county.
        county_vote_percentage = float(votes1) / float(total_votes) *100
        county_results = (
        f"{county_name}: {county_vote_percentage:.1f}% ({votes1:,})\n")
```
The next step was to determine the county with the highest turnout. 
```
if (votes1 > highest_count) and (county_vote_percentage > highest_percentage):
            highest_count = votes1
            highest_percentage = county_vote_percentage

            highest_county = county_name
```
With the analysis for the counties complete, the analysis continued with determining the candidates, the number of votes received per candidate and the percentage of votes. 
```
if candidate_name not in candidate_options:

        # Add the candidate name to the candidate list.
        candidate_options.append(candidate_name)

        # And begin tracking that candidate's voter count.
        candidate_votes[candidate_name] = 0

    # Add a vote to that candidate's count
    candidate_votes[candidate_name] += 1

for candidate_name in candidate_votes:

    # Retrieve vote count and percentage
    votes = candidate_votes.get(candidate_name)
    vote_percentage = float(votes) / float(total_votes) * 100
    candidate_results = (
        
        f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
```
Per the requirements, the winning candidate with total vote count and percentage of vote was also determined. 
```
if (votes > winning_count) and (vote_percentage > winning_percentage):
        winning_count = votes
        winning_candidate = candidate_name
        winning_percentage = vote_percentage
```
After summarizing all the data from the election_results.csv, the results were printed to a .txt file for reference.

![image](https://user-images.githubusercontent.com/88912539/133583664-933c7c87-5d32-4840-8eac-1c8ba2225927.png)

