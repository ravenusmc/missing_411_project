# importing supporting libraries
import numpy as np
import pandas as pd

class ExamineCSV():

    def __init__(self):
        self.data = pd.read_csv('./data/Missing.csv')

    # Get the top 5 states
    def states_with_most_missing_people(self):
        top_5_states = self.data['state/province'].value_counts().head(5)
        top_5_states_list = [['State', 'Count']]  # Initialize the list with column headers
        for state, count in top_5_states.items():
            top_5_states_list.append([state, count]) 
        return top_5_states_list
    
    # Gets the number of missing people by decade 
    def number_of_people_missing_by_decade(self):
        pass


# Graphs to make:
# number of people missing by year - or decade? 
# -most common ages of people missing 
# -Sex of people missing - allow user to select decades?
# -Graph of Volume - Easter or Western US

obj = ExamineCSV()
obj.states_with_most_missing_people()