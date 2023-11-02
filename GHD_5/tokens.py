import pandas as pd
import pickle5 as pickle

df = pd.read_csv('HLink_Abstracts_Updated_2019_2023.csv')
titles = df.columns.tolist()
sublists = [titles[i:i + 30] for i in range(1, len(titles), 30)]

filename = 'all_sublists.pkl'

with open(filename, 'wb') as file:
    pickle.dump(sublists, file)
