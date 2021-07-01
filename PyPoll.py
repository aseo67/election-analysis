#Add our dependencies
import csv
import os

#Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
#Assgn a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#Initialize a total vote counter.
total_votes = 0

#Start new list for list of candidates & new dictionary for candidate vote counts
candidate_options = [] 
candidate_votes = {}
#Create empty string for winning candidate and create winning count trackers
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open the election results and read the file.
with open(file_to_load) as election_data:
 
    #Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    #Read the header row.
    headers = next(file_reader)

    #Loop each row in the CSV file and add to total count.
    for row in file_reader:
        #Add to the total vote count.
        total_votes += 1
        #Print candidate name from each row
        candidate_name = row[2]
        #Add candidate name to candidate options list, if new to list
        if candidate_name not in candidate_options:
            #Add to list
            candidate_options.append(candidate_name)
            #Begin tracking vote count
            candidate_votes[candidate_name] = 0
        #Add to candidate vote counts
        candidate_votes[candidate_name] += 1

#Save results to our text file.
with open(file_to_save, "w") as txt_file:

    #Print final vote count
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")

    #Save the final vote count to the text file.
    txt_file.write(election_results)
    
    #Determine percentage of votes for each candidate by looping through the counts.
    for candidate_name in candidate_votes:
        #Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name]
        #Calculate percentage of votes.
        vote_percentage = float(votes) / float(total_votes) * 100

        #Print each candidate's name, vote count, and percentage of votes
        candidate_results = (f'{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n')
        print(candidate_results)
        #Save candidate results to our text file.
        txt_file.write(candidate_results)

        # Determine winning vote count, winning percentage, and winning candidate.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage

    #Create and print winning candidate summary.
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    #Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)
