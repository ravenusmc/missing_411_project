# importing supporting libraries
import numpy as np
import pandas as pd

class ExamineCSV():

def __init__(self):
        self.data = pd.read_csv('./data/Missing.csv')