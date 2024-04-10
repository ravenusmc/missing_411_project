# importing supporting libraries
import numpy as np
import pandas as pd

class ExamineCSV():

def __init__(self):
        self.data = pd.read_csv('./data/Missing.csv')


# Graphs to make:
# number of people missing by year - or decade? 
# States with the most missing people 
# -most common ages of people missing 
# -Sex of people missing - allow user to select decades?
# -Graph of Volume - Easter or Western US