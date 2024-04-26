import pandas as pd
import pickle

df = pd.read_csv('042624-GlobalHealthDisparities-Top50.csv')
titles = df.columns.tolist()
sublists = [titles[i:i + 50] for i in range(1, len(titles), 50)]

filename = 'all_sublists.pkl'

with open(filename, 'wb') as file:
    pickle.dump(sublists, file)
