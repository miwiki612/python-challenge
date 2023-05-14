
import os

import csv

# in instructor's .py path is with ".." , don't know why doesn't work, mine works with "." 
csvpath = os.path.join(".", "PyPoll","Resources","election_data.csv")

election_rows = []
# read data csv and convert it to list for each column
with open( csvpath, encoding='UTF-8') as csvfile:
    election_data = csv.reader( csvfile, delimiter="," )
    
    col_id = []
    col_country = []
    col_candidate = []
    
    for index, row in enumerate(election_data):
        col_id.append( row[0] )
        col_country.append( row[1] )
        col_candidate.append( row[2] )
        election_rows.append( row )

# create dictionary for election data
election_dict = { col_id[0] : col_id[ 1 : ] ,  col_country[0] : col_country[ 1 : ] , col_candidate[0] : col_candidate[ 1 : ]} 

# list for result to print
break_line = "-------------------------" 
analysis_ls = ["Election Results", break_line ]

# The total number of votes cast
total_vote = len(election_dict["Ballot ID"])
analysis_ls.append( f'Total Vote: {total_vote}')
analysis_ls.append( break_line )

# A complete list of candidates who received votes
# list for all candidates
candidate_list = list( set(election_dict["Candidate"] ) )
candidate_list.sort()

# every candidate's vote
candidate_vote = []
for candidate in candidate_list :
    vote_individual = election_dict["Candidate"].count(candidate)
    candidate_vote.append( vote_individual )
    # The percentage of votes each candidate won
    # The total number of votes each candidate won
    analysis_ls.append( f'{candidate}: {round(vote_individual / total_vote*100,3)}% ({vote_individual})')
    
    
analysis_ls.append( break_line )

# The winner of the election based on popular vote
analysis_ls.append( f'Winner: {candidate_list[ candidate_vote.index( max(candidate_vote) ) ]}' )
analysis_ls.append( break_line )

# write and print result
analysis_path = os.path.join("." , "PyPoll","analysis","election_analysis.txt")
with open( analysis_path , 'w') as result_txt :
    for i in analysis_ls:
        print(i)
        result_txt.write( i )
        result_txt.write('\n')