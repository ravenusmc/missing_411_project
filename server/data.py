# importing supporting libraries
import numpy as np
import pandas as pd

class ExamineCSV():

    def __init__(self):
        self.data = pd.read_csv('./data/Missing.csv')
        # Ensure the dateMissing column is parsed as datetime with error handling
        self.data['dateMissing'] = pd.to_datetime(self.data['dateMissing'], errors='coerce')
        # Drop rows with invalid dates
        self.data = self.data.dropna(subset=['dateMissing'])

    def states_with_most_missing_people(self):
        top_5_states = self.data['state/province'].value_counts().head(5)
        top_5_states_list = [['State', 'Count']]  # Initialize the list with column headers
        for state, count in top_5_states.items():
            top_5_states_list.append([state, count]) 
        print(top_5_states_list)
        # return top_5_states_list
    
    def get_min_year(self):
        min_date = self.data['dateMissing'].min()
        min_year = min_date.year
        result_year = min_year - 3
        print(result_year)
        
    def get_max_year(self):
        print(self.data['dateMissing'].max())
    
    def get_decade(self, date):
        return str(date.year // 10 * 10) + "s"
    
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
    
    def get_missing_by_year_for_map(self, year):
        # Filter the data to include only rows up to the specified year
        filtered_data = self.data[self.data['dateMissing'].dt.year <= year]
        # Group by state and count the number of missing persons
        result = filtered_data.groupby('state/province').size().reset_index(name='missing_count')
        # Convert the result to a dictionary
        formatted_dict = dict(zip(result['state/province'], result['missing_count']))
        return formatted_dict  # Return the dictionary directly
    

    def get_data_for_one_coast_for_drilldown(self, coast):
        # Filter the data for the given coast value
        filtered_data = self.data[self.data['volume'] == coast].copy()
        # Select relevant columns
        selected_columns = filtered_data[['firstName', 'lastName', 'age', 'dateMissing', 'state/province']].copy()
        # Ensure that the 'dateMissing' column is of datetime type and extract the year
        selected_columns['yearMissing'] = pd.to_datetime(selected_columns['dateMissing'], errors='coerce').dt.year
        # Handle missing values in 'yearMissing' column
        selected_columns['yearMissing'] = selected_columns['yearMissing'].fillna(0).astype(int)
        # Handle missing values in 'age' column (if needed)
        selected_columns['age'] = selected_columns['age'].fillna(0).astype(int)
        # Select and reorder columns
        result = selected_columns[['firstName', 'lastName', 'age', 'yearMissing', 'state/province']]
        # Convert to plain Python data types
        result = result.astype({
            'firstName': 'str',
            'lastName': 'str',
            'age': 'int',
            'yearMissing': 'int',
            'state/province': 'str'
        })
        
        # Convert the DataFrame to a list of dictionaries for JSON serialization
        result_json_serializable = result.to_dict(orient='records')
        return result_json_serializable
    
    def get_data_by_state_for_drilldown(self, state):
        filtered_data = self.data[self.data['state/province'] == state].copy()
        selected_columns = filtered_data[['firstName', 'lastName', 'age', 'dateMissing', 'state/province']].copy()
        # Ensure that the 'dateMissing' column is of datetime type and extract the year
        selected_columns['yearMissing'] = pd.to_datetime(selected_columns['dateMissing'], errors='coerce').dt.year
        # Handle missing values in 'yearMissing' column
        selected_columns['yearMissing'] = selected_columns['yearMissing'].fillna(0).astype(int)
        # Handle missing values in 'age' column (if needed)
        selected_columns['age'] = selected_columns['age'].fillna(0).astype(int)
        # Select and reorder columns
        result = selected_columns[['firstName', 'lastName', 'age', 'yearMissing', 'state/province']]
                # Convert to plain Python data types
        result = result.astype({
            'firstName': 'str',
            'lastName': 'str',
            'age': 'int',
            'yearMissing': 'int',
            'state/province': 'str'
        })
        
        # Convert the DataFrame to a list of dictionaries for JSON serialization
        result_json_serializable = result.to_dict(orient='records')
        return result_json_serializable
    
    def get_data_by_decade_for_drilldown(self, decade):
        start_year = int(decade[:4])
        end_year = start_year + 9
        self.data['dateMissing'] = pd.to_datetime(self.data['dateMissing'], errors='coerce')
        filtered_data = self.data[(self.data['dateMissing'].dt.year >= start_year) & (self.data['dateMissing'].dt.year <= end_year)]
        selected_columns = filtered_data[['firstName', 'lastName', 'age', 'dateMissing', 'state/province']].copy()
        # Ensure that the 'dateMissing' column is of datetime type and extract the year
        selected_columns['yearMissing'] = pd.to_datetime(selected_columns['dateMissing'], errors='coerce').dt.year
        # Handle missing values in 'yearMissing' column
        selected_columns['yearMissing'] = selected_columns['yearMissing'].fillna(0).astype(int)
        # Handle missing values in 'age' column (if needed)
        selected_columns['age'] = selected_columns['age'].fillna(0).astype(int)
        # Select and reorder columns
        result = selected_columns[['firstName', 'lastName', 'age', 'yearMissing', 'state/province']]
                # Convert to plain Python data types
        result = result.astype({
            'firstName': 'str',
            'lastName': 'str',
            'age': 'int',
            'yearMissing': 'int',
            'state/province': 'str'
        })
        # Convert the DataFrame to a list of dictionaries for JSON serialization
        return result.to_dict(orient='records')

    def get_data_by_age_for_drilldown(self, age):
        filtered_data = self.data[self.data['age'] == age].copy()
        selected_columns = filtered_data[['firstName', 'lastName', 'age', 'dateMissing', 'state/province']].copy()
        # Ensure that the 'dateMissing' column is of datetime type and extract the year
        selected_columns['yearMissing'] = pd.to_datetime(selected_columns['dateMissing'], errors='coerce').dt.year
        # Handle missing values in 'yearMissing' column
        selected_columns['yearMissing'] = selected_columns['yearMissing'].fillna(0).astype(int)
        # Handle missing values in 'age' column (if needed)
        selected_columns['age'] = selected_columns['age'].fillna(0).astype(int)
        # Select and reorder columns
        result = selected_columns[['firstName', 'lastName', 'age', 'yearMissing', 'state/province']]
                # Convert to plain Python data types
        result = result.astype({
            'firstName': 'str',
            'lastName': 'str',
            'age': 'int',
            'yearMissing': 'int',
            'state/province': 'str'
        })
        
        # Convert the DataFrame to a list of dictionaries for JSON serialization
        result_json_serializable = result.to_dict(orient='records')
        return result_json_serializable
    
    def get_data_by_sex_for_drilldown(self, sex):
        filtered_data = self.data[self.data['sex'] == sex].copy()
        selected_columns = filtered_data[['firstName', 'lastName', 'age', 'dateMissing', 'state/province']].copy()
        # Ensure that the 'dateMissing' column is of datetime type and extract the year
        selected_columns['yearMissing'] = pd.to_datetime(selected_columns['dateMissing'], errors='coerce').dt.year
        # Handle missing values in 'yearMissing' column
        selected_columns['yearMissing'] = selected_columns['yearMissing'].fillna(0).astype(int)
        # Handle missing values in 'age' column (if needed)
        selected_columns['age'] = selected_columns['age'].fillna(0).astype(int)
        # Select and reorder columns
        result = selected_columns[['firstName', 'lastName', 'age', 'yearMissing', 'state/province']]
                # Convert to plain Python data types
        result = result.astype({
            'firstName': 'str',
            'lastName': 'str',
            'age': 'int',
            'yearMissing': 'int',
            'state/province': 'str'
        })
        
        # Convert the DataFrame to a list of dictionaries for JSON serialization
        result_json_serializable = result.to_dict(orient='records')
        return result_json_serializable

# obj = ExamineCSV()
# obj.get_max_year()