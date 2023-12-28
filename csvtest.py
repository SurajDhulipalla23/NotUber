import pandas as pd
import json

def build_graph():
    print('Building graph...')
    # Reading the node data and connection data from JSON files
    # node_coordinates_filepath = 'node_data.json'
    node_connections_filepath = 'edges.csv'

    # node_coordinates = read_json_file(node_coordinates_filepath)
    node_connections = pd.read_csv(node_connections_filepath)
    count = 0
    for index, row in node_connections.iterrows():
    # Iterate through columns 4 to 53 (inclusive)
        if index > 1:
            break
        for col_index in range(3, 51):  # Python uses zero-based indexing
            column_value = row[2] / row[col_index]
            print("start node = {} and edge_value = {}".format(row[0], column_value))

if __name__=="__main__":
    build_graph()