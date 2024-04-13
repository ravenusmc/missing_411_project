# importing supporting libraries
import numpy as np
import pandas as pd

class ExamineCSV():

    def __init__(self):
        self.data = pd.read_csv('./data/Missing.csv')

    # Get the top 5 states
    def states_with_most_missing_people(self):
        print(self.data.head())

# Graphs to make:
# number of people missing by year - or decade? 
# States with the most missing people 
# -most common ages of people missing 
# -Sex of people missing - allow user to select decades?
# -Graph of Volume - Easter or Western US

obj = ExamineCSV()
obj.states_with_most_missing_people()