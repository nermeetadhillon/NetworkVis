import json
import pickle
import random

# Load the list of lists containing labels.
ghdbiomed = pickle.load(open('all_sublists.pkl', 'rb'))

# Load the colors and shuffle them.
colors = pickle.load(open('RGBColors.pickle', 'rb'))
random.shuffle(colors)

# Load the JSON data.
data = json.load(open('data.json', 'r'))

# Backup the original data.
json.dump(data, open('data.json_bak', 'w'))

# Dictionary for keeping track of colors assigned to each id.
idscolors = {} 

# Update nodes with colors based on the sublist they belong to.
for c, node in enumerate(data['nodes']):
    for sublist_index, sublist in enumerate(ghdbiomed):
        if node['label'] in sublist:
            # Update the node color and size.
            colorstr = str(colors[sublist_index])
            color_change = {'color': 'rgb' + colorstr}
            size_change = {'size': 1.0}
            idscolors[node['id']] = color_change
            data['nodes'][c].update(size_change)
            data['nodes'][c].update(color_change)
        elif 'Global Health Disparities Research Cluster ' in node['label']:
            # Update the cluster node if the index matches.
            cluster_number = int(node['label'].split()[-1])
            if cluster_number - 1 < len(ghdbiomed):
                colorstr = str(colors[cluster_number - 1])
                color_change = {'color': 'rgb' + colorstr}
                size_change = {'size': 3.0}
                idscolors[node['id']] = color_change
                data['nodes'][c].update(size_change)
                data['nodes'][c].update(color_change)

# Update edges with the color of their source node.
for edge in data['edges']:
    if edge['source'] in idscolors:
        edge.update(idscolors[edge['source']])

# Save the updated JSON data.
json.dump(data, open('data.json', 'w'))
