import json
import pickle5 as pickle

# Load the original data and make a backup
data = json.load(open('data.json', 'r'))
json.dump(data, open('data.json_bak', 'w'))

# Load the list of global health tokens
ghdbiomed = pickle.load(open('ListofGlobalHealthTokensOverlay.pickle', 'rb'))

label_id = {}
id_label = {}

for c, dictionary in enumerate(data['nodes']):
    # If the node's label is in ghdbiomed
    if dictionary['label'] in ghdbiomed:
             # Update shape to triangle and size to 1.0
        data['nodes'][c].update({'shape': 'triangle', 'size': 1.0})

    # Handle nodes with 'Global Health Disparity Research Cluster'
    for i in range(1, 11):  # Loop from 1 to 10 inclusive
        if 'SDSU Health Link Research Cluster' + str(i) in dictionary['label']:
            # Update shape to triangle and size to 3.0
            data['nodes'][c].update({'shape': 'triangle', 'size': 3.0})

# Save the updated data
json.dump(data, open('data.json', 'w'))
