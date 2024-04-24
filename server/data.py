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
    
    def get_decade(self, date):
        return str(date.year // 10 * 10) + "s"
    
    # Gets the number of missing people by decade 
    def number_of_people_missing_by_decade(self):
        self.data['dateMissing'] = pd.to_datetime(self.data['dateMissing'], errors='coerce')
        self.data.dropna(subset=['dateMissing'], inplace=True)
        self.data['decade'] = self.data['dateMissing'].apply(self.get_decade)
        # Group by decade and count occurrences
        decade_counts = self.data.groupby('decade').size()   
        missing_by_decade_list = [['Decade', 'Count']]  
        for decade, count in decade_counts.items(): 
            missing_by_decade_list.append([decade, count])
        print(missing_by_decade_list)
    
    def most_common_ages_of_people_missing(self):
        top_5_ages = self.data['age'].value_counts().head(5)
        top_5_ages_list = [['Age', 'Count']]
        for age, count in top_5_ages.items():
            top_5_ages_list.append([age, int(count)])
        print(top_5_ages_list)
    
    def sex_of_people_missing(self):
        count_missing_by_sex = self.data['sex'].value_counts().head()
        count_missing_by_sex_list = [['Sex', 'Count']]
        for sex, count in count_missing_by_sex.items():
            count_missing_by_sex_list.append([sex, int(count)])
        print(count_missing_by_sex_list)
    
    def eastern_versus_western_us_data(self):
        # volume
        count_western_eastern = self.data['volume'].value_counts().head()
        count_western_eastern_list = [['Coast', 'Count']]
        for coast, count in count_western_eastern.items():
            count_western_eastern_list.append([coast, int(count)])
        print(count_western_eastern_list)
        pass


# Graphs to make:
# -Graph of Volume - Easter or Western US

obj = ExamineCSV()
obj.eastern_versus_western_us_data()