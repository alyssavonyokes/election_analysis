# Add our dependencies.
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initalize the total vote counter.
total_votes = 0
candidate_options = []
candidate_votes = {}
county_votes = {}
largest_county_turnout = ""
county_options = []
winning_tally = 0
winning_county_percentage = 0
winning_county = ""

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    # To do: read and analyze the data here.
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    print(headers)

    # Print each row in the CSV file.
    for row in file_reader:
        # Add to the total vote count.
        total_votes += 1
        # Print the candidate name from each row
        candidate_name = row[2]
        #Print county name from each row
        county_name = row[1]
        # If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            candidate_options.append(candidate_name)
            # Begin tracking that candidate's vote count. 
            candidate_votes[candidate_name] = 0
        # Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1
        # Insert county analysis code.
        if county_name not in county_options:
            county_options.append(county_name)
            county_votes[county_name] = 0
        county_votes[county_name] += 1


        
# Save the results to the txt file.
with open(file_to_save, "w") as txt_file:
        # Print the final vote count to the terminal.
        election_results = (
            f"\nElection Results\n"
            f"-------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"-------------------------\n\n"
            # add in County Votes statistic row
            f"County Votes:\n")
        print(election_results, end="")
        # Save the final vote count to the text file.
        txt_file.write(election_results)
         # Determine the percentage of votes for each candidate by looping through the counts.
        # 1. Iterate through the candidate list.

        for county in county_votes:
            # Retrieve number of votes in county.
            tally = county_votes[county]
            # Calculate the percentage of votes per county.
            tally_percentage = float(tally) / float (total_votes) * 100
            # Print the county and percentage of votes per county.
            county_results = (f"{county}: {tally_percentage:.1f}% ({tally:,})\n")

            # Print results to txt.file
            txt_file.write(county_results)

            if (tally > winning_tally) and (tally_percentage > winning_county_percentage):
                winning_tally = tally
                winning_county_percentage = tally_percentage
                winning_county = county
        winning_county_summary = (
            f"\n"
            f"-------------------------\n"
            f"Largest County Turnout: {winning_county}\n"
            f"-------------------------\n")
        print(winning_county_summary)
        txt_file.write(winning_county_summary)

        for candidate in candidate_votes:
            # 2. Retrieve vote count of a candidate.
            votes = candidate_votes[candidate]
            # 3. Calculate the percentage of votes.
            vote_percentage = float(votes) / float(total_votes) * 100
            # 4. Print the candidate name and percentage of votes.
            candidate_results = (f"{candidate}: {vote_percentage:.1f}% ({votes:,})\n")

            # Print each candidate, their voter count, and percentage to the terminal.
            print(candidate_results)
            #  Save the candidate results to our text file.
            txt_file.write(candidate_results)
            # Determine winning vote count and candidate
            # 1. Determine if the votes are greater than the winning count.
            if (votes > winning_count) and (vote_percentage > winning_percentage):
                # 2. If true then set winning_count = votes and winning_percent = vote_percentage.
                winning_count = votes
                winning_percentage = vote_percentage
                winning_candidate = candidate  
        # Print the winning candidate's results to the terminal.
        winning_candidate_summary = (
            f"-------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"-------------------------\n")
        print(winning_candidate_summary)
        # Save the winning candidate's results to the text file.
        txt_file.write(winning_candidate_summary)