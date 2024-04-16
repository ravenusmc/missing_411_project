# importing supporting libraries
import numpy as np
import pandas as pd

class ExamineCSV():

    def __init__(self):
        self.data = pd.read_csv('./data/Missing.csv')

    # Get the top 5 states
    def states_with_most_missing_people(self):
        top_5_states = self.data['state/province'].value_counts().head(5)
        top_5_states = pd.DataFrame(list(top_5_states.items()), columns=['State', 'Values'])
        top_5_states_list = []
        columns = ['State', 'Count']
        top_5_states_list.append(columns)
        count = 0 
        while count < len(top_5_states):
            rows = []
            state = top_5_states.iloc[count,0]
            missing_count = int(top_5_states.iloc[count,1])
            rows.append(state)
            rows.append(missing_count)
            top_5_states_list.append(rows)
            count += 1 
        return top_5_states_list
    


# Graphs to make:
# number of people missing by year - or decade? 
# -most common ages of people missing 
# -Sex of people missing - allow user to select decades?
# -Graph of Volume - Easter or Western US

obj = ExamineCSV()
obj.states_with_most_missing_people()