#Import needed libraries
import os
import csv

#Read the election data csv file
csv_path = os.path.join('Resources', 'election_data.csv')
with open (csv_path) as csvfile:
    poll_data = csv.reader(csvfile, delimiter = ',')

    #Skip the header of the file
    header = next(poll_data)

    #Iterate through the data to get the results
    total_votes = 0
    candidates_dict = {}

    #Check for the existence of each candidate in the candidates dictionary
    for row in poll_data:
        total_votes += 1
        #If a candidate is not in the dictionary, they will be added with a value of 1 for the first instance
        if row[2] not in candidates_dict:
            candidates_dict[row[2]] = 1
        #If the candidate is already in the dictionary, add 1 for each new instance
        else:
            candidates_dict[row[2]] += 1
    
    #Calculate percentage of votes for each candidate
    votes_percentages = {}
    for candidate in candidates_dict:
        percent = round((candidates_dict[candidate]/total_votes)*100, 3)
        votes_percentages[candidate] = percent
    #Determine the winner
    winner = max(votes_percentages,key=votes_percentages.get)

    #Print the analysis to the terminal
    print("Election Results")
    print("---------------------------")
    print(f"Total Votes: {total_votes}")
    print("---------------------------")
    for candidate in candidates_dict:
        print(f"{candidate}: {votes_percentages[candidate]:.3f}% ({candidates_dict[candidate]})")
    print("---------------------------")
    print(f"Winner: {winner}")
    print("---------------------------")
    
    #Export the analysis to a text file
    analysis = os.path.join('analysis','analysis.txt')
    with open (analysis,'w') as text:
        text.write("Election Results\n")
        text.write("---------------------------\n")
        text.write(f"Total Votes: {total_votes}\n")
        text.write("---------------------------\n")
        for candidate in candidates_dict:
            text.write(f"{candidate}: {votes_percentages[candidate]:.3f}% ({candidates_dict[candidate]})\n")
        text.write("---------------------------\n")
        text.write(f"Winner: {winner}\n")
        text.write("---------------------------\n")