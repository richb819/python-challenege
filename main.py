import pandas as pd
import numpy as np
import os
import glob

def main():

	path = os.getcwd()

	electionFiles = glob.glob(os.path.join(path,"election*.csv"))
	electionData = pd.concat((pd.read_csv(f) for f in electionFiles))

	electionData['Votes'] = 1

	numVotes = sum(electionData['Votes'])
	
	pivot = pd.pivot_table(electionData, index='Candidate', values='Votes', aggfunc=np.sum)

	pivot['Percent Total (%)'] = (pivot['Votes'] / numVotes) * 100

	winner = pivot['Votes'].idxmax()

	print("The total number of Votes is: {}".format(numVotes))
	print(" ")
	print("Here's a list of the Candidates, thier number of votes, and the percent of the total votes")
	print(pivot)
	print(" ")
	print("This means the winner is {}".format(winner))
	print(" ")


if __name__ == "__main__":
	main()