#Add our dependencies
import csv
import os
# Assign a variable to load a file from a path
file_to_load = os.path.join("Resources", "election_results.csv")

#Assign a variable to save the file to a path 
file_to_save = os.path.join("analysis", "election_analysis.txt")

#initialize total votes to 0
total_votes = 0 
# declare new list for candidate names
candidate_options = []
# declare empty dictionary for vote counts by candidate
candidate_votes = {}
#Winning Cndidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open the election results and read the file
with open(file_to_load) as election_data: 
    #TO DO: read and analyze the data here
    file_reader = csv.reader(election_data)  

 #Read the header row
    headers = next(file_reader)

# Print each row in the CSV file
    for row in file_reader:
        total_votes += 1
    
    # Print the candidate name from each row
        candidate_name = row[2]
        # only add candidate name if it is not already on list
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            # get vote count per candidate start the count at 0 
            candidate_votes[candidate_name] = 0 
        # Add a vote to the candidate's count
        candidate_votes[candidate_name] += 1
   #save the results to our text file
    with open (file_to_save,"w") as txt_file:

    #Print the final vote count to the termin
        election_results = (
            f"\nElection Results\n"
            f"--------------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"--------------------------------\n")
        print(election_results, end="")

        #Save the final vote count to the text file
        txt_file.write(election_results)

        


        # iterate through candidate list
        for candidate_name in candidate_votes:
            #retrieve vote count of a candidate
            votes = candidate_votes[candidate_name]
            
            # Calculate the percentage of votes
            vote_percentage = float(votes) / float(total_votes) * 100
            #Print the candidate name and percentage of votes (:.2f is precision 2 decimal)
            #print(f"{candidate_name}: received {vote_percentage:.2f}% of the vote")
            candidate_results = (f"{candidate_name}: received {vote_percentage:.2f}% of the vote\n")
            #Print each candidate, their vote count and percentage to the terminal
            print(candidate_results)
            #Save the candidate results to our text file
            txt_file.write(candidate_results)


            #print out each candidate's name, vote count, and percentage of votes to the terminal
            #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        
            #determine winning vote count and candidate
            # Determine if the votes are greater than the winning count
            if(votes > winning_count) and (vote_percentage > winning_percentage):
                #if true set winning_count = votes an winning_percent =
                #vote_percentage
                winning_count = votes
                winning_percentage = vote_percentage

                #set the winning_candidate equal to the candidate's name
                winning_candidate = candidate_name
        winning_candidate_summary = (
            f"----------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"-----------------------------\n"
            )
        print(winning_candidate_summary)
        # Add to the total vote count
        #  total_votes += 1
         #Save the winning candidate's results to the text file
        txt_file.write(winning_candidate_summary)   
        # Print the total votes
        #print(total_votes)
        # Print candidate options
        #print(candidate_votes)